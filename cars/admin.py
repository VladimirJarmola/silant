from django.contrib import admin

from cars.models import ServiceCompany, Cars, Reclamation


admin.site.register(ServiceCompany)
admin.site.register(Cars)
admin.site.register(Reclamation)
