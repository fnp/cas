from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Alias
from . import BASE_DOMAINS


@login_required
def my_aliases(request, user=None):
    user = user or request.user  
    return render(request, 'emails/my_aliases.html', {
        'user': user,
        'base': ['{}@{}'.format(user.username, dom) for dom in BASE_DOMAINS],
        'from_me': Alias.get_from_user(user),
        })


@permission_required('emails.can_add_alias')
def user_aliases(request, username):
    user = get_object_or_404(User, username=username)
    return my_aliases(request, user=user)

