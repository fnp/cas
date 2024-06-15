from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SshKeysConfig(AppConfig):
    name = 'ssh_keys'
    verbose_name = _('SSH keys')
