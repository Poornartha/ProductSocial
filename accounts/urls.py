from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

app_name = 'accounts'
urlpatterns = [
    url(r'login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name = 'login'),
    url(r'logout/$', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name ='logout'),
    url(r'signup/$', views.SignUp.as_view(), name='signup')
]
