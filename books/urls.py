from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import BookViewSet

router = SimpleRouter()
router.register("", BookViewSet, basename="books")

urlpatterns = router.urls


