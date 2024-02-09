from django.contrib import admin

from reclamation.models import Reclamation


class ReclamationTabAdmin(admin.TabularInline):
    model = Reclamation
    fields = [
        'car',
        'service_company',
        'date_of_refusal', 
        'operating_hours', 
        'restore_date',
        'failure_node', 
        'description_of_failure',
        'recovery_method', 
        'parts_used',
    ]
    readonly_fields = [
        'car',
        'service_company',
        'date_of_refusal', 
        'operating_hours', 
        'restore_date',
        'failure_node', 
        'description_of_failure',
        'recovery_method', 
        'parts_used',
    ]


@admin.register(Reclamation)
class ReclamationAdmin(admin.ModelAdmin):
    list_display = ['car', 'date_of_refusal', 'failure_node', 'recovery_method', 'service_company']
    search_fields = ['description_of_failure', 'parts_used', 'failure_node', 'recovery_method']
    list_filter = ['car__serial_number_vehicle', 'failure_node', 'recovery_method']
    fields = [
        'car',
        'service_company',
        ('date_of_refusal', 'operating_hours', 'restore_date'),
        ('failure_node', 'description_of_failure'),
        ('recovery_method', 'parts_used'),
    ]
    