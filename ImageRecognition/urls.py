from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('limeroad', views.limeroad, name='limeroad'),
    path('zobello', views.zobello, name='zobello')
]