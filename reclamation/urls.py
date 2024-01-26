from django.urls import path

from reclamation import views


app_name = 'reclamation'

urlpatterns = [
    path('all/', views.reclamation, name='reclamation'),
    path('failure_node/<int:failure_node_id>', views.reclamation, name='failure_node'),
    path('recovery_method/<int:recovery_method_id>', views.reclamation, name='recovery_method'),
    path('service_company/<int:service_company_id>', views.reclamation, name='service_company'),
    path('<int:reclamation_id>', views.get_reclamation, name='this_reclamation'),
]
