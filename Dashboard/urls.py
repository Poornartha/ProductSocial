from . import views
from django.conf.urls import url
from django.urls import path, include


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]