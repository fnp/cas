from django.template import Library
from ..models import Service


register = Library()


@register.simple_tag(takes_context=True)
def use_ssh(context):
    user = context['request'].user
    if user.is_anonymous: return True
    return Service.for_user(user).filter(uses_ssh=True).exists()
