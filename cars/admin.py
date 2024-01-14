from django.contrib import admin

from cars.models import ServiceCompany, Cars


admin.site.register(ServiceCompany)
admin.site.register(Cars)