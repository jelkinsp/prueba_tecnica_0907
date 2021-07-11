from rest_framework import viewsets

from asteroid.models import Observatory, Device, Asteroid
from asteroid.serializers import ObservatorySerializer, DeviceSerializer, AsteroidSerializer


class ObservatoryViewSet(viewsets.ModelViewSet):
    serializer_class = ObservatorySerializer
    queryset = Observatory.objects.all()

    http_method_names = ["get", "post"]

    # def get_serializer_class(self):
    #     # if self.action == "retrieve":
    #     #     return
    #     return self.serializer_class



class DeviceViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()

    http_method_names = ["get", "post"]

    # def get_serializer_class(self):
    #     # if self.action == "retrieve":
    #     #     return
    #     return self.serializer_class


class AsteroidViewSet(viewsets.ModelViewSet):
    serializer_class = AsteroidSerializer
    queryset = Asteroid.objects.all()

    http_method_names = ["get", "post"]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return
        return self.serializer_class