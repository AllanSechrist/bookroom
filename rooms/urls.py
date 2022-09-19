from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import RoomViewSet

router = SimpleRouter()
router.register("", RoomViewSet, basename="rooms")

urlpatterns = router.urls
