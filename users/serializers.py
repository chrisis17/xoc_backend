from rest_framework import serializers

from .models import Users, Session

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['user', 'password']