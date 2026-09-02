from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class UserBasicForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)


class OnboardingForm(forms.Form):
    first_name = forms.CharField(label=_("First name"), max_length=150)
    last_name = forms.CharField(label=_("Last name"), max_length=150)
    email = forms.EmailField(label=_("External email"))
    username = forms.CharField(
        label=_("Username"),
        max_length=150,
        help_text=_("Auto-generated from first and last name")
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(_("User with this username already exists."))
        return username

