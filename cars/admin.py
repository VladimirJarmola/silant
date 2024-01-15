from django.contrib import admin

from cars.models import ServiceCompany, Cars, Maintenance, Reclamation


admin.site.register(ServiceCompany)
admin.site.register(Cars)
admin.site.register(Maintenance)
admin.site.register(Reclamation)
