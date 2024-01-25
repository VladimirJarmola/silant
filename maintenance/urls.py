from django.urls import path

from maintenance import views


app_name = 'maintenance'

urlpatterns = [
    path('all/', views.maintenance, name='maintenance'),
    path('view_maintenance/<int:view_maintenance_id>', views.maintenance, name='view_maintenance'),
    path('car/<int:car_id>', views.maintenance, name='car'),
    path('service_company/<int:service_company_id>', views.maintenance, name='service_company'),
    path('<int:maintenance_id>', views.get_maintenance, name='this_maintenance'),
]
