from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = 'search'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('limeroad', views.limeroad, name='limeroad'),
    path('zobello', views.zobello, name='zobello'),
    path('randomize', views.randomize, name='randomize'),
    path('', views.landing, name="landing"),
    path('trending', views.trending, name="trending"),
    path('search-bewakoof', views.search_bewakoof, name="search-bewakoof"),
    path('search-limeroad', views.search_limeroad, name="search-limeroad"),
    path('search-zobello', views.search_zobello, name="search-zobello"),
    path('search-random', views.search_random, name="search-random"),
    path('trend/<int:pk>/', views.trend, name="trend"),
]
