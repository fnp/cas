from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .utils import get_key_details


class SSHKey(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('user'))
    key = models.TextField(_('key'))
    comment = models.CharField(_('comment'), max_length=255, editable=False)
    algorithm = models.CharField(_('algorithm'), max_length=32, editable=False)
    bit_length = models.IntegerField(_('bit length'), null=True, editable=False)
    sha256_hash = models.CharField(_('SHA256 hash'), max_length=128, editable=False)
    md5_hash = models.CharField(_('MD5 hash'), max_length=128, editable=False)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    last_seen_at = models.DateTimeField(_('last seen at'), null=True, editable=False)

    class Meta:
        ordering = ['created_at']
        verbose_name = _('SSH key')
        verbose_name_plural = _('SSH keys')
        unique_together = [('algorithm', 'bit_length', 'md5_hash')]

    def __str__(self):
        return self.comment

    def save(self, *args, **kwargs):
        det = get_key_details(self.key)
        self.comment = det['comment'][:255]
        self.algorithm = det['algo']
        self.bit_length = det['bits']
        self.md5_hash = det['md5']
        self.sha256_hash = det['sha256']
        return super().save(*args, **kwargs)
