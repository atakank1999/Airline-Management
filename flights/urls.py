from rest_framework.routers import DefaultRouter
from .views import FlightViewSet

router = DefaultRouter()
router.register(r'', FlightViewSet)

urlpatterns = router.urls
