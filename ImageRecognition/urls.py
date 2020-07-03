from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('limeroad', views.limeroad, name='limeroad'),
    path('zobello', views.zobello, name='zobello'),
    path('randomize', views.randomize, name='randomize'),
    path('landing', views.landing, name="landing"),
    path('trending', views.trending, name="trending"),
]