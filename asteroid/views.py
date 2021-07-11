from rest_framework import viewsets

from asteroid.models import Sighting
from asteroid.serializers import SightingSerializer


class SightingViewSet(viewsets.ModelViewSet):
    serializer_class = SightingSerializer
    queryset = Sighting.objects.all()

    http_method_names = ["get", "post"]
