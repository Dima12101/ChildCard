from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name="index"),
    path('info/', views.info, name="info"),
    path('contact/', views.contact, name="contact"),
]