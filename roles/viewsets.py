from rest_framework import viewsets

from .serializers import RoleSerializer
from .models import Roles

class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Roles.objects.all()