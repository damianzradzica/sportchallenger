from rest_framework import serializers
from sportchallenger.models import Reservation, SportFacility


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SportFacility
        fields = ['name', 'kind', 'city', 'price']


