# views.py
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Donor,Want
from rest_framework.serializers import Serializer
from .serializer import DonorSerializer,WantSerializer
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from geopy.distance import geodesic
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Donor, Want
from .serializer import DonorSerializer, WantSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Donor, Want
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from .models import Donor, Want, Hospitals, Districts
from .serializer import WantSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from geopy.distance import geodesic
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Donor, Want, Hospitals
    
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Donor, Want, Hospitals, Districts
from .serializer import WantSerializer

def hello_world(request):
    return HttpResponse("Hello world")


class DonorListCreateView(generics.ListCreateAPIView):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer

    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['phone_no']
        password = request.data.get('password')  

        existing_user = Donor.objects.filter(phone_no=username).first()

        if existing_user:
            response_data = {
                "status": "error",
                "value": "error",
                'title': "Already Registered",
                "message": "A user with this phone number is already registered.",
                'redirect': 'already_registered/'
            }
        else:
            serializer.save()
            user = Donor.objects.get(phone_no=username)
            user.set_password(password)  
            user.save()
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            response_data = {
                "status": "info",
                "value": "success",
                'title': "Registration Successful",
                "message": "User registered successfully.",
                'access_token': access_token,
            }

        return Response(response_data, status=status.HTTP_201_CREATED)
    
class WantListCreateView(generics.ListCreateAPIView):
    queryset = Want.objects.all()
    serializer_class = WantSerializer

