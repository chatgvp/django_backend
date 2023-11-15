# authapp/urls.py
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('test_token/', views.test_token, name='test_token'),
    path('logout/', views.logout, name='logout'),
    # path('read/', views.display_values, name='display_values'),
]
