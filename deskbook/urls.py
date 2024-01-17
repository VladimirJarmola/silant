from django.urls import path

from deskbook import views


app_name = 'deskbook'

urlpatterns = [
    path('vehicle/<int:vehicle_id>/', views.get_vehicle, name='vehicle'),
    path('engine/<int:engine_id>/', views.get_engine, name='engine'),
    path('transmission/<int:transmission_id>/', views.get_transmission, name='transmission'),
    path('drive_axle/<int:drive_axle_id>/', views.get_drive_axle, name='drive_axle'),
    path('steering_axle/<int:steering_axle_id>/', views.get_steering_axle, name='steering_axle'),

]
