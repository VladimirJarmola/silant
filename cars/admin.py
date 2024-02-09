from django.contrib import admin

from cars.models import Cars
from maintenance.admin import MaintenanceTabAdmin
from reclamation.admin import ReclamationTabAdmin


class CarTabAdmin(admin.TabularInline):
    model = Cars
    fields = [
        'serial_number_vehicle', 
        'vehicle_model', 
        'service_company', 
        'supply_contract',
        'date_shipped_from_factory',
    ]
    readonly_fields = [
        'serial_number_vehicle', 
        'vehicle_model', 
        'service_company', 
        'supply_contract',
        'date_shipped_from_factory',
    ]
    extra = 0


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = [
        'serial_number_vehicle', 'vehicle_model', 'supply_contract', 'date_shipped_from_factory', 'client', 'delivery_address'
    ]
    list_editable = ['supply_contract', ]
    search_fields = ['serial_number_vehicle']
    list_filter = ['vehicle_model']
    fields = [
        'client',
        'service_company',
        ('vehicle_model', 'serial_number_vehicle'),
        ('engine_model', 'serial_number_of_the_engine'),
        ('transmission_model', 'serial_number_of_the_transmission'),
        ('drive_axle_model', 'drive_axle_serial_number'),
        ('steering_axle_model', 'serial_number_of_the_steered_axle'),
        'supply_contract',
        'date_shipped_from_factory',
        'consignee',
        'delivery_address',
        'equipment',
    ]

    inlines = [MaintenanceTabAdmin, ReclamationTabAdmin,]
    