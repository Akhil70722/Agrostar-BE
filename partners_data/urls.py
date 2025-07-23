# from django.urls import path
# from .views import PartnersDataAPIView, PartnerAttemptDetailsAPIView

# urlpatterns = [
#     path('partners-data/', PartnersDataAPIView.as_view(), name='partners-data'),
#     path('partners-attempts/<str:partner_name>/', PartnerAttemptDetailsAPIView.as_view(), name='partner-attempt-details'),
# ]


from django.urls import path
from .views import PartnersDataAPIView, PartnerAttemptDetailsAPIView, TotalPartnerEngagementAPIView

urlpatterns = [
    path('partners-data/', PartnersDataAPIView.as_view(), name='partners-data'),
    path('partners-attempts/<str:partner_id>/', PartnerAttemptDetailsAPIView.as_view(), name='partner_attempt_details'),
    path('total-partner-engagement/', TotalPartnerEngagementAPIView.as_view(), name='total_partner_engagement'),
]

