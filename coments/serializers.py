from rest_framework import serializers

from .models import Coments

class ComentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coments
        fields = '__all__'