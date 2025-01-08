from rest_framework.routers import DefaultRouter

from .viewsets import ComentViewSet

router = DefaultRouter()
router.register('coments', ComentViewSet)

urlpatterns = router.urls