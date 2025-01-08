from rest_framework.routers import DefaultRouter

from .viewsets import RoleViewSet

router = DefaultRouter()
router.register('roles', RoleViewSet)

urlpatterns = router.urls
