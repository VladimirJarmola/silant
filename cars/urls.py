from django.urls import path

from cars import views


app_name = 'cars'

urlpatterns = [
    path('search/', views.car_search, name='car_search'),
    path('', views.cars, name='cars'),
]
