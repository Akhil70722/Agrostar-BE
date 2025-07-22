# dashboard_api/urls.py
from django.urls import path
from .views import EngagementAPIView

urlpatterns = [
     path("engagement/", EngagementAPIView.as_view(), name="engagement_api")
     #  path('dashboard_api/', EngagementAPIView.as_view()),
]
