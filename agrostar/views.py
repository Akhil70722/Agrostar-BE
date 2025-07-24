from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from datetime import datetime
from collections import defaultdict
from .models import DebtCollectionCallQueue, DebtCollectionCallHistory
from rest_framework import status
from django.db.models import Max, Sum
import json


# =======================
# Dashboard API
# =======================
class DashboardAPI(APIView):
    def get(self, request):
        from_date = request.GET.get("from_date")
        to_date = request.GET.get("to_date")
 
        if not from_date or not to_date:
            return Response({"error": "from_date and to_date are required as query parameters."},
                            status=status.HTTP_400_BAD_REQUEST)
 
        return self._fetch_data(from_date, to_date)
 
    def post(self, request):
        from_date = request.data.get("from_date")
        to_date = request.data.get("to_date")
 
        if not from_date or not to_date:
            return Response({"error": "from_date and to_date are required in request body."},
                            status=status.HTTP_400_BAD_REQUEST)
 
        return self._fetch_data(from_date, to_date)
 
    def _fetch_data(self, from_date, to_date):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM get_dashboard_agrostar_v1(%s, %s);", [from_date, to_date])
                columns = [col[0] for col in cursor.description]
                results = [
                    dict(zip(columns, row))
                    for row in cursor.fetchall()
                ]
 
            return Response(results, status=status.HTTP_200_OK)
 
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# =======================
# Cards API
# =======================
def execute_raw_sql(query, params=None):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        desc = [col[0] for col in cursor.description]
        return [dict(zip(desc, row)) for row in cursor.fetchall()]


class CardsAPI(APIView):
    def get(self, request):
        # Query params
        conclusion_filter = request.GET.get("conclusion")
        from_date = request.GET.get("from_date")
        to_date = request.GET.get("to_date")
        partner_id = request.GET.get("partner_id")

        # Pagination
        limit = int(request.GET.get("limit", 100))
        offset = int(request.GET.get("offset", 0))

        # Date validation
        try:
            if from_date:
                datetime.strptime(from_date, "%Y-%m-%d")
            if to_date:
                datetime.strptime(to_date, "%Y-%m-%d")
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD"}, status=400)

        # Main SQL query
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
                ORDER BY customer_id, call_time DESC
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
                MAX(q.total_outstanding) AS total_outstanding,
                SUM(q.interest_amount) AS total_interest,
                MAX(q.cd_amount) AS cd_valid_amount,
                MAX(q.cd_valid_till) AS cd_valid_date,
                MAX(q.last_payment_date) AS last_payment_date,
                MAX(q.total_cd_amount) AS total_cd_amount,
                MAX(q.call_tried) AS call_attempts,
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

        customer_data = execute_raw_sql(main_query, params)

        # Fetch invoice data
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

        # Format final response
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
                "call_attempts": int(item["call_attempts"] or 0),
                "invoices": invoice_map.get(item["customer_id"], []),
            })

        return Response(results)



# =======================
# Partners API
# =======================

# =======================
# 1. Main Partner Summary API
# =======================
class PartnersDataAPIView(APIView):
    def get(self, request):
        connected_param = request.GET.get("connected", "").strip().lower()
        apply_connected_filter = connected_param in ["true", "false"]

        # Base queryset
        qs = DebtCollectionCallQueue.objects.all()

        # Filter by call_connected
        if apply_connected_filter:
            qs = qs.filter(call_connected=(connected_param == "true"))

        # Filter by partner_id (customer_id)
        partner_id = request.GET.get("partner_id")
        if partner_id:
            qs = qs.filter(customer_id=partner_id)

        # Date filters
        from_date = request.GET.get("from_date")
        to_date = request.GET.get("to_date")
        if from_date and to_date:
            qs = qs.filter(call_date__range=[from_date, to_date])
        elif from_date:
            qs = qs.filter(call_date__gte=from_date)
        elif to_date:
            qs = qs.filter(call_date__lte=to_date)

        # Exclude invalid customers
        qs = qs.exclude(customer_id__isnull=True).exclude(customer_id="")

        # Aggregate queue data per customer
        partner_data = qs.values("customer_id", "customer_name").annotate(
            no_of_attempts    = Max("call_tried"),
            ocp               = Max("ocp"),
            total_outstanding = Max("total_outstanding"),
            cd_valid_till     = Max("cd_valid_till"),
            cd_amount         = Max("cd_amount"),
            total_cd_amount   = Max("total_cd_amount"),
            as_on_date        = Max("call_date"),  # 👈 added this line
        )

        customer_ids = [p["customer_id"] for p in partner_data]

        # Latest promise info from history, grouped by customer_id
        history_agg = (
            DebtCollectionCallHistory.objects
            .filter(customer_id__in=customer_ids)
            .values("customer_id")
            .annotate(
                promise_date   = Max("promise_date"),
                promise_amount = Max("promise_amount")
            )
        )
        history_map = {
            h["customer_id"]: {
                "promise_date": h["promise_date"],
                "promise_amount": float(h["promise_amount"] or 0),
            }
            for h in history_agg
        }

        # Count distinct products per customer
        product_qs = qs.values("customer_id", "product") \
                       .exclude(product__isnull=True).exclude(product="")
        customer_products = defaultdict(set)
        for entry in product_qs:
            customer_products[entry["customer_id"]].add(entry["product"])

        # Build final response
        response_data = []
        for item in partner_data:
            cid = item["customer_id"]
            hist = history_map.get(cid, {})
            prods = customer_products.get(cid, set())

            response_data.append({
                "customer_id":       cid,
                "customer_name":     item["customer_name"],
                "no_of_attempts":    item["no_of_attempts"] or 0,
                "ocp":               float(item["ocp"] or 0),
                "total_outstanding": float(item["total_outstanding"] or 0),
                "cd_valid_till":     item["cd_valid_till"],
                "cd_amount":         float(item["cd_amount"] or 0),
                "total_cd_amount":   float(item["total_cd_amount"] or 0),
                "promise_date":      hist.get("promise_date"),
                "promise_amount":    hist.get("promise_amount", 0),
                "product_count":     len(prods),
                "as_on_date":        item["as_on_date"],  # 👈 added this line to response
            })

        return Response({"data": response_data})


# =======================
# 2. After clicking on number of attempts 
# =======================
class PartnerAttemptDetailsAPIView(APIView):
    def get(self, request, partner_id):
        # Fetch all queue records for the partner_id
        records = DebtCollectionCallQueue.objects.filter(customer_id=partner_id).order_by("-call_date")

        if not records.exists():
            return Response(
                {"detail": "No call attempts found for this partner ID."},
                status=status.HTTP_404_NOT_FOUND
            )

        response = []
        for idx, r in enumerate(records, start=1):
            # Fetch history matching the call_id of this record
            history = DebtCollectionCallHistory.objects.filter(call_id=r.call_id).order_by("-promise_date").first()

            response.append({
                "serial_number": idx,
                "customer_id": r.customer_id,
                "customer_name": r.customer_name,
                # "no_of_attempts": r.call_tried or 0,
                "ocp": float(r.ocp or 0),
                "total_outstanding": float(r.total_outstanding or 0),
                "cd_valid_till": r.cd_valid_till,
                "cd_amount": float(r.cd_amount or 0),
                "total_cd_amount": float(r.total_cd_amount or 0),
                "product": r.product or "",
                "promise_date": history.promise_date if history else None,
                "promise_amount": float(history.promise_amount or 0) if history else 0,
            })

        return Response({"data": response})


# =======================
# 3. Total Partners Engagement API
# =======================
class TotalPartnerEngagementAPIView(APIView):
    def get(self, request):
        connected_calls     = DebtCollectionCallQueue.objects.filter(call_connected=True).count()
        not_connected_calls = DebtCollectionCallQueue.objects.filter(call_connected=False).count()
        ai_calls            = DebtCollectionCallQueue.objects.filter(partner_company_name__icontains="ai").count()

        total = connected_calls + not_connected_calls + ai_calls
        return Response({"total_partner_engagement": total})


# =======================
# Communication API
# =======================
class CommunicationAPIView(APIView):
    def get(self, request):
        partner_id = request.GET.get('partner_id')

        if not partner_id:
            return Response({"error": "partner_id is required"}, status=400)

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT DISTINCT ON (h.call_id)
                h.id,
                h.call_id,
                q.partner_company_name,
                h.call_time,
                h.conversation_json,
                h.recording,
                h.call_summary_notes,
                h.call_duration,
                h.conclusion
                FROM  debtcollectioncallhistory h
                LEFT JOIN debtcollectioncallqueue q ON  h.customer_id = q.customer_id
                WHERE h.customer_id = %s
                ORDER BY h.call_id, h.call_time DESC;
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
                # "conversation_data": parsed_json,
                "recording_url": recording_url,
                "call_summary_notes": call_summary_notes or "",
                "call_duration": call_duration or 0,
                "conclusion": conclusion or ""
            })

        return Response(result)
