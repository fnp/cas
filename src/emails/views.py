from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Alias
from . import BASE_DOMAINS


@login_required
def my_aliases(request):
    return render(request, 'emails/my_aliases.html', {
        'base': ['{}@{}'.format(request.user.username, dom) for dom in BASE_DOMAINS],
        'to_me': Alias.get_to_user(request.user),
        'from_me': Alias.get_from_user(request.user),
        })
