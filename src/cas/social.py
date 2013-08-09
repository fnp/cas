from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class LooseSocialAccountAdapter(DefaultSocialAccountAdapter):
    def validate_disconnect(self, account, accounts):
        """
        Validate whether or not the socialaccount account can be
        safely disconnected.
        """
        if len(accounts) == 1:
            # No usable password would render the local account unusable
            if not account.user.has_usable_password():
                raise ValidationError(_("Your account has no password set up."))
            # No email address, no password reset
            if not account.user.email:
                raise ValidationError(_("Your account has no e-mail address."))
