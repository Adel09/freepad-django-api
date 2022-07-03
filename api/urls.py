from django.urls import path, include
from . import views

urlpatterns = [
    path('v1/register', views.register, name='register'),
    path('v1/profile', views.getProfile),
    path('v1/requests', views.getRequests),
    path('v1/requests/create', views.createRequest),
]