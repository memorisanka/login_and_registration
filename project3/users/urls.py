from . import views
from django.urls import path
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('accounts/profile/', auth_view.TemplateView.as_view(template_name='users/profile.html'), name='profile'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
]