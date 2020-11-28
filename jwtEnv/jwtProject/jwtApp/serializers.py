from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'is_superuser', 'is_staff', 'is_active', 'email', 'password']

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User