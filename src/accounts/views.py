from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext as _
from django.views.generic.edit import UpdateView
from accounts.forms import UserBasicForm


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
