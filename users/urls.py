from rest_framework.routers import DefaultRouter

from .viewsets import UserViewSet, SessionViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('session', SessionViewSet)

urlpatterns = router.urls
