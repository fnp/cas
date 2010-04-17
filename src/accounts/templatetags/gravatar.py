from django import template
from django.template.defaultfilters import stringfilter
import hashlib
import urllib

register = template.Library()

DEFAULTS = dict(size=80, rating='g', default='monsterid')

class GravatarNode(template.Node):

    def __init__(self, email, size):
        self.email = template.Variable(email)
        self.size = size

    def render(self, context):
        try:
            email = self.email.resolve(context)
        except template.VariableDoesNotExist:
            return ''

        gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email).hexdigest() + "?"
        gravatar_url += urllib.urlencode({'default': 'wavatar', 'size': str(self.size)})

        return gravatar_url

@register.tag
def gravatar(parser, token):
    try:
        _tag_name, email, size = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires two args" % token.contents.split()[0]

    return GravatarNode(email, int(size))




@register.filter(name='md5')
@stringfilter
def md5_hash(value):
    h = hashlib.md5()
    h.update(value)
    return h.hexdigest()
