from django.contrib import admin
from . import models


class HookInline(admin.TabularInline):
    model = models.Hook


class ServiceAdmin(admin.ModelAdmin):
    filter_horizontal = ['groups', 'users']
    inlines = [
            HookInline,
        ]


admin.site.register(models.Service, ServiceAdmin)


