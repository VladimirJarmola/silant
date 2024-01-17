from django.urls import path

from cars import views


app_name = 'cars'

urlpatterns = [
    path('', views.cars, name='cars'),
    path('search/', views.car_search, name='car_search'),
    path('car/<int:car_id>', views.get_car, name='car'),
    
]
