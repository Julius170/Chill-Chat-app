from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.firstpage, name='firstpage'),
    path('signup/', views.signup, name='signup'), 
    path('login/', auth_views.LoginView.as_view(template_name ='Base/login.html'), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),    
]