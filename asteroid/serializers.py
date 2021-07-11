from rest_framework import serializers

from asteroid.mixins import StringErrorsMixin
from asteroid.models import Observatory, Device, Asteroid


class ObservatorySerializer(StringErrorsMixin, serializers.ModelSerializer):
    class Meta:
        model = Observatory
        fields = "__all__"


class DeviceSerializer(StringErrorsMixin, serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"


class AsteroidSerializer(StringErrorsMixin, serializers.ModelSerializer):
    class Meta:
        model = Asteroid
        fields = "__all__"
