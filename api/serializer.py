from .models import Donor,Want,Districts
from rest_framework import serializers,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Districts
        fields = ['id']

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = [
            'id',
            'name',
            'blood_group',
            'phone_no',
            'age',
            'address',
            'has_tattoo',
            'district',
            'password',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

class LoginSerializer(serializers.Serializer):
    phone_no = serializers.CharField()
    password = serializers.CharField(write_only=True)


class WantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Want
        fields = [
            'id',
            'name',
            'age',
            'blood_group',
            'phone_no',
            'no_of_units_here',
            'hospital',
            'district',
        ]
