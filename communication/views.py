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

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.db import models
# from django.db.models import F, Value
# from django.db.models.functions import Cast
# from .models import DebtCollectionCallHistory

# class CommunicationAPIView(APIView):
#     def get(self, request):
#         partner_id = request.GET.get('partner_id')

#         if not partner_id:
#             return Response({"error": "partner_id is required"}, status=400)

#         calls = DebtCollectionCallHistory.objects.filter(
#             customer_id=partner_id
#         ).annotate(
#             partner=F('call_id__partner_company_name'),
#             conversation_type=Value('AI Call', output_field=models.CharField()),
#             conversation_id=F('call_id_id'),
#             conversation_date=Cast('call_time', output_field=models.DateField()),
#             conversation_data=F('conversation_json'),
#             recording_url=F('recording'),
#         ).values(
#             'partner',
#             'conversation_type',
#             'conversation_id',
#             'conversation_date',
#             'conversation_data',
#             'recording_url',
#             'call_summary_notes',
#             'call_duration',
#             'conclusion'
#         )

#         return Response(list(calls))

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
import json

class CommunicationAPIView(APIView):
    def get(self, request):
        partner_id = request.GET.get('partner_id')

        if not partner_id:
            return Response({"error": "partner_id is required"}, status=400)

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    h.id,
                    h.call_id,
                    q.partner_company_name,
                    h.call_time,
                    h.conversation_json,
                    h.recording,
                    h.call_summary_notes,
                    h.call_duration,
                    h.conclusion
                FROM debtcollectioncallhistory h
                LEFT JOIN debtcollectioncallqueue q ON h.call_id = q.call_id
                INNER JOIN (
                    SELECT MAX(id) as latest_id
                    FROM debtcollectioncallhistory
                    WHERE customer_id = %s
                    GROUP BY call_id
                ) latest ON h.id = latest.latest_id
                ORDER BY h.call_time DESC
            """, [partner_id])
            rows = cursor.fetchall()

        result = []
        for row in rows:
            (
                history_id,
                conversation_id,
                partner,
                call_time,
                conversation_json,
                recording,
                call_summary_notes,
                call_duration,
                conclusion
            ) = row

            conversation_date = call_time.date() if call_time else None

            # Parse JSON safely
            try:
                parsed_json = json.loads(conversation_json) if conversation_json else {}
            except Exception:
                parsed_json = {}

            is_empty_json = parsed_json == {}

            # Handle default values for empty json
            if is_empty_json:
                call_summary_notes = "Call Attempted, Customer did not pick up"
                call_duration = 0
                conclusion = "No Response"
                recording_url = None
            else:
                # Extract recording URL from conversation data if present
                recording_url = None
                try:
                    conversation_data = parsed_json.get("conversation", [])
                    for entry in conversation_data:
                        if isinstance(entry, dict) and "url" in entry:
                            recording_url = entry["url"]
                            break
                except Exception:
                    pass

                # Fallback to DB field if no recording found in JSON
                if not recording_url and recording:
                    recording = recording.strip()
                    recording_url = f"/media/{recording}" if not recording.startswith("/media/") else recording

            result.append({
                "partner": partner,
                "conversation_type": "AI Call",
                "conversation_id": conversation_id,
                "conversation_date": conversation_date,
                "conversation_data": parsed_json,
                "recording_url": recording_url,
                "call_summary_notes": call_summary_notes or "",
                "call_duration": call_duration or 0,
                "conclusion": conclusion or ""
            })

        return Response(result)
