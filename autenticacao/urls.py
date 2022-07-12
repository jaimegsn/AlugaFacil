from django.urls import path
from autenticacao import views

urlpatterns = [
    path("register/", views.register, name="auth_urls-register"),
    path("login/", views.login, name="auth_urls-login"),
    path("logout/", views.logout, name="auth_urls-logout")
]
