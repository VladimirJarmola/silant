from django.urls import path

from reclamation import views


app_name = 'reclamation'

urlpatterns = [
    # Отображение всех рекламаций
    path('all/', views.reclamation, name='reclamation_all'),
    # Рекламации конкретной машины
    path('<int:car_id>', views.get_reclamation, name='car_reclamations'),
    # Фильтрация рекламаций конкретной машины
    path('<int:car_id>/failure_node/<int:failure_node_id>', views.get_reclamation, name='car_reclamations_failure_node'),
    path('<int:car_id>/recovery_method/<int:recovery_method_id>', views.get_reclamation, name='car_reclamations_recovery_method'),
    path('<int:car_id>/service_company/<int:service_company_id>', views.get_reclamation, name='car_reclamations_service_company'),
    # Фильтрация всех рекламаций
    path('failure_node/<int:failure_node_id>', views.reclamation, name='failure_node'),
    path('recovery_method/<int:recovery_method_id>', views.reclamation, name='recovery_method'),
    path('service_company/<int:service_company_id>', views.reclamation, name='service_company'),
    # Добавление, удаление, редактирование рекламации
    path('add_reclamation/', views.add_reclamation, name='add_reclamation'),
    path('add_reclamation/<int:car_id>', views.add_reclamation, name='add_reclamation_car'),
    path('edit_reclamation/<int:reclamation_id>', views.edit_reclamation, name='edit_reclamation'),
    path('remove_reclamation/<int:reclamation_id>', views.remove_reclamation, name='remove_reclamation'),
]
