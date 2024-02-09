from django.urls import path

from deskbook import views


app_name = 'deskbook'

urlpatterns = [

    path('vehicle_model/', views.get_deskbook, name='vehicle_model'),
    path('engine_model/', views.get_deskbook, name='engine_model'),
    path('transmission_model/', views.get_deskbook, name='transmission_model'),
    path('drive_axle_model/', views.get_deskbook, name='drive_axle_model'),
    path('steering_axle_model/', views.get_deskbook, name='steering_axle_model'),
    path('failure_node/', views.get_deskbook, name='failure_node'),
    path('recovery_method/', views.get_deskbook, name='recovery_method'),
    path('view_maintenance/', views.get_deskbook, name='view_maintenance'),

    path('add_deskbook/<slug:slug>', views.add_deskbook, name='add_deskbook'),
    path('edit_deskbook/<slug:slug>/<int:item_id>', views.edit_deskbook, name='edit_deskbook'),
    path('remove_deskbook/<slug:slug>/<int:item_id>', views.remove_deskbook, name='remove_deskbook'),

    path('api_deskbook/', views.api_deskbook, name='api_deskbook'),
]
