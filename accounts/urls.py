from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls import path, include


app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name ='logout'),
    path('signup/', views.SignUp, name='signup')
]
