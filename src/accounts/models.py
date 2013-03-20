from django.db import models


class Service(models.Model):
    ordering = models.IntegerField()
    name = models.CharField(max_length=255)
    url = models.URLField()
    image = models.ImageField(upload_to='accounts/service/')

    class Meta:
        ordering = ('ordering', )
