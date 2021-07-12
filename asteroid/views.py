from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from asteroid.models import Sighting
from asteroid.serializers import SightingSerializer, SightingListSerializer


class SightingViewSet(viewsets.ModelViewSet):
    serializer_class = SightingSerializer
    queryset = Sighting.objects.all()
    http_method_names = ['get']

    @action(detail=True, methods=["get"], url_path="search_sighting")
    def get_sighting(self, request, pk=None):
        sighting = self.get_object()

        sighting_serializer = SightingListSerializer(sighting)
        return Response(sighting_serializer.data, status=status.HTTP_200_OK)
