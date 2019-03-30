from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Service(models.Model):
    name = models.CharField(_('name'), max_length=255)
    url = models.URLField(_('URL'), blank=True)
    key = models.CharField(_('key'), max_length=255, blank=True)
    uses_ssh = models.BooleanField(_('uses SSH'), default=False)
    groups = models.ManyToManyField('auth.Group', verbose_name=_('groups'), blank=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_('users'), blank=True)

    class Meta:
        ordering = ('name', )
        verbose_name = _('service')
        verbose_name_plural = _('services')

    def __str__(self):
        return self.name

    def all_users(self):
        return User.objects.filter(
                models.Q(service=self) |
                models.Q(groups__service=self)
            ).distinct()

    @classmethod
    def for_user(cls, user):
        return cls.objects.filter(models.Q(users=user) | models.Q(groups__user=user))


class Hook(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
