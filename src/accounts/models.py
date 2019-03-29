from django.conf import settings
from django.db import models
from cas_provider.signals import cas_collect_custom_attributes


class Service(models.Model):
    ordering = models.IntegerField()
    name = models.CharField(max_length=255)
    url = models.URLField()
    image = models.ImageField(upload_to='accounts/service/')

    class Meta:
        ordering = ('ordering', )


class ServiceUser(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class ServiceGroup(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    group = models.ForeignKey('auth.Group', on_delete=models.CASCADE)


def user_attributes(sender, user, **kwargs):
    return {
        'firstname': user.first_name,
        'lastname': user.last_name,
        'cn': ' '.join((user.first_name, user.last_name)),
        'email': user.email,
    }
cas_collect_custom_attributes.connect(user_attributes)
