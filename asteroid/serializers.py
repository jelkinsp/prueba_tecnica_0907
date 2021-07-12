from rest_framework import serializers
from rest_framework.utils import json

from asteroid.mixins import StringErrorsMixin
from asteroid.models import Sighting


class SightingSerializer(StringErrorsMixin, serializers.ModelSerializer):
    class Meta:
        model = Sighting
        fields = "__all__"


class SightingListSerializer(StringErrorsMixin, serializers.ModelSerializer):
    sightings = serializers.SerializerMethodField(allow_null=True, read_only=True)

    class Meta:
        model = Sighting
        fields = ("sightings",)

    def get_sightings(self, obj):
        return Sighting.objects.filter(device_matrix_clear=obj.device_matrix_clear).values("id", "device_matrix",
                                                                                           "date", "time",
                                                                                           "observatory_code")
