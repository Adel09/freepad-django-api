from django.urls import path, include
from . import views

urlpatterns = [
    path('v1/register', views.register, name='register'), #POST
    path('v1/profile', views.getProfile), #GET
    path('v1/requests', views.getRequests), #GET
    path('v1/login', views.loginuser), #POST
    path('v1/requests/create', views.createRequest), #POST
]