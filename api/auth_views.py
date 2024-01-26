# auth_views.py

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.views import LoginView as DjangoLoginView
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import Donor
from .serializer import LoginSerializer,DistrictSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.views import LoginView as DjangoLoginView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import Token
from django.contrib.auth.hashers import check_password


# auth_views.py

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import Donor
from .serializer import LoginSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data['phone_no']
        password = serializer.validated_data['password']

        user = Donor.objects.filter(phone_no=phone_number).first()

        if user:
            if user and check_password(password, user.password):
                district_serializer = DistrictSerializer(user.district)
                token_data = TokenObtainPairSerializer.get_token(user)
                response_data = {
                    'status': 'success',
                    'value': 'success',
                    'title': 'Login Successful',
                    'message': 'Logged in successfully.',
                    'token': str(token_data.access_token),
                    'name': user.name,  # Add user information
                    'phone': user.phone_no,
                    'district': district_serializer.data, 
                    'blood_group': user.blood_group,
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                response_data = {
                    'status': 'error',
                    'value': 'error',
                    'title': 'Login Failed',
                    'message': 'Invalid phone number or password.',
                }
                return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
        else:
            print('no user')
