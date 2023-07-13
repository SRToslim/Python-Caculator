from django.urls import path
from .views import index, calculation

urlpatterns = [
    path('', index),
    path('calculation', calculation),
]