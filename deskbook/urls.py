from django.urls import path

from deskbook import views


app_name = 'deskbook'

urlpatterns = [
    path('vehicle/<int:vehicle_id>/', views.get_vehicle, name='vehicle'),

]
