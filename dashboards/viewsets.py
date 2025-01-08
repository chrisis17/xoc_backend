from rest_framework import viewsets

from .serializers import DashboardSerializer
from .models import Dashboards

class DashboardsViewSet(viewsets.ModelViewSet):
    serializer_class = DashboardSerializer
    queryset = Dashboards.objects.all()