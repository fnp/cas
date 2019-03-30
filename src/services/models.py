from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(blank=True)
    key = models.CharField(max_length=255, blank=True)
    uses_ssh = models.BooleanField(default=False)
    groups = models.ManyToManyField('auth.Group', blank=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    class Meta:
        ordering = ('name', )

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
