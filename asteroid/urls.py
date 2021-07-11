from rest_framework.routers import DefaultRouter

from asteroid.views import SightingViewSet

router = DefaultRouter()
router.register("sightings", SightingViewSet, basename="sighting")

urlpatterns = [] + router.urls

app_name = "asteroids"
