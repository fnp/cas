from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class SSHKey(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('user'))
    key = models.TextField(_('key'))
    comment = models.CharField(_('comment'), max_length=255, blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = _('SSH key')
        verbose_name_plural = _('SSH keys')

    def __str__(self):
        return self.comment

    def save(self, *args, **kwargs):
        self.comment = self.key.rsplit()[-1][:255]
        return super().save(*args, **kwargs)
