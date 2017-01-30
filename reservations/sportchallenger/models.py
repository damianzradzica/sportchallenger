from django.db import models
from django.contrib.auth.models import User


# Create your models here.

MONTHS = (
    (1, 'styczeń'),
    (2, 'luty'),
    (3, 'marzec'),
    (4, 'kwiecień'),
    (5, 'maj'),
    (6, 'czerwiec'),
    (7, 'lipiec'),
    (8, 'sierpień'),
    (9, 'wrzesień'),
    (10, 'październik'),
    (11, 'listopad'),
    (12, 'grudzień'),
)

KINDS = (
    (1, 'hala wielofukcyjna'),
    (2, 'boisko piłkarskie'),
    (3, 'pływalnia'),
    (4, 'obiekt lekkoatletyczny')
)

SPORTS = (
    (1, 'piłka nożna'),
    (2, 'koszykówka'),
    (3, 'siatkówka'),
    (4, 'tenis'),
    (5, 'futsal'),
    (6, 'pływanie'),
    (7, 'piłka wodna'),
    (8, 'biegi'),
    (9, 'rzuty'),
    (10, 'skoki')
)

RATING= (
    (1, 'obiekt bez wyposażenia'),
    (2, 'komplet przyrządów sportowych do obsługiwanych dyscyplin'),
    (3, 'klimatyzacja / sztuczne oświetlenie')
)


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=200, null = True)
    photo = models.ImageField(upload_to = 'static/pictures', blank = True, null = True)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nickname

class SportFacility(models.Model):
    name = models.CharField(max_length=200)
    photos = models.ImageField(upload_to = 'static/pictures', blank = True, null = True) #tutaj zapytać jak zrobić galerię
    kind = models.IntegerField(choices = KINDS)
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    sports = models.IntegerField(choices = SPORTS) #tutai i w innych przypadkach trzeba stworzyć i dodawać klasę
    rating = models.IntegerField(choices = RATING, default = 1)
    description = models.TextField(null = True, blank = True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    facility = models.ForeignKey(SportFacility, related_name='facility_reservation', null = True, blank = True)
    user = models.ForeignKey(MyUser, related_name='user_reservation', null = True, blank = True)
    creation_date = models.DateTimeField(auto_now_add=True)
    reservation_date = models.DateField(null = True, blank = True)

    def __str__(self):
        return '{}'.format(self.reservation_date)

# class Basket(models.Model):
#     user = models.ForeignKey(MyUser, related_name='user-basket', null=True, blank=True)
#     reservation = models.ForeignKey(Reservation, related_name='reservation-field', null=True, blank=True)
#     creation_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.creation_date

# zmiany można wprowadzić w ten sposób albo danymi w sesji
