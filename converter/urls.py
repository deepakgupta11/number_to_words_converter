from django.urls import path
from . import views

urlpatterns = [
    path('', views.convert_amount, name='convert_amount'),
]
