from django.contrib import admin
from . import models


class AliasAdmin(admin.ModelAdmin):
    list_display = ['source', 'destination']


admin.site.register(models.Alias, AliasAdmin)
