from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        Models = User
        fields = ('username', 'email', 'password')
