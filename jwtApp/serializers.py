from .models import User
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email', 'Phone', 'Occupation']
        extra_kwargs = {"password":{'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate_Occupation(self, value):
        value = value.capitalize()
        if value != "Student":
            raise serializers.ValidationError("Occupation must be Student")
        return value

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email', 'Phone', 'Occupation', 'is_superuser']
        extra_kwargs = {"password":{'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate_Occupation(self, value):
        value = value.capitalize()
        if value != "Teacher":
            raise serializers.ValidationError("Occupation must be Teacher")
        return value

    def validate_is_superuser(self, value):
        if value != True:
            raise serializers.ValidationError("Superuser must be True")
        return value