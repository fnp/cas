from django.contrib import admin
from . import models


@admin.register(models.Alias)
class AliasAdmin(admin.ModelAdmin):
    search_fields = ['source', 'destination']
    list_display = ['source', 'destination', 'mode']
    list_filter = ['mode']


@admin.register(models.SharedMailbox)
class SharedMailboxAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    filter_horizontal = ['users']

