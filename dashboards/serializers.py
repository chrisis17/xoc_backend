from rest_framework import serializers

from .models import Dashboards

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboards
        fields = '__all__'