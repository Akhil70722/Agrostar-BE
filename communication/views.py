# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.db import models
# from django.db.models import F, Value
# from django.db.models.functions import Cast
# from .models import DebtCollectionCallHistory

# class CommunicationAPIView(APIView):
#     def get(self, request):
#         partner_id = request.GET.get('partner_id')  # Function-like parameter

#         if not partner_id:
#             return Response({"error": "partner_id is required"}, status=400)

#         calls = DebtCollectionCallHistory.objects.filter(
#             call_id__partner_company_name=partner_id
#         ).annotate(
#             partner=F('call_id__partner_company_name'),
#             conversation_type=Value('AI Call', output_field=models.CharField()),
#             conversation_id=F('call_id_id'),
#             conversation_date=Cast('call_time', output_field=models.DateField()),
#             conversation_data=F('conversation_json'),  # renamed to avoid conflict
#             recording_url=F('recording'),
#             conclusion_text=F('conclusion'),
#         ).values(
#             'partner',
#             'conversation_type',
#             'conversation_id',
#             'conversation_date',
#             'conversation_data',
#             'recording_url',
#             'conclusion_text',
#         )

#         return Response(list(calls))

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import models
from django.db.models import F, Value
from django.db.models.functions import Cast
from .models import DebtCollectionCallHistory

class CommunicationAPIView(APIView):
    def get(self, request):
        partner_id = request.GET.get('partner_id')

        if not partner_id:
            return Response({"error": "partner_id is required"}, status=400)

        calls = DebtCollectionCallHistory.objects.filter(
            call_id__customer_id=partner_id
        ).annotate(
            partner=F('call_id__partner_company_name'),
            conversation_type=Value('AI Call', output_field=models.CharField()),
            conversation_id=F('call_id_id'),
            conversation_date=Cast('call_time', output_field=models.DateField()),
            conversation_data=F('conversation_json'),
            recording_url=F('recording'),
        ).values(
            'partner',
            'conversation_type',
            'conversation_id',
            'conversation_date',
            'conversation_data',
            'recording_url',
            'call_summary_notes',
            'call_duration',
            'conclusion'
        )

        return Response(list(calls))
