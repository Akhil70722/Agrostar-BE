from django.urls import path, include 
from .views import DashboardAPI, CardsAPI,PartnersDataAPIView, PartnerAttemptDetailsAPIView, TotalPartnerEngagementAPIView, CommunicationAPIView

urlpatterns = [
     path("engagement/", DashboardAPI.as_view(), name="engagement_api"),
     path('queue-history/', CardsAPI.as_view(), name='queue-history'),
     path('partners-data/', PartnersDataAPIView.as_view(), name='partners-data'),
     path("partner-attempts/<str:partner_id>/", PartnerAttemptDetailsAPIView.as_view(), name="partner_attempt_details"),
     path('total-partner-engagement/', TotalPartnerEngagementAPIView.as_view(), name='total_partner_engagement'),
     path('communication/', CommunicationAPIView.as_view(), name='communication_api'),
]

