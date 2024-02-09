from django.contrib import admin

from maintenance.models import Maintenance


class MaintenanceTabAdmin(admin.TabularInline):
    model = Maintenance
    fields = [
        'car',
        'service_company',
        'view_maintenance', 
        'Date_maintenance',
        'operating_hours',
        'work_order_number', 
        'work_order_date',
    ]
    readonly_fields = [
        'car',
        'service_company',
        'view_maintenance', 
        'Date_maintenance',
        'operating_hours',
        'work_order_number', 
        'work_order_date',
    ]
    extra = 0


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = [
        'car', 'view_maintenance', 'work_order_number', 'work_order_date', 'service_company'
    ]
    list_editable = ['work_order_number', 'work_order_date']
    list_filter = ['car__serial_number_vehicle']
    fields = [
        'car',
        'service_company',
        ('view_maintenance', 'Date_maintenance'),
        'operating_hours',
        ('work_order_number', 'work_order_date'),
    ]
    