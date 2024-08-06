from django.urls import path
from .import views
from django.contrib.auth import views as auth_view
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('sign_up/', views.sign_up, name='users-sign-up'),
    path('profile/',views.profile, name='users-profile'),
    path('', auth_view.LoginView.as_view(template_name='users/login.html'),
         name='users-login'),
    path('logout/', views.logout_Fun ,name='users-logout'),

]   
