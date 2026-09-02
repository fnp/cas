from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.edit import UpdateView, FormView
from accounts.forms import UserBasicForm, OnboardingForm
from accounts.models import OnboardingEmail


class ProfileView(LoginRequiredMixin, UpdateView):
    form_class = UserBasicForm
    template_name = "account/profile.html"
    success_url = '/accounts/'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        retval = super().form_valid(form)
        messages.add_message(self.request, messages.INFO, _("Profile has been changed."))
        return retval


class OnboardingView(PermissionRequiredMixin, FormView):
    permission_required = 'auth.add_user'
    form_class = OnboardingForm
    template_name = "account/onboarding.html"
    success_url = reverse_lazy('onboarding')

    def form_valid(self, form):
        # Generate random password
        password = User.objects.make_random_password(length=12)

        # Create user
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=password,
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
        )

        # Send onboarding email
        template = OnboardingEmail.objects.first()
        if template:
            body = template.body.format(
                username=user.username,
                password=password,
                first_name=user.first_name,
                last_name=user.last_name,
            )
            send_mail(
                template.subject,
                body,
                None,  # Use DEFAULT_FROM_EMAIL
                [form.cleaned_data['email']],
            )
            messages.success(
                self.request,
                _("User %(username)s has been created and email sent to %(email)s.") % {
                    'username': user.username,
                    'email': form.cleaned_data['email'],
                }
            )
        else:
            messages.warning(
                self.request,
                _("User %(username)s has been created, but no email template is configured.") % {
                    'username': user.username,
                }
            )

        return super().form_valid(form)
