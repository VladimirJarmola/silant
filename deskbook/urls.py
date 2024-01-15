from django.urls import path

from deskbook import views


app_name = 'deskbook'

urlpatterns = [
    path('', views.failure_node, name='failure_node'),

]
