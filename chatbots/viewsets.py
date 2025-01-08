from rest_framework import viewsets

from .serializers import ChatbotSerializer
from .models import Chatbots

class ChatbotViewSet(viewsets.ModelViewSet):
    serializer_class = ChatbotSerializer
    queryset = Chatbots.objects.all()