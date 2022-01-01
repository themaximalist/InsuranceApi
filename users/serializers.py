
from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.password_validation import validate_password


class CustomUserSerializer(serializers.ModelSerializer):
    """
        this class used for serialize data from registration endpoint.
        username, password and phoneNumber are required.
        phoneNumber must be a valid phoneNumber.
    """
    class Meta:
        model = User
        fields = ('username', 'phoneNumber', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)

        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.

    """
    old_password = serializers.CharField(required=True, )
    password = serializers.CharField(required=True, )
    password2 = serializers.CharField(required=True, )

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('new passwords does not match')
        return attrs


