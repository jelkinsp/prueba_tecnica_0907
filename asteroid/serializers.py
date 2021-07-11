from rest_framework import serializers

from asteroid.mixins import StringErrorsMixin
from asteroid.models import Sighting


class SightingSerializer(StringErrorsMixin, serializers.ModelSerializer):
    class Meta:
        model = Sighting
        fields = "__all__"
