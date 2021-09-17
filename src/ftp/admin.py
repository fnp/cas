from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _
from . import models
from .utils import generate_password


@admin.register(models.FtpUser)
class FtpUserAdmin(admin.ModelAdmin):
    fields = ['login', 'created_at', 'last_seen_at', 'password', 'password_set_at']
    readonly_fields = ['created_at', 'last_seen_at', 'password_set_at']

    def save_model(self, request, obj, form, change):
        if not obj.password:
            pwd = obj.set_password(save=False)
            self.message_user(
                request,
                mark_safe(
                    _('Password for <strong>%(login)s</strong> set to: <input disabled value="%(password)s">.') % {
                        "login": obj.login,
                        "password": pwd,
                    }
                )
            )
        return super().save_model(request, obj, form, change)


        
