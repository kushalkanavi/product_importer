from rest_framework import serializers
from .models import productdetails


class productDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = productdetails
        fields = '__all__'
