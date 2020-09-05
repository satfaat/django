from django.urls import path
from . import views # . is blogapp dir

urlpatterns = [
    path('', views.home, name='blog-home'),
]