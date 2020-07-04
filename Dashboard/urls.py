from . import views
from django.conf.urls import url
from django.urls import path, include
app_name = 'Dashboard'


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('shirt', views.shirt, name='shirt'),
    path('shoes', views.shoes, name='shoes'),
    path('shorts', views.shorts, name='shorts'),
    path('jeans', views.jeans, name='jeans'),
    path('red', views.red, name='red'),
    path('blue', views.blue, name='blue'),
    path('yellow', views.yellow, name='yellow'),
    path('black', views.black, name='black'),
    path('green', views.green, name='green'),
    path('white', views.white, name='white'),
    path('sugessions', views.suggesions, name='sugessions'),
]
