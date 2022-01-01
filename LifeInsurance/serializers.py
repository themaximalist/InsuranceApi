from rest_framework import serializers
from .models import LifeInsurnaceModel


class LifeInsuranceSerializer(serializers.ModelSerializer):
    """
        this is a serializer for "LifeInsuranceView".
        it contains all fields of "LifeInsuranceModel".
        the "age" field must be under 45. if it's not it returns validation error
    """

    class Meta:
        model = LifeInsurnaceModel
        fields = "__all__"

    def validate_age(self, value):
        if value > 45:
            raise serializers.ValidationError("age not valid")
        return value


