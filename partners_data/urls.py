from django.urls import path
from .views import PartnersDataAPIView

urlpatterns = [
    path('partners-data/', PartnersDataAPIView.as_view(), name='partners-data'),
]
