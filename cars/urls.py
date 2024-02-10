from django.urls import path

from cars import views


app_name = 'cars'

urlpatterns = [
    # Поиск машины для незарегистрированных пользователей
    path('search/', views.car_search, name='car_search'),
    # Отображение всех машин для зарегестрированных пользователей
    path('all/', views.cars, name='cars'),
    # Пути для фильтрации по справочникам
    path('vehicle_model/<int:vehicle_model_id>', views.cars, name='vehicle'),
    path('engine_model/<int:engine_model_id>', views.cars, name='engine'),
    path('transmission_model/<int:transmission_model_id>', views.cars, name='transmission'),
    path('drive_axle_model/<int:drive_axle_model_id>', views.cars, name='drive_axle'),
    path('steering_axle_model/<int:steering_axle_model_id>', views.cars, name='steering_axle'),
    # добавление, удаление, редактирвование машин
    path('add_car/', views.add_car, name='add_car'),
    path('edit_car/<int:pk>', views.edit_car, name='edit_car'),
    path('remove_car/<int:car_id>', views.remove_car, name='remove_car'),
    # ajax запрос машины
    path('car_ajax', views.car_ajax, name='car_ajax'),
]
