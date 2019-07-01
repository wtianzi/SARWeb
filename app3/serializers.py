from django.contrib.auth.models import User, Group
from .models import GPSData
from rest_framework import serializers

class GPSDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GPSData
        fields = ('deviceid', 'taskid', 'gpsdata')
