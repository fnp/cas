from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SshKeysConfig(AppConfig):
    name = 'ssh_keys'
    verbose_name = _('SSH keys')
