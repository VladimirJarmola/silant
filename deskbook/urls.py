from django.urls import path

from deskbook import views


app_name = 'deskbook'

urlpatterns = [

    path('vehicle/', views.get_deskbook, name='vehicle'),
    path('engine/', views.get_deskbook, name='engine'),
    path('transmission/', views.get_deskbook, name='transmission'),
    path('drive_axle/', views.get_deskbook, name='drive_axle'),
    path('steering_axle/', views.get_deskbook, name='steering_axle'),
    path('failure_node/', views.get_deskbook, name='failure_node'),
    path('recovery_method/', views.get_deskbook, name='recovery_method'),
    path('view_maintenance/', views.get_deskbook, name='view_maintenance'),

    path('add_deskbook/<slug:slug>', views.add_deskbook, name='add_deskbook'),
    path('edit_deskbook/<slug:slug>/<int:item_id>', views.edit_deskbook, name='edit_deskbook'),
    path('remove_deskbook/<slug:slug>/<int:item_id>', views.remove_deskbook, name='remove_deskbook'),
]
