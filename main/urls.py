from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from main.forms import UserLoginForm

app_name = 'main'
urlpatterns = [
    # Authentication
    path('', views.dashboard_view, name='dashboard'),
    path('login/', LoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]