from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import get_callable

from cas_provider.etree import etree, register_namespace, ElementRoot

class ServiceTicket(models.Model):
    user = models.ForeignKey(User)
    service = models.URLField(verify_exists=False)
    ticket = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return "%s (%s) - %s" % (self.user.username, self.service, self.created)
        
class LoginTicket(models.Model):
    ticket = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return "%s - %s" % (self.ticket, self.created)

CAS_URI = 'http://www.yale.edu/tp/cas'
register_namespace('cas', CAS_URI)
CAS = '{%s}' % CAS_URI

def auth_success_response(user):
    attrs = {}
    if settings.CAS_CUSTOM_ATTRIBUTES_CALLBACK:
        callback = get_callable(settings.CAS_CUSTOM_ATTRIBUTES_CALLBACK)
        attrs = callback(user)
    
    response = ElementRoot(CAS + 'serviceResponse')
    auth_success = etree.SubElement(response, CAS + 'authenticationSuccess')
    username = etree.SubElement(auth_success, CAS + 'user')
    username.text = user.username
    for name, value in attrs.items():
        element = etree.SubElement(auth_success, name)
        element.text = value
    return unicode(etree.tostring(response, encoding='utf-8'), 'utf-8')
