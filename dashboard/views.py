# from rest_framework import viewsets
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import DebtCollectionCallQueue, DebtCollectionCallHistory
# from .serializers import DebtCollectionCallQueueSerializer, DebtCollectionCallHistorySerializer


# class FlatDebtCollectionQueueView(APIView):
#     def get(self, request):
#         queue_queryset = DebtCollectionCallQueue.objects.all()
#         history_queryset = DebtCollectionCallHistory.objects.all()

#         # Map history records by phone number
#         history_map = {}
#         for history in history_queryset:
#             key = history.phone_number  # You can change this key if needed
#             if key not in history_map:
#                 history_map[key] = []
#             history_map[key].append(DebtCollectionCallHistorySerializer(history).data)

#         # Prepare response: one flat object per queue record
#         response = []
#         for queue in queue_queryset:
#             queue_data = DebtCollectionCallQueueSerializer(queue).data
#             phone = queue.phone_number
#             queue_data["call_history"] = history_map.get(phone, [])
#             response.append(queue_data)

#         return Response(response)


# class DebtCollectionCallQueueViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = DebtCollectionCallQueue.objects.all()
#     serializer_class = DebtCollectionCallQueueSerializer


# class DebtCollectionCallHistoryViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = DebtCollectionCallHistory.objects.all()
#     serializer_class = DebtCollectionCallHistorySerializer



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import DebtCollectionCallQueue
# from .serializers import FlatDebtCollectionSerializer

# class FlatDebtCollectionAPIView(APIView):
#     def get(self, request):
#         queues = DebtCollectionCallQueue.objects.all().select_related('debtcollectioncallhistory')
#         serializer = FlatDebtCollectionSerializer(queues, many=True)
#         return Response(serializer.data)


# views.py

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import DebtCollectionCallQueue, DebtCollectionCallHistory
# from .serializers import FlatDebtCollectionSerializer
# from django.db.models import OuterRef, Subquery

# class FlatDebtCollectionAPIView(APIView):
#     def get(self, request):
#         # Subquery to get only ONE matching history per call_id
#         history_subquery = DebtCollectionCallHistory.objects.filter(
#             call_id=OuterRef('call_id')
#         ).order_by('id')  # or latest with '-id'

#         # Annotate queue records with a related history instance
#         queues = DebtCollectionCallQueue.objects.annotate(
#             history_id=Subquery(history_subquery.values('id')[:1])
#         ).select_related()

#         # Prefetch the related DebtCollectionCallHistory objects using the annotated ID
#         history_map = {
#             h.id: h for h in DebtCollectionCallHistory.objects.filter(
#                 id__in=[q.history_id for q in queues if q.history_id]
#             )
#         }

#         for q in queues:
#             q.history = history_map.get(q.history_id)

#         # Group by call_id by using distinct call_id (you can also use .distinct('call_id') on Postgres)
#         seen = set()
#         unique_queues = []
#         for q in queues:
#             if q.call_id not in seen:
#                 seen.add(q.call_id)
#                 unique_queues.append(q)

#         serializer = FlatDebtCollectionSerializer(unique_queues, many=True)
#         return Response(serializer.data)


# views.py

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import DebtCollectionCallQueue, DebtCollectionCallHistory
# from .serializers import DebtCollectionQueueSerializer, DebtCollectionHistorySerializer


# class DebtCollectionCallView(APIView):
#     def get(self, request):
#         queues = DebtCollectionCallQueue.objects.all()
#         serializer = DebtCollectionQueueSerializer(queues, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class DebtCollectionCallHistoryView(APIView):
#     def get(self, request):
#         history = DebtCollectionCallHistory.objects.all()
#         serializer = DebtCollectionHistorySerializer(history, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from .models import DebtCollectionCallQueue, DebtCollectionCallHistory
# from .serializers import DebtCollectionQueueSerializer, DebtCollectionHistorySerializer


# class DebtCollectionCallView(APIView):
#     def get(self, request):
#         queues = DebtCollectionCallQueue.objects.all()
#         serializer = DebtCollectionQueueSerializer(queues, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class DebtCollectionCallHistoryView(APIView):
#     def get(self, request):
#         history = DebtCollectionCallHistory.objects.all()
#         serializer = DebtCollectionHistorySerializer(history, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class MappedDebtCollectionView(APIView):
#     def get(self, request):
#         queues = DebtCollectionCallQueue.objects.all()
#         serializer = DebtCollectionQueueSerializer(queues, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)



# from django.http import JsonResponse
# from django.views import View
# from django.db.models import Sum
# from dashboard.models import DebtCollectionCallQueue, DebtCollectionCallHistory

# # Helper function to safely convert to float
# def safe_float(value):
#     return round(float(value), 2) if value is not None else 0.0

# class QueueHistoryCombinedView(View):
#     def get(self, request):
#         combined_data = []

#         # Fetch all call queue records
#         queue_data = DebtCollectionCallQueue.objects.all()

#         for queue in queue_data:
#             customer_id = queue.customer_id

#             # Get call history related to this customer
#             call_history = DebtCollectionCallHistory.objects.filter(customer_id=customer_id)

#             # Aggregate sums
#             total_interest = call_history.aggregate(total=Sum('call_id__interest_amount'))['total'] or 0
#             total_outstanding = call_history.aggregate(total=Sum('call_id__total_outstanding'))['total'] or 0
#             total_cd_amount = call_history.aggregate(total=Sum('call_id__total_cd_amount'))['total'] or 0

#             # Date fields
#             last_payment_date = queue.last_payment_date
#             cd_valid_date = queue.cd_valid_till

#             # Latest related call history (if any)
#             latest_history = call_history.order_by('-call_time').first()

#             data = {
#                 "id": queue.call_id,  # call_id is primary key
#                 "customer_name": queue.customer_name,
#                 "customer_id": queue.customer_id,
#                 "max_ocp": safe_float(queue.ocp),
#                 "total_outstanding": safe_float(total_outstanding),
#                 "total_interest": safe_float(total_interest),
#                 "cd valid amount": safe_float(queue.cd_amount),
#                 "cd valid date": cd_valid_date,
#                 "last payment date": last_payment_date,
#                 "total_cd_amount(upcoming overdue amount)": safe_float(total_cd_amount),
#                 "mode_of_payment": latest_history.mode_of_payment if latest_history else None,
#                 "promise_date": latest_history.promise_date if latest_history else None,
#                 "promise_amount": safe_float(latest_history.promise_amount) if latest_history else 0.0,
#             }

#             combined_data.append(data)

#         return JsonResponse(combined_data, safe=False)



# from django.http import JsonResponse
# from django.db.models import Max, Subquery, OuterRef
# from .models import DebtCollectionCallQueue, DebtCollectionCallHistory

# def queue_history_view(request):
#     # Subquery to get latest DebtCollectionCallHistory per customer
#     latest_history = DebtCollectionCallHistory.objects.filter(
#         customer_id=OuterRef('customer_id')
#     ).order_by('-id')  # assumes latest by ID

#     data = (
#         DebtCollectionCallQueue.objects
#         .values('customer_id', 'customer_name')
#         .annotate(
#             max_ocp=Max('ocp'),
#             total_outstanding=Max('total_outstanding'),  
#             total_interest=Max('interest_amount'),       
#             cd_valid_amount=Max('cd_amount'),            
#             cd_valid_date=Max('cd_valid_till'),
#             last_payment_date=Max('last_payment_date'),
#             total_cd_amount=Max('total_cd_amount'),
#             mode_of_payment=Subquery(latest_history.values('mode_of_payment')[:1]),
#             promise_date=Subquery(latest_history.values('promise_date')[:1]),
#             promise_amount=Subquery(latest_history.values('promise_amount')[:1])
#         )
#         .order_by('customer_id')
#     )

#     # Format response
#     results = []
#     for item in data:
#         results.append({
#             "customer_name": item["customer_name"],
#             "customer_id": item["customer_id"],
#             "max_ocp": item["max_ocp"],
#             "total_outstanding": item["total_outstanding"],
#             "total_interest": item["total_interest"],
#             "cd valid amount": item["cd_valid_amount"],
#             "cd valid date": item["cd_valid_date"],
#             "last payment date": item["last_payment_date"],
#             "total_cd_amount(upcoming overdue amount)": item["total_cd_amount"],
#             "mode_of_payment": item["mode_of_payment"],
#             "promise_date": item["promise_date"],
#             "promise_amount": item["promise_amount"],
#         })

#     return JsonResponse(results, safe=False)



# from django.views import View
# from django.http import JsonResponse
# from django.db.models import Max, Subquery, OuterRef
# from .models import DebtCollectionCallQueue, DebtCollectionCallHistory

# class QueueHistoryView(View):
#     def get(self, request, *args, **kwargs):
#         latest_history = DebtCollectionCallHistory.objects.filter(
#             customer_id=OuterRef('customer_id')
#         ).order_by('-id')

#         data = (
#             DebtCollectionCallQueue.objects
#             .values('customer_id', 'customer_name')
#             .annotate(
#                 max_ocp=Max('ocp'),
#                 total_outstanding=Max('total_outstanding'),
#                 total_interest=Max('interest_amount'),
#                 cd_valid_amount=Max('cd_amount'),
#                 cd_valid_date=Max('cd_valid_till'),
#                 last_payment_date=Max('last_payment_date'),
#                 total_cd_amount=Max('total_cd_amount'),
#                 mode_of_payment=Subquery(latest_history.values('mode_of_payment')[:1]),
#                 promise_date=Subquery(latest_history.values('promise_date')[:1]),
#                 promise_amount=Subquery(latest_history.values('promise_amount')[:1])
#             )
#             .order_by('customer_id')
#         )

#         results = []
#         for item in data:
#             results.append({
#                 "customer_name": item["customer_name"],
#                 "customer_id": item["customer_id"],
#                 "max_ocp": item["max_ocp"],
#                 "total_outstanding": item["total_outstanding"],
#                 "total_interest": item["total_interest"],
#                 "cd valid amount": item["cd_valid_amount"],
#                 "cd valid date": item["cd_valid_date"],
#                 "last payment date": item["last_payment_date"],
#                 "total_cd_amount(upcoming overdue amount)": item["total_cd_amount"],
#                 "mode_of_payment": item["mode_of_payment"],
#                 "promise_date": item["promise_date"],
#                 "promise_amount": item["promise_amount"],
#             })

#         return JsonResponse(results, safe=False)



# from django.http import JsonResponse
# from django.db.models import Max, Sum, Subquery, OuterRef, F
# from django.views import View
# from .models import DebtCollectionCallQueue, DebtCollectionCallHistory


# class QueueHistoryView(View):
#     def get(self, request):
#         # Subquery: Latest history data for each customer_id
#         latest_history = DebtCollectionCallHistory.objects.filter(
#             customer_id=OuterRef('customer_id')
#         ).order_by('-id')  # Assumes 'id' indicates most recent

#         # Step 1: Grouping customer-level data
#         customer_data = (
#             DebtCollectionCallQueue.objects
#             .values('customer_id', 'customer_name')
#             .annotate(
#                 max_ocp=Max('ocp'),
#                 total_outstanding=Sum('total_outstanding'),
#                 total_interest=Sum('interest_amount'),
#                 cd_valid_amount=Sum('cd_amount'),
#                 cd_valid_date=Max('cd_valid_till'),
#                 last_payment_date=Max('last_payment_date'),
#                 total_cd_amount=Sum('total_cd_amount'),
#                 mode_of_payment=Subquery(latest_history.values('mode_of_payment')[:1]),
#                 promise_date=Subquery(latest_history.values('promise_date')[:1]),
#                 promise_amount=Subquery(latest_history.values('promise_amount')[:1])
#             )
#             .order_by('customer_id')
#         )

#         # Step 2: Constructing the final response list
#         results = []
#         for item in customer_data:
#             # Fetch invoice-level details for this customer
#             invoices = DebtCollectionCallQueue.objects.filter(
#                 customer_id=item['customer_id']
#             ).values(
#                 'invoice_no',
#                 'product',
#                 'invoice_overdue',
#                 'ocp'
#             )

#             results.append({
#                 "customer_id": item["customer_id"],
#                 "customer_name": item["customer_name"],
#                 "max_ocp": item["max_ocp"],
#                 "total_outstanding": item["total_outstanding"],
#                 "total_interest": item["total_interest"],
#                 "cd_valid_amount": item["cd_valid_amount"],
#                 "cd_valid_date": item["cd_valid_date"],
#                 "last_payment_date": item["last_payment_date"],
#                 "total_cd_amount": item["total_cd_amount"],
#                 "mode_of_payment": item["mode_of_payment"],
#                 "promise_date": item["promise_date"],
#                 "promise_amount": item["promise_amount"],
#                 "invoices": list(invoices)
#             })

#         return JsonResponse(results, safe=False)

# null values hai jiske that customer is removeed
# from django.http import JsonResponse
# from django.db.models import Max, Sum, Subquery, OuterRef, F
# from django.views import View
# from .models import DebtCollectionCallQueue, DebtCollectionCallHistory


# class QueueHistoryView(View):
#     def get(self, request):
#         latest_history = DebtCollectionCallHistory.objects.filter(
#             customer_id=OuterRef('customer_id')
#         ).order_by('-id')

#         customer_data = (
#             DebtCollectionCallQueue.objects
#             .values('customer_id', 'customer_name')
#             .annotate(
#                 max_ocp=Max('ocp'),
#                 total_outstanding=Sum('total_outstanding'),
#                 total_interest=Sum('interest_amount'),
#                 cd_valid_amount=Sum('cd_amount'),
#                 cd_valid_date=Max('cd_valid_till'),
#                 last_payment_date=Max('last_payment_date'),
#                 total_cd_amount=Sum('total_cd_amount'),
#                 mode_of_payment=Subquery(latest_history.values('mode_of_payment')[:1]),
#                 promise_date=Subquery(latest_history.values('promise_date')[:1]),
#                 promise_amount=Subquery(latest_history.values('promise_amount')[:1])
#             )
#             .order_by('customer_id')
#         )

#         results = []

#         for item in customer_data:
#             # Filter out customers with all null "promise to pay" fields
#             if not (item["mode_of_payment"] or item["promise_date"] or item["promise_amount"]):
#                 continue  # Skip this customer

#             invoices = DebtCollectionCallQueue.objects.filter(
#                 customer_id=item['customer_id']
#             ).values(
#                 'invoice_no',
#                 'product',
#                 'invoice_overdue',
#                 'ocp'
#             )

#             results.append({
#                 "customer_id": item["customer_id"],
#                 "customer_name": item["customer_name"],
#                 "max_ocp": item["max_ocp"],
#                 "total_outstanding": item["total_outstanding"],
#                 "total_interest": item["total_interest"],
#                 "cd_valid_amount": item["cd_valid_amount"],
#                 "cd_valid_date": item["cd_valid_date"],
#                 "last_payment_date": item["last_payment_date"],
#                 "total_cd_amount": item["total_cd_amount"],
#                 "mode_of_payment": item["mode_of_payment"],
#                 "promise_date": item["promise_date"],
#                 "promise_amount": item["promise_amount"],
#                 "invoices": list(invoices)
#             })

#         return JsonResponse(results, safe=False)


# from django.http import JsonResponse
# from django.db.models import Max, Sum, Subquery, OuterRef
# from django.views import View
# from .models import DebtCollectionCallQueue, DebtCollectionCallHistory


# class QueueHistoryView(View):
#     def get(self, request):
#         # Subquery to fetch latest call history details for each customer
#         latest_history = DebtCollectionCallHistory.objects.filter(
#             customer_id=OuterRef('customer_id')
#         ).order_by('-id')

#         # Aggregate customer-level data
#         customer_data = (
#             DebtCollectionCallQueue.objects
#             .values('customer_id', 'customer_name')
#             .annotate(
#                 max_ocp=Max('ocp'),
#                 total_outstanding=Sum('total_outstanding'),
#                 total_interest=Sum('interest_amount'),
#                 cd_valid_amount=Sum('cd_amount'),
#                 cd_valid_date=Max('cd_valid_till'),
#                 last_payment_date=Max('last_payment_date'),
#                 total_cd_amount=Sum('total_cd_amount'),
#                 mode_of_payment=Subquery(latest_history.values('mode_of_payment')[:1]),
#                 promise_date=Subquery(latest_history.values('promise_date')[:1]),
#                 promise_amount=Subquery(latest_history.values('promise_amount')[:1])
#             )
#             .order_by('customer_id')
#         )

#         results = []

#         for item in customer_data:
#             # Skip customers without promise-to-pay details
#             if not (item["mode_of_payment"] or item["promise_date"] or item["promise_amount"]):
#                 continue

#             # Fetch invoices for the customer (removed invalid 'status' filter)
#             invoices = DebtCollectionCallQueue.objects.filter(
#                 customer_id=item['customer_id']
#             ).values(
#                 'invoice_no',
#                 'product',
#                 'invoice_overdue',
#                 'ocp'
#             )

#             # Skip if no invoices found
#             if not invoices.exists():
#                 continue

#             # Append combined customer data and invoice list
#             results.append({
#                 "customer_id": item["customer_id"],
#                 "customer_name": item["customer_name"],
#                 "max_ocp": item["max_ocp"],
#                 "total_outstanding": item["total_outstanding"],
#                 "total_interest": item["total_interest"],
#                 "cd_valid_amount": item["cd_valid_amount"],
#                 "cd_valid_date": item["cd_valid_date"],
#                 "last_payment_date": item["last_payment_date"],
#                 "total_cd_amount": item["total_cd_amount"],
#                 "mode_of_payment": item["mode_of_payment"],
#                 "promise_date": item["promise_date"],
#                 "promise_amount": item["promise_amount"],
#                 "invoices": list(invoices)
#             })

#         return JsonResponse(results, safe=False)



from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Max, Sum, OuterRef, Subquery, F
from django.db.models.functions import Lower
from .models import DebtCollectionCallQueue, DebtCollectionCallHistory


class QueueHistoryAPIView(APIView):
    def get(self, request):
        conclusion_filter = request.GET.get("conclusion", None)

        if not conclusion_filter:
            return Response({"error": "Missing 'conclusion' parameter."}, status=400)

        normalized_filter = conclusion_filter.strip().lower()

        # Subquery to get the latest history per customer with normalized matching conclusion
        filtered_history = (
            DebtCollectionCallHistory.objects
            .annotate(norm_conclusion=Lower('conclusion'))
            .filter(customer_id=OuterRef('customer_id'), norm_conclusion=normalized_filter)
            .order_by('-id')
        )

        customer_data = (
            DebtCollectionCallQueue.objects
            .values('customer_id', 'customer_name')
            .annotate(
                max_ocp=Max('ocp'),
                total_outstanding=Sum('total_outstanding'),
                total_interest=Sum('interest_amount'),
                cd_valid_amount=Sum('cd_amount'),
                cd_valid_date=Max('cd_valid_till'),
                last_payment_date=Max('last_payment_date'),
                total_cd_amount=Sum('total_cd_amount'),
                mode_of_payment=Subquery(filtered_history.values('mode_of_payment')[:1]),
                promise_date=Subquery(filtered_history.values('promise_date')[:1]),
                promise_amount=Subquery(filtered_history.values('promise_amount')[:1]),
                conclusion=Subquery(filtered_history.values('conclusion')[:1]),
            )
            .order_by('customer_id')
        )

        # Final filter to only include those with matching conclusion
        results = []
        for item in customer_data:
            if not item['conclusion'] or item['conclusion'].strip().lower() != normalized_filter:
                continue

            invoices = DebtCollectionCallQueue.objects.filter(
                customer_id=item['customer_id']
            ).values('invoice_no', 'product', 'invoice_overdue', 'ocp')

            if not invoices.exists():
                continue

            results.append({
                "customer_id": item["customer_id"],
                "customer_name": item["customer_name"],
                "max_ocp": item["max_ocp"],
                "total_outstanding": item["total_outstanding"],
                "total_interest": item["total_interest"],
                "cd_valid_amount": item["cd_valid_amount"],
                "cd_valid_date": item["cd_valid_date"],
                "last_payment_date": item["last_payment_date"],
                "total_cd_amount": item["total_cd_amount"],
                "mode_of_payment": item["mode_of_payment"],
                "promise_date": item["promise_date"],
                "promise_amount": item["promise_amount"],
                "conclusion": item["conclusion"],
                "invoices": list(invoices)
            })

        return Response(results)
