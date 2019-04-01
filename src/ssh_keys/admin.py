from django.contrib import admin
from django.db.models import F
from .models import SSHKey


class SSHKeyAdmin(admin.ModelAdmin):
    fields = ['user',  'key', 'algorithm', 'bit_length', 'md5_hash', 'created_at', 'last_seen_at']
    readonly_fields = ['algorithm', 'bit_length', 'md5_hash', 'created_at', 'last_seen_at']
    list_display = ['comment', 'last_seen_at', 'user', 'md5_hash', 'algorithm', 'bit_length', 'created_at']
    ordering = (F('last_seen_at').desc(nulls_last=True),)

admin.site.register(SSHKey, SSHKeyAdmin)
