from django.contrib import admin
from . import models


class AliasAdmin(admin.ModelAdmin):
    search_fields = ['source', 'destination']
    list_display = ['source', 'destination', 'mode']
    list_filter = ['mode']


admin.site.register(models.Alias, AliasAdmin)
