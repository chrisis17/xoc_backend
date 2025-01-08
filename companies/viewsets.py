from rest_framework import viewsets

from .serializers import CompanySerializer
from .models import Companies

class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Companies.objects.all()