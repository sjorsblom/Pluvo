from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    # Authentication
    path('', views.dashboard_view, name='dashboard'),
]