from django.contrib import admin
from sportchallenger.models import MyUser, SportFacility, Reservation

# Register your models here.



@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo']

@admin.register(SportFacility)
class SportFacilityAdmin(admin.ModelAdmin):
    list_display = ['name', 'photos', 'kind', 'city', 'street', 'sports', 'rating', 'price']

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['facility', 'user', 'creation_date', 'reservation_date']




