from django.db import models
from django.utils.translation import gettext_lazy as _
from cas_provider.signals import cas_collect_custom_attributes


class OnboardingEmail(models.Model):
    subject = models.CharField(_("subject"), max_length=255)
    body = models.TextField(
        _("body"),
        help_text=_("Available placeholders: {username}, {password}, {first_name}, {last_name}")
    )

    class Meta:
        verbose_name = _("onboarding email template")
        verbose_name_plural = _("onboarding email templates")


def user_attributes(sender, user, **kwargs):
    return {
        'firstname': user.first_name,
        'lastname': user.last_name,
        'cn': ' '.join((user.first_name, user.last_name)),
        'email': user.email,
    }
cas_collect_custom_attributes.connect(user_attributes)
