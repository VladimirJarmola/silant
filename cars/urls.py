from django.urls import path

from cars import views


app_name = 'cars'

urlpatterns = [
    path('search/', views.cars, name='search'),
]
