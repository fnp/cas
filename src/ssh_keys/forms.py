from django import forms
from .models import SSHKey


class SSHKeyForm(forms.ModelForm):
    model = SSHKey
