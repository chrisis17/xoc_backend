from rest_framework.routers import DefaultRouter

from .viewsets import ChatbotViewSet

router = DefaultRouter()
router.register('chatbots', ChatbotViewSet)

urlpatterns = router.urls