# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_value, name='create_value'),
    path('read/', views.display_values, name='display_values'),
    path('read/<int:pk>/', views.display_value, name='display_value'),
    path('update/<int:pk>/', views.update_value, name='update_value'),
    path('delete/<int:pk>/', views.delete_value, name='delete_value'),
]
