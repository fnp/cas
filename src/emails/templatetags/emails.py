from django.template import Library
from emails.models import Alias


register = Library()


@register.simple_tag(takes_context=True)
def use_email(context):
    user = context['request'].user
    if user.is_anonymous: return False
    return user.groups.filter(name='e-mail').exists()


@register.inclusion_tag('emails/list_aliases.html', takes_context=True)
def list_aliases(context, emails):
    if isinstance(emails, str):
        emails = [emails]
    admin_links = context.get('admin_links', context['request'].user.has_perm('emails.can_change_alias'))
    return {
        "admin_links": admin_links,
        "aliases": [a.source for a in Alias.objects.filter(destination__in=emails)],
        "request": context['request'],
    }
