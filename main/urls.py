from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'main'
urlpatterns = [
    # Authentication
    path('', views.dashboard_view, name='dashboard'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]