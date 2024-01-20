from django.urls import path

from cars import views


app_name = 'cars'

urlpatterns = [
    path('search/', views.car_search, name='car_search'),
    path('all/', views.cars, name='cars'),
    path('vehicle_model/<int:vehicle_model_id>', views.cars, name='vehicle'),
    path('engine_model/<int:engine_model_id>', views.cars, name='engine'),
    path('transmission_model/<int:transmission_model_id>', views.cars, name='transmission'),
    path('drive_axle_model/<int:drive_axle_model_id>', views.cars, name='drive_axle'),
    path('steering_axle_model/<int:steering_axle_model_id>', views.cars, name='steering_axle'),
    path('car/<int:car_id>', views.get_car, name='car'),
]
