from rest_framework.routers import DefaultRouter
from .views import AirplaneViewSet

router = DefaultRouter()
router.register(r'', AirplaneViewSet)

urlpatterns = router.urls
