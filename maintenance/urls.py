from django.urls import path

from maintenance import views


app_name = 'maintenance'

urlpatterns = [
    # Отображение всех ТО для зарегестрированных пользователей
    path('all/', views.maintenance, name='maintenance_all'),
    # ТО для конкретной машины
    path('<int:car_id>', views.get_maintenances, name='car_maintenances'),
    # Фильтрация ТО конкретной машины
    path('<int:car_id>/view_maintenance/<int:view_maintenance_id>', views.get_maintenances, name='car_maintenances_view'),
    path('<int:car_id>/service_company/<int:service_company_id>', views.get_maintenances, name='car_maintenances_service'),
    # Пути для фильтрации по справочникам всех ТО
    path('view_maintenance/<int:view_maintenance_id>', views.maintenance, name='view_maintenance'),
    path('car/<int:car_id>', views.maintenance, name='car'),
    path('service_company/<int:service_company_id>', views.maintenance, name='service_company'),
    # добавление, удаление, редактирвование ТО
    path('add_maintenance/', views.add_maintenance, name='add_maintenance'),
    path('add_maintenance/<int:car_id>', views.add_maintenance, name='add_maintenance_car'),
    path('edit_maintenance/<int:view_maintenance_id>', views.edit_maintenance, name='edit_maintenance'),
    path('remove_maintenance/<int:view_maintenance_id>', views.remove_maintenance, name='remove_maintenance'),
]
