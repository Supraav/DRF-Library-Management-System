from rest_framework import serializers
from accounts.models import User
from django.contrib.auth.hashers import make_password


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

#Register
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['Name', 'Email', 'Password']
        extra_kwargs = {'Password': {'write_only': True}}

    def validate(self, data):
        email_exists=User.objects.filter(Email=data['Email']).exists()
        if email_exists:
            raise serializers.ValidationError("Unique emails required. ")
        return data

    def create(self, validated_data):
        validated_data['Password'] = make_password(validated_data['Password'])
        user = User.objects.create(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    Email = serializers.EmailField()
    Password = serializers.CharField(write_only=True)

