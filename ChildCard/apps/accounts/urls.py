from django_registration.backends.activation.views import RegistrationView
from django.contrib.auth.views import PasswordResetView
from django.urls import path, include
from .forms import EmailValidationOnForgotPassword
from .forms import EmailValidationOnRegister

urlpatterns = [
    path('register/', RegistrationView.as_view(form_class=EmailValidationOnRegister),
         name='form_valid'), # Addition check email
    path('', include('django.contrib.auth.urls')),
    path('', include('django_registration.backends.activation.urls')),
    path('sifre-sifirla/', PasswordResetView.as_view(form_class=EmailValidationOnForgotPassword),
         name='password_reset'), # Addition check email
]
