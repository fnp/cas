# Create your views here.
from django import http
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _
from django.views.decorators.http import require_POST
from accounts.forms import UserBasicForm, UserPasswordForm
from .models import Service
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


@login_required
def account_profile(request, basic_form=None, pass_form=None):
    return render(request, "account/profile.html", {
        "basic_form": basic_form or UserBasicForm(instance=request.user),
        "pass_form": pass_form or UserPasswordForm(),
        "services": Service.objects.all(),
    })


@require_POST
@login_required
def account_change_basic_profile(request):
    form = UserBasicForm(request.POST, instance=request.user)

    if form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, _("Profile has been changed."))
        return http.HttpResponseRedirect('/accounts/')

    return account_profile(request, basic_form=form)

@require_POST
@login_required
def account_change_password(request):
    form = UserPasswordForm(request.POST)

    if form.is_valid():
        request.user.set_password(form.cleaned_data['new_password'])
        request.user.save()

        messages.add_message(request, messages.INFO, _("Password has been changed."))
        return http.HttpResponseRedirect('/accounts/')

    return account_profile(request, pass_form=form)


class Register(FormView):
    form_class = UserCreationForm
    template_name = "account/register.html"

    def form_valid(self, form):
        user = form.save()
        user.backend='django.contrib.auth.backends.ModelBackend'
        login(self.request, user)
        return redirect('account_profile')
