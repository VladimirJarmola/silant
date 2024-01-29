from django.urls import path

from maintenance import views


app_name = 'maintenance'

urlpatterns = [
    path('all/', views.maintenance, name='maintenance_all'),

    path('<int:car_id>', views.get_maintenances, name='car_maintenances'),
    path('<int:car_id>/view_maintenance/<int:view_maintenance_id>', views.get_maintenances, name='car_maintenances_view'),
    path('<int:car_id>/service_company/<int:service_company_id>', views.get_maintenances, name='car_maintenances_service'),

    path('view_maintenance/<int:view_maintenance_id>', views.maintenance, name='view_maintenance'),
    path('car/<int:car_id>', views.maintenance, name='car'),
    path('service_company/<int:service_company_id>', views.maintenance, name='service_company'),
]
