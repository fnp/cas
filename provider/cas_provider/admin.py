from django.contrib import admin

from cas_provider.models import ServiceTicket, LoginTicket

class ServiceTicketAdmin(admin.ModelAdmin):
    pass
admin.site.register(ServiceTicket, ServiceTicketAdmin)

class LoginTicketAdmin(admin.ModelAdmin):
    pass
admin.site.register(LoginTicket, LoginTicketAdmin)