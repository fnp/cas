from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView
from .models import SSHKey


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
        return super().form_valid(form)

    
class DeleteSSHKeyView(LoginRequiredMixin, DeleteView):
    success_url = '/ssh/'

    def get_queryset(self):
        return SSHKey.objects.filter(user=self.request.user)
    
