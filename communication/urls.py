from django.urls import path
from .views import CommunicationAPIView

urlpatterns = [
    path('communication/', CommunicationAPIView.as_view(), name='communication_api'),
]
