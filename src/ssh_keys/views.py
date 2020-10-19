from datetime import datetime, timedelta
import re
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db import IntegrityError
from django.db.models import Q
from django import http
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from django.utils.translation import ugettext as _
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DeleteView
from services.models import Service
from .models import SSHKey
from .utils import parse_log_line


class SSHKeysView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return SSHKey.objects.filter(user=self.request.user)


class AddSSHKeyView(LoginRequiredMixin, CreateView):
    fields = ['key']
    model = SSHKey
    success_url = '/ssh/'
    template_name = 'ssh_keys/sshkey_add.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            return super().form_valid(form)
        except ValueError as e:
            messages.add_message(self.request, messages.ERROR, e)
        except IntegrityError:
            messages.add_message(self.request, messages.ERROR, _("Key already in the database."))
        return http.HttpResponseRedirect(self.success_url)


    
class DeleteSSHKeyView(LoginRequiredMixin, DeleteView):
    success_url = '/ssh/'

    def get_queryset(self):
        return SSHKey.objects.filter(user=self.request.user)


@csrf_exempt
def ssh_keys_seen(request):
    key = request.GET.get('key')
    service = get_object_or_404(Service, key=key)
    n = now()

    logline_re = r'^(?P<time>\w{3}\s+\d+\s+\d\d:\d\d:\d\d).*: Accepted publickey for .* from .* port .* ssh2: (?P<algo>\w+) (?P<hash>[a-f0-9:]+)$'

    last_seen = {}
    for line in request.body.decode('latin1').split('\n'):
        if not line.strip():
            continue
        data = parse_log_line(line)
        if data is None:
            continue
        dt = data['datetime']
        algo = data['algo']
        if 'md5' in data:
            hash_type = 'md5'
            hash_value = data['md5']
        else:
            hash_type = 'sha256'
            hash_value = data['sha256']
        key = algo, hash_type, hash_value
        last_seen[key] = max(last_seen.get(key, dt), dt)

    for key, dt in last_seen.items():
        algo, hash_type, hash_value = key
        SSHKey.objects.filter(
            Q(last_seen_at=None) | Q(last_seen_at__lt=dt),
            algorithm=algo,
            **{f'{hash_type}_hash': hash_value}
        ).update(
            last_seen_at=dt
        )

    return http.HttpResponse('ok')

