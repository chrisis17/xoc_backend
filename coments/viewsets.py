from rest_framework import viewsets

from .serializers import ComentSerializer
from .models import Coments

class ComentViewSet(viewsets.ModelViewSet):
    serializer_class = ComentSerializer
    queryset = Coments.objects.all()