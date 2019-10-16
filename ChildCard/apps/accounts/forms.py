from smtplib import SMTPDataError

from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django_registration.forms import RegistrationForm
from django_registration import validators

from ChildCard import settings


class EmailValidationOnForgotPassword(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email).exists():
            msg = "Данный адрес электронной почты не зарегистрирован."
            self.add_error('email', msg)
        elif not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = "Данный адрес электронной почты не активирован."
            self.add_error('email', msg)

        return email


class EmailValidationOnRegister(RegistrationForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = validators.DUPLICATE_EMAIL
            self.add_error('email', msg)
        # settings.EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        # try:
        #     send_mail('TestValid', '', settings.DEFAULT_FROM_EMAIL, [email])
        # except SMTPDataError:
        #     msg = 'Данный адрес электронной почты не существует'
        #     self.add_error('email', msg)
        # settings.EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        return email

