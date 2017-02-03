from django import forms
from django.contrib.auth.models import User
from sportchallenger.models import MONTHS, Reservation, MyUser
from datetime import date
from django.core.exceptions import ValidationError



def validate_date(value):
    if value < date.today().year:
        raise ValidationError("Wskazana data: %s już minęła. Wprowadź inną datę." %value)

class LoginForm(forms.Form):
    username = forms.CharField(
        label='username',
        max_length=64,
        widget=forms.TextInput,
        required=True,
    )

    password = forms.CharField(
        label='password',
        max_length=64,
        widget=forms.PasswordInput,
        required=True,
    )

class MonthForm(forms.Form):
    year = forms.IntegerField(
        initial = date.today().year,
        label='Rok',
        validators=[validate_date]
    )
    month = forms.ChoiceField(
        initial=date.today().month,
        choices = MONTHS,
        label = 'Miesiąc'
    )

class ReservationForm(forms.Form):
    facility = forms.CharField(
        label = 'Obiekt',
        disabled = True
    )
    user = forms.CharField(
        label='Użytkownik',
        disabled=True
    )
    reservation_date = forms.CharField(
        label='Data rezerwacji',
        disabled=True
    )
    price = forms.CharField(
        label='Cena',
        disabled=True
    )

class NewUserForm(forms.Form):
    username = forms.CharField(
        label='nazwa użytkownika',
        max_length=64,
        widget=forms.TextInput,
        required=True,
    )
    password = forms.CharField(
        label='hasło',
        max_length=64,
        widget=forms.PasswordInput,
        required=True,
    )
    email =forms.CharField(
        max_length=64,
        widget=forms.EmailInput,
        required=True,
    )
    nickname = forms.CharField(
        max_length=64,
        widget=forms.TextInput,
        required=True,
    )
    photo = forms.FileField(
        label='zdjęcie'
    )
