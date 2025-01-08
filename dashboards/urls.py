from rest_framework.routers import DefaultRouter

from .viewsets import DashboardsViewSet

router = DefaultRouter()
router.register('dashboards', DashboardsViewSet)

urlpatterns = router.urls