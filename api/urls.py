# urls.py

from django.urls import path
from api.views import DonorListCreateView, hello_world,WantListCreateView
from .auth_views import LoginView

app_name = "api"

urlpatterns = [
    path('', hello_world, name="helloworld"),
    path('donors/', DonorListCreateView.as_view(), name='donor-list-create'),
    path('want/', WantListCreateView.as_view(), name='want-blood'),
    path('login/', LoginView.as_view(), name='login'),
]
