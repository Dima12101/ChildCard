from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name="index"),
    path('info/', views.info, name="info"),
    path('contact/', views.contact, name="contact"),
    path('create_card_form/', views.create_card_form, name="create_card_form"),
    path('create_card_complete/', views.create_card_complete, name="create_card_complete")
]