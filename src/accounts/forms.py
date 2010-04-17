from django import forms
from django.contrib.auth.models import User as DjangoUser
from django.utils.translation import ugettext_lazy as _

class UserBasicForm(forms.ModelForm):

    class Meta:
        model = DjangoUser
        fields = ('first_name', 'last_name', 'email',)


class UserPasswordForm(forms.Form):

    new_password = forms.CharField(widget=forms.PasswordInput(),
                        label=_("Your new password"))
    verifier = forms.CharField(widget=forms.PasswordInput(),
                        label=_("Repeated password"))

    def clean(self):
        if 'verifier' not in self.cleaned_data or 'new_password' not in self.cleaned_data:
            return self.cleaned_data

        if self.cleaned_data['verifier'] != self.cleaned_data['new_password']:
            raise forms.ValidationError(_("Passwords do not match!"))

        return self.cleaned_data
