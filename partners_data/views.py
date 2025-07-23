# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.db.models import Count, Max, Sum
# from .models import DebtCollectionCallQueue, DebtCollectionCallHistory

# class PartnersDataAPIView(APIView):
#     def get(self, request):
#         show_connected = request.GET.get("connected") == "true"

#         queryset = DebtCollectionCallQueue.objects.all()
#         if show_connected:
#             queryset = queryset.exclude(customer_id__isnull=True).exclude(customer_id="")

#         data = (
#             queryset.values("customer_id", "customer_name")
#             .annotate(
#                 no_of_attempts=Count("call_id"),
#                 ocp=Max("ocp"),
#                 overdue_amount=sum("invoice_overdue"),
#                 cd_valid_till=Max("cd_valid_till"),
#                 cd_amount=Sum("cd_amount"),              
#                 total_cd_amount=Sum("total_cd_amount"),  
#             )
#         )

#         history = (
#             DebtCollectionCallHistory.objects.values("call_id__customer_id")
#             .annotate(
#                 latest_promise_date=Max("promise_date"),
#                 latest_promise_amount=Max("promise_amount"),
#             )
#         )

#         history_map = {
#             h["call_id__customer_id"]: {
#                 "promise_date": h["latest_promise_date"],
#                 "promise_amount": h["latest_promise_amount"]
#             }
#             for h in history
#         }

#         result = []
#         for item in data:
#             customer_id = item["customer_id"]
#             hist = history_map.get(customer_id, {})

#             result.append({
#                 "partner_id": customer_id,
#                 "partner_name": item["customer_name"],
#                 "no_of_attempts": item["no_of_attempts"],
#                 "ocp": float(item["ocp"] or 0),
#                 "overdue_amount": float(item["overdue_amount"] or 0),
#                 "cd_valid_till": item["cd_valid_till"],
#                 "cd_amount": float(item["cd_amount"] or 0),
#                 "total_cd_amount": float(item["total_cd_amount"] or 0),
#                 "promise_date": hist.get("promise_date"),
#                 "promise_amount": float(hist.get("promise_amount") or 0),
#             })

#         return Response({"data": result})



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.db.models import Count, Max, Sum
# from .models import DebtCollectionCallQueue, DebtCollectionCallHistory

# class PartnersDataAPIView(APIView):
#     def get(self, request):
#         # Check if user wants only connected partners
#         show_connected = request.GET.get("connected") == "true"

#         # Get base queryset
#         queryset = DebtCollectionCallQueue.objects.all()
#         if show_connected:
#             queryset = queryset.exclude(customer_id__isnull=True).exclude(customer_id="")

#         # Aggregate partner data
#         data = (
#             queryset.values("customer_id", "customer_name")
#             .annotate(
#                 no_of_attempts=Count("call_id"),
#                 ocp=Max("ocp"),
#                 overdue_amount=Sum("invoice_overdue"),  # ✅ FIXED
#                 cd_valid_till=Max("cd_valid_till"),
#                 cd_amount=Sum("cd_amount"),
#                 total_cd_amount=Sum("total_cd_amount"),
#             )
#         )

#         # Fetch latest promise date and amount from call history
#         history = (
#             DebtCollectionCallHistory.objects.values("call_id__customer_id")
#             .annotate(
#                 latest_promise_date=Max("promise_date"),
#                 latest_promise_amount=Max("promise_amount"),
#             )
#         )

#         # Map history by customer_id
#         history_map = {
#             h["call_id__customer_id"]: {
#                 "promise_date": h["latest_promise_date"],
#                 "promise_amount": h["latest_promise_amount"]
#             }
#             for h in history
#         }

#         # Final result formatting
#         result = []
#         for item in data:
#             customer_id = item["customer_id"]
#             hist = history_map.get(customer_id, {})

#             result.append({
#                 "partner_id": customer_id,
#                 "partner_name": item["customer_name"],
#                 "no_of_attempts": item["no_of_attempts"],
#                 "ocp": float(item["ocp"] or 0),
#                 "overdue_amount": float(item["overdue_amount"] or 0),
#                 "cd_valid_till": item["cd_valid_till"],
#                 "cd_amount": float(item["cd_amount"] or 0),
#                 "total_cd_amount": float(item["total_cd_amount"] or 0),
#                 "promise_date": hist.get("promise_date"),
#                 "promise_amount": float(hist.get("promise_amount") or 0),
#             })

#         return Response({"data": result})



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.db.models import Count, Max, Sum
# from .models import DebtCollectionCallQueue, DebtCollectionCallHistory


# class PartnersDataAPIView(APIView):
#     def get(self, request):
#         # Query parameter to filter connected partners only
#         show_connected = request.GET.get("connected") == "true"

#         # Filter DebtCollectionCallQueue accordingly
#         queue_qs = DebtCollectionCallQueue.objects.all()
#         if show_connected:
#             queue_qs = queue_qs.exclude(customer_id__isnull=True).exclude(customer_id="")

#         # Partner aggregated data
#         partner_data = (
#             queue_qs.values("customer_id", "customer_name")
#             .annotate(
#                 no_of_attempts=Count("call_id"),
#                 ocp=Max("ocp"),
#                 overdue_amount=Sum("invoice_overdue"),
#                 cd_valid_till=Max("cd_valid_till"),
#                 cd_amount=Sum("cd_amount"),
#                 total_cd_amount=Sum("total_cd_amount"),
#             )
#         )

#         # Get promise data from latest call history grouped by customer_id
#         history_data = (
#             DebtCollectionCallHistory.objects.values("call_id__customer_id")
#             .annotate(
#                 latest_promise_date=Max("promise_date"),
#                 latest_promise_amount=Max("promise_amount"),
#             )
#         )

#         # Map customer_id to promise data
#         history_map = {
#             h["call_id__customer_id"]: {
#                 "promise_date": h["latest_promise_date"],
#                 "promise_amount": float(h["latest_promise_amount"] or 0)
#             }
#             for h in history_data
#         }

#         # Build final response
#         response_data = []
#         for item in partner_data:
#             cust_id = item["customer_id"]
#             promise_info = history_map.get(cust_id, {})

#             response_data.append({
#                 "partner_id": cust_id,
#                 "partner_name": item["customer_name"],
#                 "no_of_attempts": item["no_of_attempts"],
#                 "ocp": float(item["ocp"] or 0),
#                 "overdue_amount": float(item["overdue_amount"] or 0),
#                 "cd_valid_till": item["cd_valid_till"],
#                 "cd_amount": float(item["cd_amount"] or 0),
#                 "total_cd_amount": float(item["total_cd_amount"] or 0),
#                 "promise_date": promise_info.get("promise_date"),
#                 "promise_amount": promise_info.get("promise_amount", 0)
#             })

#         return Response({"data": response_data})

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.db.models import Count, Max, Sum
# from .models import DebtCollectionCallQueue, DebtCollectionCallHistory

# class PartnersDataAPIView(APIView):
#     def get(self, request):
#         connected_param = request.GET.get("connected", "").strip().lower()
#         filter_connected = connected_param == "true"

#         # Base queryset with filtering if needed
#         queue_qs = DebtCollectionCallQueue.objects.all()

#         if filter_connected:
#             queue_qs = queue_qs.exclude(customer_id__isnull=True).exclude(customer_id="")

#         # Remove rows without customer_id early
#         queue_qs = queue_qs.exclude(customer_id__isnull=True).exclude(customer_id="")

#         # Aggregate queue data by customer_id and customer_name
#         partner_data = list(
#             queue_qs.values("customer_id", "customer_name")
#             .annotate(
#                 no_of_attempts=Count("call_id"),
#                 ocp=Max("ocp"),
#                 overdue_amount=Sum("invoice_overdue"),
#                 cd_valid_till=Max("cd_valid_till"),
#                 cd_amount=Sum("cd_amount"),
#                 total_cd_amount=Sum("total_cd_amount"),
#             )
#         )

#         # Extract customer_ids
#         customer_ids = [entry["customer_id"] for entry in partner_data]

#         # Get latest history data per customer_id
#         history_agg = (
#             DebtCollectionCallHistory.objects
#             .filter(call_id__customer_id__in=customer_ids)
#             .values("call_id__customer_id")
#             .annotate(
#                 promise_date=Max("promise_date"),
#                 promise_amount=Max("promise_amount")
#             )
#         )

#         # Map customer_id to history data
#         history_map = {
#             h["call_id__customer_id"]: {
#                 "promise_date": h["promise_date"],
#                 "promise_amount": float(h["promise_amount"] or 0)
#             }
#             for h in history_agg
#         }

#         # Final combined response
#         response_data = []
#         for item in partner_data:
#             customer_id = item["customer_id"]
#             history = history_map.get(customer_id, {})
#             response_data.append({
#                 "partner_id": customer_id,
#                 "partner_name": item["customer_name"],
#                 "no_of_attempts": item["no_of_attempts"],
#                 "ocp": float(item["ocp"] or 0),
#                 "overdue_amount": float(item["overdue_amount"] or 0),
#                 "cd_valid_till": item["cd_valid_till"],
#                 "cd_amount": float(item["cd_amount"] or 0),
#                 "total_cd_amount": float(item["total_cd_amount"] or 0),
#                 "promise_date": history.get("promise_date"),
#                 "promise_amount": history.get("promise_amount", 0)
#             })

#         return Response({"data": response_data})


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.db.models import Count, Max, Sum
# from .models import DebtCollectionCallQueue, DebtCollectionCallHistory

# class PartnersDataAPIView(APIView):
#     def get(self, request):
#         connected_param = request.GET.get("connected", "").strip().lower()
#         apply_connected_filter = connected_param in ["true", "false"]

#         # Base queryset
#         queue_qs = DebtCollectionCallQueue.objects.all()

#         # Apply call_connected filter based on query param
#         if apply_connected_filter:
#             if connected_param == "true":
#                 queue_qs = queue_qs.filter(call_connected=True)
#             else:
#                 queue_qs = queue_qs.filter(call_connected=False)

#         # Apply partner_id filter
#         partner_id = request.GET.get("partner_id")
#         if partner_id:
#             queue_qs = queue_qs.filter(customer_id=partner_id)

#         # Apply from_date and to_date filter on call_date
#         from_date = request.GET.get("from_date")
#         to_date = request.GET.get("to_date")
#         if from_date and to_date:
#             queue_qs = queue_qs.filter(call_date__range=[from_date, to_date])
#         elif from_date:
#             queue_qs = queue_qs.filter(call_date__gte=from_date)
#         elif to_date:
#             queue_qs = queue_qs.filter(call_date__lte=to_date)

#         # Filter out rows without valid customer_id (for aggregation)
#         filtered_qs = queue_qs.exclude(customer_id__isnull=True).exclude(customer_id="")

#         # Aggregate queue data
#         partner_data = list(
#             filtered_qs.values("customer_id", "customer_name")
#             .annotate(
#                 no_of_attempts=Max("call_tried"),
#                 ocp=Max("ocp"),
#                 overdue_amount=Max("total_outstanding"),
#                 cd_valid_till=Max("cd_valid_till"),
#                 cd_amount=Sum("cd_amount"),
#                 total_cd_amount=Sum("total_cd_amount"),
#             )
#         )

#         # Extract customer_ids
#         customer_ids = [entry["customer_id"] for entry in partner_data]

#         # Fetch latest history data per customer_id
#         history_agg = (
#             DebtCollectionCallHistory.objects
#             .filter(call_id__customer_id__in=customer_ids)
#             .values("call_id__customer_id")
#             .annotate(
#                 promise_date=Max("promise_date"),
#                 promise_amount=Max("promise_amount")
#             )
#         )

#         # Map history to customer_id
#         history_map = {
#             h["call_id__customer_id"]: {
#                 "promise_date": h["promise_date"],
#                 "promise_amount": float(h["promise_amount"] or 0)
#             }
#             for h in history_agg
#         }

#         # Final response
#         response_data = []
#         for item in partner_data:
#             customer_id = item["customer_id"]
#             history = history_map.get(customer_id, {})
#             response_data.append({
#                 "partner_id": customer_id,
#                 "partner_name": item["customer_name"],
#                 "no_of_attempts": item["no_of_attempts"],
#                 "ocp": float(item["ocp"] or 0),
#                 "overdue_amount": float(item["overdue_amount"] or 0),
#                 "cd_valid_till": item["cd_valid_till"],
#                 "cd_amount": float(item["cd_amount"] or 0),
#                 "total_cd_amount": float(item["total_cd_amount"] or 0),
#                 "promise_date": history.get("promise_date"),
#                 "promise_amount": history.get("promise_amount", 0)
#             })

#         return Response({"data": response_data})


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.db.models import Count, Max, Sum
# from collections import defaultdict
# from .models import DebtCollectionCallQueue, DebtCollectionCallHistory
# from django.db import connection
# from django.http import JsonResponse


# # =======================
# # 1. Main Partner Summary API
# # =======================
# class PartnersDataAPIView(APIView):
#     def get(self, request):
#         connected_param = request.GET.get("connected", "").strip().lower()
#         apply_connected_filter = connected_param in ["true", "false"]

#         # Base queryset
#         queue_qs = DebtCollectionCallQueue.objects.all()

#         # Apply call_connected filter
#         if apply_connected_filter:
#             queue_qs = queue_qs.filter(call_connected=(connected_param == "true"))

#         # Apply partner_id filter
#         partner_id = request.GET.get("partner_id")
#         if partner_id:
#             queue_qs = queue_qs.filter(customer_id=partner_id)

#         # Apply date filters
#         from_date = request.GET.get("from_date")
#         to_date = request.GET.get("to_date")
#         if from_date and to_date:
#             queue_qs = queue_qs.filter(call_date__range=[from_date, to_date])
#         elif from_date:
#             queue_qs = queue_qs.filter(call_date__gte=from_date)
#         elif to_date:
#             queue_qs = queue_qs.filter(call_date__lte=to_date)

#         # Filter invalid customer_ids
#         filtered_qs = queue_qs.exclude(customer_id__isnull=True).exclude(customer_id="")

#         # Aggregate queue data
#         partner_data = list(
#             filtered_qs.values("customer_id", "customer_name")
#             .annotate(
#                 no_of_attempts=Max("call_tried"),
#                 ocp=Max("ocp"),
#                 total_outstanding=Max("total_outstanding"),
#                 cd_valid_till=Max("cd_valid_till"),
#                 cd_amount=Sum("cd_amount"),
#                 total_cd_amount=Sum("total_cd_amount"),
#             )
#         )

#         # Get customer_ids
#         customer_ids = [entry["customer_id"] for entry in partner_data]

#         # Latest call history per partner
#         history_agg = (
#             DebtCollectionCallHistory.objects
#             .filter(call_id__customer_id__in=customer_ids)
#             .values("call_id__customer_id")
#             .annotate(
#                 promise_date=Max("promise_date"),
#                 promise_amount=Max("promise_amount")
#             )
#         )

#         history_map = {
#             h["call_id__customer_id"]: {
#                 "promise_date": h["promise_date"],
#                 "promise_amount": float(h["promise_amount"] or 0)
#             }
#             for h in history_agg
#         }

#         # Product list per customer
#         product_qs = filtered_qs.values("customer_id", "product").exclude(product__isnull=True).exclude(product="")
#         customer_products = defaultdict(set)
#         for entry in product_qs:
#             customer_products[entry["customer_id"]].add(entry["product"])

#         # Final response
#         response_data = []
#         for item in partner_data:
#             customer_id = item["customer_id"]
#             history = history_map.get(customer_id, {})
#             products = customer_products.get(customer_id, set())

#             response_data.append({
#                 "customer_id": customer_id,
#                 "customer_name": item["customer_name"],
#                 "no_of_attempts": item["no_of_attempts"],
#                 "ocp": float(item["ocp"] or 0),
#                 "total_outstanding": float(item["total_outstanding"] or 0),
#                 "cd_valid_till": item["cd_valid_till"],
#                 "cd_amount": float(item["cd_amount"] or 0),
#                 "total_cd_amount": float(item["total_cd_amount"] or 0),
#                 "promise_date": history.get("promise_date"),
#                 "promise_amount": history.get("promise_amount", 0),
#                 "product_count": len(products),
#             })

#         return Response({"data": response_data})




# # =======================
# # 2. Product-wise Attempts API
# # =======================
# class PartnerAttemptsAPIView(APIView):
#     def get(self, request):
#         with connection.cursor() as cursor:
#             query = """
#                 SELECT 
#                     partner_company_name,
#                     COUNT(*) as total_attempts
#                 FROM dashboard_debtcollectioncallhistory
#                 WHERE partner_company_name IS NOT NULL
#                 GROUP BY partner_company_name
#                 ORDER BY total_attempts DESC;
#             """
#             cursor.execute(query)
#             data = cursor.fetchall()
#             response = [
#                 {"partner_company_name": row[0], "total_attempts": row[1]}
#                 for row in data
#             ]
#             return Response(response)


# class PartnerAttemptDetailsAPIView(APIView):
#     def get(self, request, partner_name):
#         with connection.cursor() as cursor:
#             query = """
#                 SELECT 
#                     call_id,
#                     phone_number,
#                     customer_name,
#                     customer_id,
#                     attempt_number,
#                     created_at,
#                     conclusion
#                 FROM dashboard_debtcollectioncallhistory
#                 WHERE partner_company_name = %s
#                 ORDER BY attempt_number ASC;
#             """
#             cursor.execute(query, [partner_name])
#             data = cursor.fetchall()

#             response = [
#                 {
#                     "call_id": row[0],
#                     "phone_number": row[1],
#                     "customer_name": row[2],
#                     "customer_id": row[3],
#                     "attempt_number": row[4],
#                     "created_at": row[5],
#                     "conclusion": row[6]
#                 }
#                 for row in data
#             ]
#             return Response(response)



from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Max, Sum
from collections import defaultdict
from .models import DebtCollectionCallQueue, DebtCollectionCallHistory
from django.db import connection
from django.http import JsonResponse
from rest_framework import status

# =======================
# 1. Main Partner Summary API
# =======================
class PartnersDataAPIView(APIView):
    def get(self, request):
        connected_param = request.GET.get("connected", "").strip().lower()
        apply_connected_filter = connected_param in ["true", "false"]

        # Base queryset
        queue_qs = DebtCollectionCallQueue.objects.all()

        # Apply call_connected filter
        if apply_connected_filter:
            queue_qs = queue_qs.filter(call_connected=(connected_param == "true"))

        # Apply partner_id filter
        partner_id = request.GET.get("partner_id")
        if partner_id:
            queue_qs = queue_qs.filter(customer_id=partner_id)

        # Apply date filters
        from_date = request.GET.get("from_date")
        to_date = request.GET.get("to_date")
        if from_date and to_date:
            queue_qs = queue_qs.filter(call_date__range=[from_date, to_date])
        elif from_date:
            queue_qs = queue_qs.filter(call_date__gte=from_date)
        elif to_date:
            queue_qs = queue_qs.filter(call_date__lte=to_date)

        # Filter invalid customer_ids
        filtered_qs = queue_qs.exclude(customer_id__isnull=True).exclude(customer_id="")

        # Aggregate queue data
        partner_data = list(
            filtered_qs.values("customer_id", "customer_name")
            .annotate(
                no_of_attempts=Max("call_tried"),
                ocp=Max("ocp"),
                total_outstanding=Max("total_outstanding"),
                cd_valid_till=Max("cd_valid_till"),
                cd_amount=Sum("cd_amount"),
                total_cd_amount=Sum("total_cd_amount"),
            )
        )

        # Get customer_ids
        customer_ids = [entry["customer_id"] for entry in partner_data]

        # Latest call history per partner
        history_agg = (
            DebtCollectionCallHistory.objects
            .filter(call_id__customer_id__in=customer_ids)
            .values("call_id__customer_id")
            .annotate(
                promise_date=Max("promise_date"),
                promise_amount=Max("promise_amount")
            )
        )

        history_map = {
            h["call_id__customer_id"]: {
                "promise_date": h["promise_date"],
                "promise_amount": float(h["promise_amount"] or 0)
            }
            for h in history_agg
        }

        # Product list per customer
        product_qs = filtered_qs.values("customer_id", "product").exclude(product__isnull=True).exclude(product="")
        customer_products = defaultdict(set)
        for entry in product_qs:
            customer_products[entry["customer_id"]].add(entry["product"])

        # Final response
        response_data = []
        for item in partner_data:
            customer_id = item["customer_id"]
            history = history_map.get(customer_id, {})
            products = customer_products.get(customer_id, set())

            response_data.append({
                "customer_id": customer_id,
                "customer_name": item["customer_name"],
                "no_of_attempts": item["no_of_attempts"],
                "ocp": float(item["ocp"] or 0),
                "total_outstanding": float(item["total_outstanding"] or 0),
                "cd_valid_till": item["cd_valid_till"],
                "cd_amount": float(item["cd_amount"] or 0),
                "total_cd_amount": float(item["total_cd_amount"] or 0),
                "promise_date": history.get("promise_date"),
                "promise_amount": history.get("promise_amount", 0),
                "product_count": len(products),
            })

        return Response({"data": response_data})


# =======================
# 2. Product-wise Attempts Summary API (Grouped by Partner ID)
# =======================
class PartnerAttemptDetailsAPIView(APIView):
    def get(self, request, partner_id):
        records = DebtCollectionCallHistory.objects.filter(customer_id=partner_id).order_by("call_time")

        if not records.exists():
            return Response({"detail": "No call attempts found for this partner ID."}, status=status.HTTP_404_NOT_FOUND)

        response = []
        for idx, r in enumerate(records):
            call_id_value = None

            # Safely fetch first matching DebtCollectionCallQueue (in case of duplicates)
            if r.call_id_id:  # Use the _id to avoid triggering unnecessary object fetch
                queue_obj = DebtCollectionCallQueue.objects.filter(call_id=r.call_id_id).first()
                if queue_obj:
                    call_id_value = queue_obj.call_id

            response.append({
                "call_id": call_id_value,
                "phone_number": r.phone_number,
                "customer_name": r.customer_name,
                "partner_id": r.customer_id,
                "attempt_number": idx + 1,
                "created_at": r.call_time,
                "conclusion": r.conclusion,
            })

        return Response(response, status=status.HTTP_200_OK)


# =======================
# 3. Total Partners Engangament
# =======================
class TotalPartnerEngagementAPIView(APIView):
    def get(self, request):
        connected_calls = DebtCollectionCallQueue.objects.filter(call_connected=True).count()
        not_connected_calls = DebtCollectionCallQueue.objects.filter(call_connected=False).count()
        ai_calls = DebtCollectionCallQueue.objects.filter(partner_company_name__icontains='ai').count()

        total_partner_engagement = connected_calls + not_connected_calls + ai_calls

        return Response({"total_partner_engagement": total_partner_engagement})

