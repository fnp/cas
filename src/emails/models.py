from django.db import models
from django.utils.translation import ugettext_lazy as _


class Alias(models.Model):
    source = models.EmailField(_('source'), db_index=True)
    destination = models.EmailField(_('destination'))

    class Meta:
        verbose_name = _('alias')
        verbose_name_plural = _('aliases')
        ordering = ('source', 'destination')

    def __str__(self):
        return '{} -> {}'.format(self.source, self.destination)
