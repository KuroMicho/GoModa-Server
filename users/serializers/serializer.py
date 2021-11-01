from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class CustomStorageUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'is_vendor', 'is_staff')

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'last_name', 'email', 'is_vendor', 'is_staff')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user