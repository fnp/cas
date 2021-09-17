from crypt import crypt
from django.db import models
from django.contrib.messages import add_message
from django.utils.timezone import now
from .utils import generate_password


class FtpUser(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_seen_at = models.DateTimeField(null=True, editable=False)
    login = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, blank=True)
    password_set_at = models.DateTimeField(null=True, editable=False)

    def __str__(self):
        return self.login

    def set_password(self, save=True):
        pwd = generate_password()
        self.password = crypt(pwd)
        self.password_set_at = now()
        if save:
            self.save()
        return pwd
