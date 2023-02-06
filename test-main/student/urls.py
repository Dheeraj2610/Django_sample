from django.urls import path
from .views import index, register, login_user, logout_user, home

urlpatterns = [

    path('', index, name="index"),
    path('home/', home, name="home"),
    path('register/', register, name="register"),
    path("login_user/", login_user, name="login_user"),
    path("logout_user", logout_user, name="logout_user"),
]
