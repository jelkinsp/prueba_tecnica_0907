from rest_framework.routers import DefaultRouter

from asteroid.views import ObservatoryViewSet, DeviceViewSet, AsteroidViewSet

router = DefaultRouter()
router.register("observatories", ObservatoryViewSet, basename="observatory")
router.register("devices", DeviceViewSet, basename="device")
router.register("asteroids", AsteroidViewSet, basename="asteriod")

urlpatterns = [] + router.urls

app_name = "asteroids"
