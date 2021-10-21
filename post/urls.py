from django.urls import path
from . import views


urlpatterns = [
    path('', views.index), 
    path('validate', views.validate),
    path('register', views.register), 
    path('verify', views.verify),
    path('login', views.login),
    path('signup', views.signup),
]
