# Create your views here.
from django import http
from django.utils.translation import ugettext as __
from django.views.generic.simple import direct_to_template
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from accounts.forms import UserBasicForm, UserPasswordForm

@login_required
def account_profile(request, basic_form=None, pass_form=None):
    return direct_to_template(request, "account/profile.html", {
        "basic_form": basic_form or UserBasicForm(instance=request.user),
        "pass_form": pass_form or UserPasswordForm(),
    })


@require_POST
@login_required
def account_change_basic_profile(request):
    form = UserBasicForm(request.POST, instance=request.user)

    if form.is_valid():
        form.save()
        request.user.message_set.create(message=__("Profile has been changed."))
        return http.HttpResponseRedirect('/accounts/')

    return account_profile(request, basic_form=form)

@require_POST
@login_required
def account_change_password(request):
    form = UserPasswordForm(request.POST)

    if form.is_valid():
        request.user.set_password(form.cleaned_data['new_password'])
        request.user.save()

        request.user.message_set.create(message=__("Password has been changed."))
        return http.HttpResponseRedirect('/accounts/')

    return account_profile(request, pass_form=form)
