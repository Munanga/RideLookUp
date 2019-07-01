from rest_framework import serializers
from AppAuto import models


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vehicle
        fields = '__all__'
        #fields = ('name', 'model', 'price', 'mileage')





