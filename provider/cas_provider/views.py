from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.utils.encoding import smart_str
from django.utils.translation import ugettext_lazy as _

from cas_provider.forms import LoginForm
from cas_provider.models import ServiceTicket, LoginTicket, auth_success_response
from cas_provider.utils import create_service_ticket

import urlparse, urllib

try:
    from urlparse import parse_qs as url_parse_qs
except ImportError:
    from cgi import parse_qs as url_parse_qs

import logging
logger = logging.getLogger("cas.provider")

__all__ = ['login', 'validate', 'service_validate', 'logout']

def _add_query_param(url, param, value):
    parsed = urlparse.urlparse(url)
    query = url_parse_qs(smart_str(parsed.query))
    query[param] = [unicode(value, 'utf-8')]
    query = [ ((k, v) if len(v) != 1 else (k, v[0])) for k, v in query.iteritems() ]
    parsed = urlparse.ParseResult(parsed.scheme, parsed.netloc,
                                  parsed.path, parsed.params,
                                  urllib.urlencode(query), parsed.fragment)
    return parsed.geturl()


def login(request, template_name='cas/login.html', success_redirect='/accounts/'):
    service = request.GET.get('service', None)

    if request.user.is_authenticated():
        if service is not None:
            ticket = create_service_ticket(request.user, service)
            target = _add_query_param(service, 'ticket', ticket.ticket)
            logger.info("Redirecting to %s", target)
            return HttpResponseRedirect(target)
        else:
            logger.info("Redirecting to default: %s", success_redirect)
            return HttpResponseRedirect(success_redirect)

    errors = []
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        service = request.POST.get('service', None)
        lt = request.POST.get('lt', None)

        logger.debug("User %s logging in", username)

        try:
            login_ticket = LoginTicket.objects.get(ticket=lt)
        except:
            errors.append(_(u'Login ticket expired. Please try again.'))
        else:
            login_ticket.delete()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    if service is not None:
                        ticket = create_service_ticket(user, service)
                        target = _add_query_param(service, 'ticket', ticket.ticket)
                        return HttpResponseRedirect(target)
                    else:
                        return HttpResponseRedirect(success_redirect)
                else:
                    errors.append(_(u'This account is disabled.'))
            else:
                    errors.append(_(u'Incorrect username and/or password.'))

    form = LoginForm(service)
    return render_to_response(template_name, {'form': form, 'errors': errors}, context_instance=RequestContext(request))

def validate(request):
    service = request.GET.get('service', None)
    ticket_string = request.GET.get('ticket', None)
    if service is not None and ticket_string is not None:
        try:
            ticket = ServiceTicket.objects.get(ticket=ticket_string)
            username = ticket.user.username
            ticket.delete()
            return HttpResponse("yes\n%s\n" % username)
        except:
            pass
    return HttpResponse("no\n\n")

def service_validate(request):
    service = request.GET.get('service', None)
    ticket_string = request.GET.get('ticket', None)
    if service is None or ticket_string is None:
        return HttpResponse(r'''<cas:serviceResponse xmlns:cas="http://www.yale.edu/tp/cas">
            <cas:authenticationFailure code="INVALID_REQUEST">
                Not all required parameters were sent.
            </cas:authenticationFailure>
        </cas:serviceResponse>''', mimetype='application/xml')

    try:
        ticket = ServiceTicket.objects.get(ticket=ticket_string)
        ticket.delete()
        return HttpResponse(auth_success_response(ticket.user), mimetype='text/xml')
    except ServiceTicket.DoesNotExist:
        return HttpResponse(r'''<cas:serviceResponse xmlns:cas="http://www.yale.edu/tp/cas">
            <cas:authenticationFailure code="INVALID_TICKET">
                The provided ticket is invalid.
            </cas:authenticationFailure>
        </cas:serviceResponse>''', mimetype='application/xml')

def logout(request, template_name='cas/logout.html'):
    url = request.GET.get('url', None)
    auth_logout(request)
    return render_to_response(template_name, {'url': url}, context_instance=RequestContext(request))
