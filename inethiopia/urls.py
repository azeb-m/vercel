from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name='show'),
    # Add more paths as needed
]