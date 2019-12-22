from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('setting_account_form/', views.setting_account_form, name="setting_account_form"),
    path('setting_account_complete/', views.setting_account_complete, name="setting_account_complete"),
    path('create_card_form/', views.create_card_form, name="create_card_form"),
    path('create_card_complete/', views.create_card_complete, name="create_card_complete")
]