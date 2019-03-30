from django.views.generic import DetailView
from .models import Service


class SshAuthorizedKeysView(DetailView):
    model = Service
    template_name = 'services/ssh_authorized_keys.txt'
    content_type = 'text/plain'

    def get_object(self):
        obj = super().get_object()
        if self.request.GET.get('key') != obj.key:
            obj = None
        return obj

