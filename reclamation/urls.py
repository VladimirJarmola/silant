from django.urls import path

from reclamation import views


app_name = 'reclamation'

urlpatterns = [
    path('all/', views.reclamation, name='reclamation_all'),

    path('<int:car_id>', views.get_reclamation, name='car_reclamations'),
    path('<int:car_id>/failure_node/<int:failure_node_id>', views.get_reclamation, name='car_reclamations_failure_node'),
    path('<int:car_id>/recovery_method/<int:recovery_method_id>', views.get_reclamation, name='car_reclamations_recovery_method'),
    path('<int:car_id>/service_company/<int:service_company_id>', views.get_reclamation, name='car_reclamations_service_company'),

    path('failure_node/<int:failure_node_id>', views.reclamation, name='failure_node'),
    path('recovery_method/<int:recovery_method_id>', views.reclamation, name='recovery_method'),
    path('service_company/<int:service_company_id>', views.reclamation, name='service_company'),
]
