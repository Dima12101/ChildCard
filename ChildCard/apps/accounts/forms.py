from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django_registration.forms import RegistrationForm
from django_registration import validators


class EmailValidationOnForgotPassword(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = "Данный адрес электронной почты не зарегистрирован."
            self.add_error('email', msg)
        return email


class EmailValidationOnRegister(RegistrationForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = validators.DUPLICATE_EMAIL
            self.add_error('email', msg)
        return email
