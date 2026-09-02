from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import path, reverse
from django.utils.translation import gettext_lazy as _
from .models import OnboardingEmail


@admin.register(OnboardingEmail)
class OnboardingEmailAdmin(admin.ModelAdmin):
    list_display = ('subject',)


admin.site.unregister(User)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    change_form_template = 'admin/accounts/user/change_form.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<id>/send-onboarding-email/',
                self.admin_site.admin_view(self.send_onboarding_email_view),
                name='accounts_user_send_onboarding_email',
            ),
        ]
        return custom_urls + urls

    def send_onboarding_email_view(self, request, id):
        user = self.get_object(request, id)
        if user is None:
            return self._get_obj_does_not_exist_redirect(request, User._meta, id)

        if request.method == 'POST':
            template = OnboardingEmail.objects.first()
            if not template:
                messages.error(request, _("No onboarding email template configured."))
            else:
                # Generate new password
                password = User.objects.make_random_password(length=12)
                user.set_password(password)
                user.save()

                body = template.body.format(
                    username=user.username,
                    password=password,
                    first_name=user.first_name,
                    last_name=user.last_name,
                )
                send_mail(
                    template.subject,
                    body,
                    None,
                    [user.email],
                )
                messages.success(
                    request,
                    _("Onboarding email sent to %(email)s. Password has been reset.") % {'email': user.email}
                )
            return HttpResponseRedirect(
                reverse('admin:auth_user_change', args=[user.pk])
            )

        context = {
            **self.admin_site.each_context(request),
            'opts': self.model._meta,
            'user_obj': user,
            'title': _("Send onboarding email"),
        }
        return TemplateResponse(
            request,
            'admin/accounts/user/send_onboarding_email.html',
            context,
        )
