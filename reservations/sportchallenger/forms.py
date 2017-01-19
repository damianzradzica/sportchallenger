from django import forms
from django.contrib.auth.models import User
from sportchallenger.models import MONTHS, Reservation, MyUser



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
        initial = 2017,
        label='Rok'
    )
    month = forms.ChoiceField(
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

class NewUserForm(forms.Form):
    pass
    # username =
    # password =
    # email =

class NewUserForm2(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['nickname', 'photo']