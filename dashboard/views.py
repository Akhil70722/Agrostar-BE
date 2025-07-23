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



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.db.models import Max, Sum, Subquery, OuterRef, Count
# from django.db.models.functions import Lower
# from .models import DebtCollectionCallQueue, DebtCollectionCallHistory
# from datetime import datetime

# class QueueHistoryAPIView(APIView):
#     def get(self, request):
#         # Get optional filters
#         conclusion_filter = request.GET.get("conclusion")
#         from_date = request.GET.get("from_date")
#         to_date = request.GET.get("to_date")
#         partner_id = request.GET.get("partner_id")  # actually customer_id

#         # Start with all queue data
#         queue_queryset = DebtCollectionCallQueue.objects.all()

#         # Filter by dates if provided
#         if from_date:
#             try:
#                 from_date_obj = datetime.strptime(from_date, "%Y-%m-%d")
#                 queue_queryset = queue_queryset.filter(call_date__gte=from_date_obj)
#             except ValueError:
#                 return Response({"error": "Invalid from_date format. Use YYYY-MM-DD"}, status=400)

#         if to_date:
#             try:
#                 to_date_obj = datetime.strptime(to_date, "%Y-%m-%d")
#                 queue_queryset = queue_queryset.filter(call_date__lte=to_date_obj)
#             except ValueError:
#                 return Response({"error": "Invalid to_date format. Use YYYY-MM-DD"}, status=400)

#         # Filter by customer_id if provided
#         if partner_id:
#             queue_queryset = queue_queryset.filter(customer_id=partner_id)

#         # Prepare subquery for latest history with normalized conclusion (if provided)
#         filtered_history = DebtCollectionCallHistory.objects.annotate(
#             norm_conclusion=Lower('conclusion')
#         ).filter(
#             customer_id=OuterRef('customer_id')
#         ).order_by('-id')

#         # If conclusion_filter provided, filter subquery further
#         if conclusion_filter:
#             normalized_filter = conclusion_filter.strip().lower()
#             filtered_history = filtered_history.filter(norm_conclusion=normalized_filter)

#         # Annotate customer data
#         customer_data = (
#             queue_queryset
#             .values('customer_id', 'customer_name')
#             .annotate(
#                 max_ocp=Max('ocp'),
#                 total_outstanding=Sum('total_outstanding'),
#                 total_interest=Sum('interest_amount'),
#                 cd_valid_amount=Sum('cd_amount'),
#                 cd_valid_date=Max('cd_valid_till'),
#                 last_payment_date=Max('last_payment_date'),
#                 total_cd_amount=Sum('total_cd_amount'),
#                 mode_of_payment=Subquery(filtered_history.values('mode_of_payment')[:1]),
#                 promise_date=Subquery(filtered_history.values('promise_date')[:1]),
#                 promise_amount=Subquery(filtered_history.values('promise_amount')[:1]),
#                 conclusion=Subquery(filtered_history.values('conclusion')[:1]),
#                 call_attempts=Count('call_id')  # ✅ Added number of attempts
#             )
#             .order_by('customer_id')
#         )

#         results = []
#         for item in customer_data:
#             # If conclusion_filter is provided, filter results again
#             if conclusion_filter:
#                 if not item['conclusion'] or item['conclusion'].strip().lower() != normalized_filter:
#                     continue

#             # Get invoices
#             invoices = queue_queryset.filter(
#                 customer_id=item['customer_id']
#             ).values('invoice_no', 'product', 'invoice_overdue', 'ocp')

#             if not invoices.exists():
#                 continue

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
#                 "conclusion": item["conclusion"],
#                 "call_attempts": item["call_attempts"],  # ✅ Return in response
#                 "invoices": list(invoices)
#             })

#         return Response(results)

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.db import connection
# from datetime import datetime


# # Helper function to run raw SQL and return list of dicts
# def execute_raw_sql(query, params=None):
#     with connection.cursor() as cursor:
#         cursor.execute(query, params)
#         desc = [col[0] for col in cursor.description]
#         return [dict(zip(desc, row)) for row in cursor.fetchall()]


# class QueueHistoryAPIView(APIView):
#     def get(self, request):
#         conclusion_filter = request.GET.get("conclusion")
#         from_date = request.GET.get("from_date")
#         to_date = request.GET.get("to_date")
#         partner_id = request.GET.get("partner_id")

#         # Validate date formats
#         try:
#             if from_date:
#                 datetime.strptime(from_date, "%Y-%m-%d")
#             if to_date:
#                 datetime.strptime(to_date, "%Y-%m-%d")
#         except ValueError:
#             return Response({"error": "Invalid date format. Use YYYY-MM-DD"}, status=400)

#         # ✅ Corrected table names below
#         main_query = """
#             WITH latest_history AS (
#                 SELECT DISTINCT ON (customer_id)
#                     customer_id,
#                     mode_of_payment,
#                     promise_date,
#                     promise_amount,
#                     conclusion
#                 FROM debtcollectioncallhistory
#                 WHERE (%(conclusion_filter)s IS NULL OR LOWER(conclusion) = LOWER(%(conclusion_filter)s))
#                 ORDER BY customer_id, id DESC
#             ),
#             queue_filtered AS (
#                 SELECT *
#                 FROM debtcollectioncallqueue
#                 WHERE (%(from_date)s IS NULL OR call_date >= %(from_date)s)
#                   AND (%(to_date)s IS NULL OR call_date <= %(to_date)s)
#                   AND (%(partner_id)s IS NULL OR customer_id = %(partner_id)s)
#             )
#             SELECT
#                 q.customer_id,
#                 q.customer_name,
#                 MAX(q.ocp) AS max_ocp,
#                 SUM(q.total_outstanding) AS total_outstanding,
#                 SUM(q.interest_amount) AS total_interest,
#                 SUM(q.cd_amount) AS cd_valid_amount,
#                 MAX(q.cd_valid_till) AS cd_valid_date,
#                 MAX(q.last_payment_date) AS last_payment_date,
#                 SUM(q.total_cd_amount) AS total_cd_amount,
#                 COUNT(q.call_id) AS call_attempts,
#                 lh.mode_of_payment,
#                 lh.promise_date,
#                 lh.promise_amount,
#                 lh.conclusion
#             FROM queue_filtered q
#             LEFT JOIN latest_history lh ON q.customer_id = lh.customer_id
#             GROUP BY q.customer_id, q.customer_name, lh.mode_of_payment, lh.promise_date, lh.promise_amount, lh.conclusion
#             ORDER BY q.customer_id;
#         """

#         params = {
#             "conclusion_filter": conclusion_filter,
#             "from_date": from_date,
#             "to_date": to_date,
#             "partner_id": partner_id,
#         }

#         customer_data = execute_raw_sql(main_query, params)
#         normalized_filter = conclusion_filter.strip().lower() if conclusion_filter else None

#         results = []
#         for item in customer_data:
#             # Apply conclusion filter again (to mimic ORM behavior)
#             if normalized_filter:
#                 if not item['conclusion'] or item['conclusion'].strip().lower() != normalized_filter:
#                     continue

#             # ✅ Corrected table name here as well
#             invoice_query = """
#                 SELECT invoice_no, product, invoice_overdue, ocp
#                 FROM debtcollectioncallqueue
#                 WHERE customer_id = %s
#             """
#             invoices = execute_raw_sql(invoice_query, [item['customer_id']])

#             if not invoices:
#                 continue  # skip if no invoices found (mimic previous logic)

#             # Final output dictionary
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
#                 "conclusion": item["conclusion"],
#                 "call_attempts": item["call_attempts"],
#                 "invoices": invoices,
#             })

#         return Response(results)



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.db.models import Max, Sum, Subquery, OuterRef
# from django.db.models.functions import Lower
# from .models import DebtCollectionCallQueue, DebtCollectionCallHistory
# from datetime import datetime

# class QueueHistoryAPIView(APIView):
#     def get(self, request):
#         # Get optional filters
#         conclusion_filter = request.GET.get("conclusion")
#         from_date = request.GET.get("from_date")
#         to_date = request.GET.get("to_date")
#         partner_id = request.GET.get("partner_id")  # actually customer_id

#         # Start with all queue data
#         queue_queryset = DebtCollectionCallQueue.objects.all()

#         # Filter by dates if provided
#         if from_date:
#             try:
#                 from_date_obj = datetime.strptime(from_date, "%Y-%m-%d")
#                 queue_queryset = queue_queryset.filter(call_date__gte=from_date_obj)
#             except ValueError:
#                 return Response({"error": "Invalid from_date format. Use YYYY-MM-DD"}, status=400)

#         if to_date:
#             try:
#                 to_date_obj = datetime.strptime(to_date, "%Y-%m-%d")
#                 queue_queryset = queue_queryset.filter(call_date__lte=to_date_obj)
#             except ValueError:
#                 return Response({"error": "Invalid to_date format. Use YYYY-MM-DD"}, status=400)

#         # Filter by customer_id if provided
#         if partner_id:
#             queue_queryset = queue_queryset.filter(customer_id=partner_id)

#         # Prepare subquery for latest history with normalized conclusion (if provided)
#         filtered_history = DebtCollectionCallHistory.objects.annotate(
#             norm_conclusion=Lower('conclusion')
#         ).filter(
#             customer_id=OuterRef('customer_id')
#         ).order_by('-id')

#         # If conclusion_filter provided, filter subquery further
#         if conclusion_filter:
#             normalized_filter = conclusion_filter.strip().lower()
#             filtered_history = filtered_history.filter(norm_conclusion=normalized_filter)
#         else:
#             normalized_filter = None

#         # Annotate customer data
#         customer_data = (
#             queue_queryset
#             .values('customer_id', 'customer_name')
#             .annotate(
#                 max_ocp=Max('ocp'),
#                 total_outstanding=Sum('total_outstanding'),
#                 total_interest=Sum('interest_amount'),
#                 cd_valid_amount=Sum('cd_amount'),
#                 cd_valid_date=Max('cd_valid_till'),
#                 last_payment_date=Max('last_payment_date'),
#                 total_cd_amount=Sum('total_cd_amount'),
#                 mode_of_payment=Subquery(filtered_history.values('mode_of_payment')[:1]),
#                 promise_date=Subquery(filtered_history.values('promise_date')[:1]),
#                 promise_amount=Subquery(filtered_history.values('promise_amount')[:1]),
#                 conclusion=Subquery(filtered_history.values('conclusion')[:1]),
#             )
#             .order_by('customer_id')
#         )

#         # Collect all customer_ids
#         customer_ids = [item['customer_id'] for item in customer_data]

#         # Fetch all invoices for these customers in one query
#         invoices_qs = queue_queryset.filter(
#             customer_id__in=customer_ids
#         ).values('customer_id', 'invoice_no', 'product', 'invoice_overdue', 'ocp')

#         # Build a map: customer_id → list of invoices
#         invoices_map = {}
#         for inv in invoices_qs:
#             invoices_map.setdefault(inv['customer_id'], []).append(inv)

#         results = []
#         for item in customer_data:
#             # If conclusion_filter is provided, filter results again
#             if normalized_filter:
#                 if not item['conclusion'] or item['conclusion'].strip().lower() != normalized_filter:
#                     continue

#             invoices = invoices_map.get(item['customer_id'], [])
#             if not invoices:
#                 continue

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
#                 "conclusion": item["conclusion"],
#                 "invoices": invoices
#             })

#         return Response(results)
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
from datetime import datetime
 
 
def execute_raw_sql(query, params=None):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        desc = [col[0] for col in cursor.description]
        return [dict(zip(desc, row)) for row in cursor.fetchall()]
 
 
class QueueHistoryAPIView(APIView):
    def get(self, request):
        # Filters
        conclusion_filter = request.GET.get("conclusion")
        from_date = request.GET.get("from_date")
        to_date = request.GET.get("to_date")
        partner_id = request.GET.get("partner_id")
 
        # Pagination (default: first 100 rows)
        limit = int(request.GET.get("limit", 100))
        offset = int(request.GET.get("offset", 0))
 
        # Validate dates
        try:
            if from_date:
                datetime.strptime(from_date, "%Y-%m-%d")
            if to_date:
                datetime.strptime(to_date, "%Y-%m-%d")
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD"}, status=400)
 
        # Main customer query
        main_query = """
            WITH latest_history AS (
                SELECT DISTINCT ON (customer_id)
                    customer_id,
                    mode_of_payment,
                    promise_date,
                    promise_amount,
                    conclusion
                FROM debtcollectioncallhistory
                WHERE (%(conclusion_filter)s IS NULL OR LOWER(conclusion) = LOWER(%(conclusion_filter)s))
                ORDER BY customer_id, id DESC
            ),
            queue_filtered AS (
                SELECT *
                FROM debtcollectioncallqueue
                WHERE (%(from_date)s IS NULL OR call_date >= %(from_date)s)
                  AND (%(to_date)s IS NULL OR call_date <= %(to_date)s)
                  AND (%(partner_id)s IS NULL OR customer_id = %(partner_id)s)
            )
            SELECT
                q.customer_id,
                MAX(q.customer_name) AS customer_name,
                MAX(q.ocp) AS max_ocp,
                SUM(q.total_outstanding) AS total_outstanding,
                SUM(q.interest_amount) AS total_interest,
                SUM(q.cd_amount) AS cd_valid_amount,
                MAX(q.cd_valid_till) AS cd_valid_date,
                MAX(q.last_payment_date) AS last_payment_date,
                SUM(q.total_cd_amount) AS total_cd_amount,
                COUNT(q.call_id) AS call_attempts,
                lh.mode_of_payment,
                lh.promise_date,
                lh.promise_amount,
                lh.conclusion
            FROM queue_filtered q
            INNER JOIN latest_history lh ON q.customer_id = lh.customer_id
            WHERE (%(conclusion_filter)s IS NULL OR LOWER(lh.conclusion) = LOWER(%(conclusion_filter)s))
            GROUP BY q.customer_id, lh.mode_of_payment, lh.promise_date, lh.promise_amount, lh.conclusion
            ORDER BY q.customer_id
            LIMIT %(limit)s OFFSET %(offset)s
        """
 
        params = {
            "conclusion_filter": conclusion_filter,
            "from_date": from_date,
            "to_date": to_date,
            "partner_id": partner_id,
            "limit": limit,
            "offset": offset,
        }
        print("[QueueHistoryAPIView] Incoming params:", params)
 
        customer_data = execute_raw_sql(main_query, params)
 
        # ✅ Fetch all invoices in a single query (not one per customer)
        customer_ids = [row["customer_id"] for row in customer_data]
        invoice_map = {}
        if customer_ids:
            invoice_query = """
                SELECT customer_id, invoice_no, product, invoice_overdue, ocp
                FROM debtcollectioncallqueue
                WHERE customer_id = ANY(%s)
            """
            invoice_data = execute_raw_sql(invoice_query, [customer_ids])
            for inv in invoice_data:
                invoice_map.setdefault(inv["customer_id"], []).append({
                    "invoice_no": inv["invoice_no"],
                    "product": inv["product"],
                    "invoice_overdue": float(inv["invoice_overdue"] or 0),
                    "ocp": float(inv["ocp"] or 0),
                })
 
        # Final response build
        normalized_filter = conclusion_filter.strip().lower() if conclusion_filter else None
        results = []
        for item in customer_data:
            results.append({
                "customer_id": item["customer_id"],
                "customer_name": item["customer_name"],
                "max_ocp": float(item["max_ocp"] or 0),
                "total_outstanding": float(item["total_outstanding"] or 0),
                "total_interest": float(item["total_interest"] or 0),
                "cd_valid_amount": float(item["cd_valid_amount"] or 0),
                "cd_valid_date": item["cd_valid_date"],
                "last_payment_date": item["last_payment_date"],
                "total_cd_amount": float(item["total_cd_amount"] or 0),
                "mode_of_payment": item["mode_of_payment"],
                "promise_date": item["promise_date"],
                "promise_amount": float(item["promise_amount"] or 0),
                "conclusion": item["conclusion"],
                "call_attempts": item["call_attempts"],
                "invoices": invoice_map.get(item["customer_id"], []),
            })

        return Response(results)