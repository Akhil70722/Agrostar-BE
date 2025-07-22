# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import (
#     FlatDebtCollectionQueueView,
#     DebtCollectionCallHistoryViewSet,
# )

# router = DefaultRouter()
# router.register(r'history', DebtCollectionCallHistoryViewSet, basename='history')

# urlpatterns = [
#     path('', include(router.urls)),
#     path('flat-data/', FlatDebtCollectionQueueView.as_view(), name='flat-data'),
# ]


# from django.urls import path
# from .views import FlatDebtCollectionAPIView

# urlpatterns = [
#     path('flat-data/', FlatDebtCollectionAPIView.as_view(), name='flat-data'),
# ]

# urls.py

# from django.urls import path
# from .views import FlatDebtCollectionAPIView

# urlpatterns = [
#     path('flat-data/', FlatDebtCollectionAPIView.as_view(), name='flat-data'),
# ]


# urls.py

# from django.urls import path
# from .views import DebtCollectionCallView, DebtCollectionCallHistoryView

# urlpatterns = [
#     path('queue/', DebtCollectionCallView.as_view()),
#     path('history/', DebtCollectionCallHistoryView.as_view()),
# ]

# from django.urls import path
# from .views import (
#     DebtCollectionCallView,
#     DebtCollectionCallHistoryView,
#     MappedDebtCollectionView,
# )

# urlpatterns = [
#     path('queue/', DebtCollectionCallView.as_view()),
#     path('history/', DebtCollectionCallHistoryView.as_view()),
#     path('mapped/', MappedDebtCollectionView.as_view()),
# ]

from django.urls import path
from .views import QueueHistoryAPIView
from django.urls import path, include 

urlpatterns = [
    path('queue-history/', QueueHistoryAPIView.as_view(), name='queue-history'),
]
