from django.db import models
from django.utils.translation import ugettext_lazy as _
from . import BASE_DOMAINS



class Alias(models.Model):
    source = models.EmailField(_('source'), db_index=True)
    destination = models.EmailField(_('destination'))
    mode = models.CharField(
        _('mode'), max_length=255, default='', blank=True, choices=[
            ('', _('Forward everything')),
            ('@FORWARD', _('Do not forward e-mail marked as spam.'))
        ])

    class Meta:
        verbose_name = _('alias')
        verbose_name_plural = _('aliases')
        ordering = ('source', 'destination')

    def __str__(self):
        return '{} -> {}'.format(self.source, self.destination)

    @classmethod
    def get_from_user(cls, user):
        lookups = ["{}@{}".format(user.username, domain) for domain in BASE_DOMAINS]
        return cls.objects.filter(source__in=lookups)

    @classmethod
    def get_to_user(cls, user):
        lookups = ["{}@{}".format(user.username, domain) for domain in BASE_DOMAINS]
        return cls.objects.filter(destination__in=lookups)


class AliasUsage(models.Model):
    alias = models.ForeignKey(Alias, models.CASCADE, _('alias'))
    date = models.DateField(_('date'), auto_now_add=True)
    count = models.PositiveSmallIntegerField(_('count'))

    class Meta:
        unique_together = (('alias', 'date'),)
        verbose_name = _('alias usage')
        verbose_name_plural = _('alias usage')
