# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.db import connection
# import datetime


# class EngagementAPIView(APIView):
#     def get(self, request):
#         return self._fetch_data()

#     def post(self, request):
#         from_date = request.data.get("from_date")
#         to_date = request.data.get("to_date")

#         if not from_date or not to_date:
#             return Response({"error": "from_date and to_date are required."},
#                             status=status.HTTP_400_BAD_REQUEST)

#         try:
#             from_date = datetime.datetime.strptime(from_date, "%Y-%m-%d").date()
#             to_date = datetime.datetime.strptime(to_date, "%Y-%m-%d").date()
#         except Exception as e:
#             return Response({"error": "Invalid date format. Use YYYY-MM-DD"},
#                             status=status.HTTP_400_BAD_REQUEST)

#         return self._fetch_data(from_date, to_date)

#     def _fetch_data(self, from_date=None, to_date=None):
#         with connection.cursor() as cursor:
#             # ✅ FIXED TABLE NAME HERE
#             engagement_query = """
#                 SELECT DATE(call_time) as CreatedDate, COUNT(*) as total_engaged
#                 FROM debtcollectioncallhistory
#                 WHERE conclusion IS NOT NULL
#             """
#             if from_date and to_date:
#                 engagement_query += " AND DATE(call_time) BETWEEN %s AND %s"
#                 cursor.execute(engagement_query + " GROUP BY DATE(call_time) ORDER BY DATE(call_time)", [from_date, to_date])
#             else:
#                 cursor.execute(engagement_query + " GROUP BY DATE(call_time) ORDER BY DATE(call_time)")

#             engagement_data = [
#                 {"CreatedDate": row[0].strftime("%Y-%m-%d"), "total_engaged": row[1]}
#                 for row in cursor.fetchall()
#             ]

#             # ✅ FIXED TABLE NAME HERE
#             dashboard_query = """
#                 SELECT
#                     COUNT(*) FILTER (WHERE conclusion IS NULL) AS customers_to_connect,
#                     COUNT(*) FILTER (WHERE conclusion IS NOT NULL) AS customers_connected,
#                     COUNT(*) FILTER (WHERE conclusion = 'Promised to pay') AS promised_to_pay,
#                     COUNT(*) FILTER (WHERE conclusion = 'Refuse to pay') AS refuse_to_pay,
#                     COUNT(*) FILTER (WHERE conclusion = 'Already paid') AS already_paid,
#                     COUNT(*) FILTER (WHERE conclusion = 'Wrong number') AS wrong_number,
#                     COALESCE(SUM(promise_amount), 0) AS total_promised_amount
#                 FROM debtcollectioncallhistory
#             """
#             if from_date and to_date:
#                 dashboard_query += " WHERE DATE(call_time) BETWEEN %s AND %s"
#                 cursor.execute(dashboard_query, [from_date, to_date])
#             else:
#                 cursor.execute(dashboard_query)

#             row = cursor.fetchone()
#             dashboard_data = [{
#                 "customers_to_connect": row[0],
#                 "customers_connected": row[1],
#                 "promised_to_pay": row[2],
#                 "refuse_to_pay": row[3],
#                 "already_paid": row[4],
#                 "wrong_number": row[5],
#                 "total_promised_amount": row[6],
#             }]

#         return Response({
#             "engagement_data": engagement_data,
#             "dashboard_data": dashboard_data
#         })


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.db import connection
# import datetime


# class EngagementAPIView(APIView):
#     def get(self, request):
#         return self._fetch_data()

#     def post(self, request):
#         from_date = request.data.get("from_date")
#         to_date = request.data.get("to_date")

#         if not from_date or not to_date:
#             return Response(
#                 {"error": "from_date and to_date are required."},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             from_date = datetime.datetime.strptime(from_date, "%Y-%m-%d").date()
#             to_date = datetime.datetime.strptime(to_date, "%Y-%m-%d").date()
#         except ValueError:
#             return Response(
#                 {"error": "Invalid date format. Use YYYY-MM-DD"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         return self._fetch_data(from_date, to_date)

#     def _fetch_data(self, from_date=None, to_date=None):
#         with connection.cursor() as cursor:
#             # ✅ Query for engagement chart data
#             engagement_query = """
#                 SELECT DATE(call_time) AS CreatedDate, COUNT(*) AS total_engaged
#                 FROM debtcollectioncallhistory
#                 WHERE conclusion IS NOT NULL
#             """
#             query_params = []
#             if from_date and to_date:
#                 engagement_query += " AND DATE(call_time) BETWEEN %s AND %s"
#                 query_params += [from_date, to_date]

#             engagement_query += " GROUP BY DATE(call_time) ORDER BY DATE(call_time)"
#             cursor.execute(engagement_query, query_params)

#             engagement_data = [
#                 {
#                     "CreatedDate": row[0].strftime("%Y-%m-%d"),
#                     "total_engaged": row[1]
#                 }
#                 for row in cursor.fetchall()
#             ]

#             # ✅ Query for dashboard summary data
#             dashboard_query = """
#                 SELECT
#                     COUNT(*) FILTER (WHERE conclusion IS NULL) AS customers_to_connect,
#                     COUNT(*) FILTER (WHERE conclusion IS NOT NULL) AS customers_connected,
#                     COUNT(*) FILTER (WHERE conclusion = 'Promised to pay') AS promised_to_pay,
#                     COUNT(*) FILTER (WHERE conclusion = 'Refuse to pay') AS refuse_to_pay,
#                     COUNT(*) FILTER (WHERE conclusion = 'Already paid') AS already_paid,
#                     COUNT(*) FILTER (WHERE conclusion = 'Wrong number') AS wrong_number,
#                     COALESCE(SUM(promise_amount), 0) AS total_promised_amount
#                 FROM debtcollectioncallhistory
#             """
#             query_params = []
#             if from_date and to_date:
#                 dashboard_query += " WHERE DATE(call_time) BETWEEN %s AND %s"
#                 query_params += [from_date, to_date]

#             cursor.execute(dashboard_query, query_params)
#             row = cursor.fetchone()

#             dashboard_data = [{
#                 "customers_to_connect": row[0],
#                 "customers_connected": row[1],
#                 "promised_to_pay": row[2],
#                 "refuse_to_pay": row[3],
#                 "already_paid": row[4],
#                 "wrong_number": row[5],
#                 "total_promised_amount": float(row[6])  # ensure JSON serializable
#             }]

#         return Response({
#             "engagement_data": engagement_data,
#             "dashboard_data": dashboard_data
#         })



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.db import connection
# import datetime


# class EngagementAPIView(APIView):
#     def get(self, request):
#         return self._fetch_data()

#     def post(self, request):
#         from_date = request.data.get("from_date")
#         to_date = request.data.get("to_date")

#         if not from_date or not to_date:
#             return Response(
#                 {"error": "from_date and to_date are required."},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             from_date = datetime.datetime.strptime(from_date, "%Y-%m-%d").date()
#             to_date = datetime.datetime.strptime(to_date, "%Y-%m-%d").date()
#         except ValueError:
#             return Response(
#                 {"error": "Invalid date format. Use YYYY-MM-DD"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         return self._fetch_data(from_date, to_date)

#     def _fetch_data(self, from_date=None, to_date=None):
#         try:
#             with connection.cursor() as cursor:
#                 # ✅ 1. Engagement Chart Data
#                 engagement_query = """
#                     SELECT call_date, COUNT(DISTINCT customer_id) AS total_engaged
#                     FROM (
#                         SELECT customer_id, DATE(call_time) AS call_date
#                         FROM debtcollectioncallhistory
#                         WHERE conclusion IS NOT NULL
#                 """
#                 params = []
#                 if from_date and to_date:
#                     engagement_query += " AND DATE(call_time) BETWEEN %s AND %s"
#                     params += [from_date, to_date]

#                 engagement_query += """
#                     ) AS sub
#                     GROUP BY call_date
#                     ORDER BY call_date
#                 """

#                 cursor.execute(engagement_query, params)
#                 engagement_data = [
#                     {
#                         "CreatedDate": row[0].strftime("%Y-%m-%d"),
#                         "total_engaged": row[1]
#                     }
#                     for row in cursor.fetchall()
#                 ]

#                 # ✅ 2. Dashboard Summary Data
#                 dashboard_query = """
#                     SELECT
#                         COUNT(DISTINCT CASE WHEN conclusion IS NULL THEN customer_id END) AS customers_to_connect,
#                         COUNT(DISTINCT CASE WHEN conclusion IS NOT NULL THEN customer_id END) AS customers_connected,
#                         COUNT(DISTINCT CASE WHEN LOWER(conclusion) = 'promised to pay' THEN customer_id END) AS promised_to_pay,
#                         COUNT(DISTINCT CASE WHEN LOWER(conclusion) = 'refuse to pay' THEN customer_id END) AS refuse_to_pay,
#                         COUNT(DISTINCT CASE WHEN LOWER(conclusion) = 'already paid' THEN customer_id END) AS already_paid,
#                         COUNT(DISTINCT CASE WHEN LOWER(conclusion) = 'wrong number' THEN customer_id END) AS wrong_number,
#                         COALESCE(SUM(promise_amount), 0) AS total_promised_amount
#                     FROM debtcollectioncallhistory
#                 """
#                 params = []
#                 if from_date and to_date:
#                     dashboard_query += " WHERE DATE(call_time) BETWEEN %s AND %s"
#                     params += [from_date, to_date]

#                 cursor.execute(dashboard_query, params)
#                 row = cursor.fetchone()

#                 dashboard_data = [{
#                     "customers_to_connect": row[0],
#                     "customers_connected": row[1],
#                     "promised_to_pay": row[2],
#                     "refuse_to_pay": row[3],
#                     "already_paid": row[4],
#                     "wrong_number": row[5],
#                     "total_promised_amount": float(row[6])
#                 }]

#             return Response({
#                 "engagement_data": engagement_data,
#                 "dashboard_data": dashboard_data
#             })

#         except Exception as e:
#             return Response(
#                 {"error": str(e)},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.db import connection
# import datetime


# class EngagementAPIView(APIView):
#     def get(self, request):
#         # Default: last 45 days if no date range provided
#         to_date = datetime.date.today()
#         from_date = to_date - datetime.timedelta(days=45)
#         return self._fetch_data(from_date, to_date)

#     def post(self, request):
#         from_date = request.data.get("from_date")
#         to_date = request.data.get("to_date")

#         if not from_date or not to_date:
#             return Response(
#                 {"error": "from_date and to_date are required."},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             from_date = datetime.datetime.strptime(from_date, "%Y-%m-%d").date()
#             to_date = datetime.datetime.strptime(to_date, "%Y-%m-%d").date()
#         except ValueError:
#             return Response(
#                 {"error": "Invalid date format. Use YYYY-MM-DD"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         return self._fetch_data(from_date, to_date)

#     def _fetch_data(self, from_date, to_date):
#         try:
#             with connection.cursor() as cursor:
#                 # ✅ Engagement Data
#                 cursor.execute("""
#                     SELECT DATE(call_time) AS created_date, COUNT(DISTINCT customer_id) AS total_engaged
#                     FROM debtcollectioncallhistory
#                     WHERE conclusion IS NOT NULL
#                     AND DATE(call_time) BETWEEN %s AND %s
#                     GROUP BY DATE(call_time)
#                     ORDER BY DATE(call_time)
#                 """, [from_date, to_date])

#                 engagement_data = [
#                     {
#                         "CreatedDate": row[0].strftime("%Y-%m-%d"),
#                         "total_engaged": row[1]
#                     }
#                     for row in cursor.fetchall()
#                 ]

#                 # ✅ Dashboard Data
#                 cursor.execute("""
#                     SELECT
#                         COUNT(DISTINCT CASE WHEN conclusion IS NULL THEN customer_id END) AS customers_to_connect,
#                         COUNT(DISTINCT CASE WHEN conclusion IS NOT NULL THEN customer_id END) AS customers_connected,
#                         COUNT(DISTINCT CASE WHEN LOWER(conclusion) = 'promised to pay' THEN customer_id END) AS promised_to_pay,
#                         COUNT(DISTINCT CASE WHEN LOWER(conclusion) = 'refuse to pay' THEN customer_id END) AS refuse_to_pay,
#                         COUNT(DISTINCT CASE WHEN LOWER(conclusion) = 'already paid' THEN customer_id END) AS already_paid,
#                         COUNT(DISTINCT CASE WHEN LOWER(conclusion) = 'wrong number' THEN customer_id END) AS wrong_number,
#                         COALESCE(SUM(promise_amount), 0)
#                     FROM debtcollectioncallhistory
#                     WHERE DATE(call_time) BETWEEN %s AND %s
#                 """, [from_date, to_date])

#                 row = cursor.fetchone()
#                 dashboard_data = [{
#                     "customers_to_connect": row[0],
#                     "customers_connected": row[1],
#                     "promised_to_pay": row[2],
#                     "refuse_to_pay": row[3],
#                     "already_paid": row[4],
#                     "wrong_number": row[5],
#                     "total_promised_amount": int(row[6]) if row[6] else 0
#                 }]

#             return Response({
#                 "engagement_data": engagement_data,
#                 "dashboard_data": dashboard_data
#             })

#         except Exception as e:
#             return Response(
#                 {"error": str(e)},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.db import connection
# import datetime


# class EngagementAPIView(APIView):
#     def get(self, request):
#         # Default date range: last 45 days
#         to_date = datetime.date.today()
#         from_date = to_date - datetime.timedelta(days=45)
#         return self._fetch_data(from_date, to_date)

#     def post(self, request):
#         from_date = request.data.get("from_date")
#         to_date = request.data.get("to_date")

#         if not from_date or not to_date:
#             return Response(
#                 {"error": "from_date and to_date are required."},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             from_date = datetime.datetime.strptime(from_date, "%Y-%m-%d").date()
#             to_date = datetime.datetime.strptime(to_date, "%Y-%m-%d").date()
#         except ValueError:
#             return Response(
#                 {"error": "Invalid date format. Use YYYY-MM-DD"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         return self._fetch_data(from_date, to_date)

#     def _fetch_data(self, from_date, to_date):
#         try:
#             with connection.cursor() as cursor:
#                 # ✅ Engagement Data
#                 cursor.execute("""
#                     SELECT DATE(call_time) AS created_date, COUNT(DISTINCT customer_id) AS total_engaged
#                     FROM debtcollectioncallhistory
#                     WHERE conclusion IS NOT NULL
#                     AND DATE(call_time) BETWEEN %s AND %s
#                     GROUP BY DATE(call_time)
#                     ORDER BY DATE(call_time)
#                 """, [from_date, to_date])

#                 engagement_data = [
#                     {
#                         "CreatedDate": row[0].strftime("%Y-%m-%d"),
#                         "total_engaged": row[1]
#                     }
#                     for row in cursor.fetchall()
#                 ]

#                 # ✅ Dashboard Data
#                 cursor.execute("""
#                     SELECT
#                         COUNT(DISTINCT CASE WHEN conclusion IS NULL THEN customer_id END) AS customers_to_connect,
#                         COUNT(DISTINCT CASE WHEN conclusion IS NOT NULL THEN customer_id END) AS customers_connected,
#                         COUNT(DISTINCT CASE WHEN LOWER(conclusion) = 'promised to pay' THEN customer_id END) AS promised_to_pay,
#                         COUNT(DISTINCT CASE WHEN LOWER(conclusion) = 'refuse to pay' THEN customer_id END) AS refuse_to_pay,
#                         COUNT(DISTINCT CASE WHEN LOWER(conclusion) = 'already paid' THEN customer_id END) AS already_paid,
#                         COUNT(DISTINCT CASE WHEN LOWER(conclusion) = 'wrong number' THEN customer_id END) AS wrong_number,
#                         COALESCE(SUM(promise_amount), 0) AS total_promised_amount
#                     FROM debtcollectioncallhistory
#                     WHERE DATE(call_time) BETWEEN %s AND %s
#                 """, [from_date, to_date])

#                 row = cursor.fetchone()
#                 dashboard_data = {
#                     "customers_to_connect": row[0],
#                     "customers_connected": row[1],
#                     "promised_to_pay": row[2],
#                     "refuse_to_pay": row[3],
#                     "already_paid": row[4],
#                     "wrong_number": row[5],
#                     "total_promised_amount": float(row[6]) if row[6] else 0
#                 }

#             return Response({
#                 "engagement_data": engagement_data,
#                 "dashboard_data": dashboard_data
#             })

#         except Exception as e:
#             return Response(
#                 {"error": str(e)},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.db import connection
# import datetime

# class EngagementAPIView(APIView):
#     def get(self, request):
#         # Default date range: last 45 days
#         to_date = datetime.date.today()
#         from_date = to_date - datetime.timedelta(days=45)
#         return self._fetch_data(from_date, to_date)

#     def post(self, request):
#         from_date = request.data.get("from_date")
#         to_date = request.data.get("to_date")

#         if not from_date or not to_date:
#             return Response(
#                 {"error": "from_date and to_date are required."},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             from_date = datetime.datetime.strptime(from_date, "%Y-%m-%d").date()
#             to_date = datetime.datetime.strptime(to_date, "%Y-%m-%d").date()
#         except ValueError:
#             return Response(
#                 {"error": "Invalid date format. Use YYYY-MM-DD"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         return self._fetch_data(from_date, to_date)

#     def _fetch_data(self, from_date, to_date):
#         try:
#             with connection.cursor() as cursor:
#                 # ✅ Engagement Data
#                 cursor.execute("""
#                     SELECT DATE(call_time) AS created_date, COUNT(DISTINCT customer_id) AS total_engaged
#                     FROM debtcollectioncallhistory
#                     WHERE conclusion IS NOT NULL
#                     AND DATE(call_time) BETWEEN %s AND %s
#                     GROUP BY DATE(call_time)
#                     ORDER BY DATE(call_time)
#                 """, [from_date, to_date])

#                 engagement_data = [
#                     {
#                         "CreatedDate": row[0].strftime("%Y-%m-%d"),
#                         "total_engaged": row[1]
#                     }
#                     for row in cursor.fetchall()
#                 ]

#                 # ✅ Dashboard Data
#                 cursor.execute("""
#                     SELECT
#                         COUNT(DISTINCT CASE WHEN conclusion IS NULL THEN customer_id END) AS customers_to_connect,
#                         COUNT(DISTINCT CASE WHEN conclusion IS NOT NULL THEN customer_id END) AS customers_connected,
#                         COUNT(DISTINCT CASE WHEN LOWER(conclusion) = 'promised to pay' THEN customer_id END) AS promised_to_pay,
#                         COUNT(DISTINCT CASE WHEN LOWER(conclusion) = 'refuse to pay' THEN customer_id END) AS refuse_to_pay,
#                         COUNT(DISTINCT CASE WHEN LOWER(conclusion) = 'already paid' THEN customer_id END) AS already_paid,
#                         COUNT(DISTINCT CASE WHEN LOWER(conclusion) = 'wrong number' THEN customer_id END) AS wrong_number,
#                         COALESCE(SUM(promise_amount), 0) AS total_promised_amount
#                     FROM debtcollectioncallhistory
#                     WHERE DATE(call_time) BETWEEN %s AND %s
#                 """, [from_date, to_date])

#                 row = cursor.fetchone()
#                 dashboard_data = [{
#                     "customers_to_connect": row[0],
#                     "customers_connected": row[1],
#                     "promised_to_pay": row[2],
#                     "refuse_to_pay": row[3],
#                     "already_paid": row[4],
#                     "wrong_number": row[5],
#                     "total_promised_amount": int(row[6]) if row[6] else 0
#                 }]

#             return Response({
#                 "engagement_data": engagement_data,
#                 "dashboard_data": dashboard_data
#             }, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response(
#                 {"error": str(e)},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.db import connection
# import datetime

# class EngagementAPIView(APIView):
#     def get(self, request):
#         from_date = "2025-04-01"
#         to_date = datetime.date.today().strftime('%Y-%m-%d')

#         return self._fetch_data(from_date, to_date)

#     def _fetch_data(self, from_date, to_date):
#         try:
#             with connection.cursor() as cursor:
#                 cursor.execute("SELECT * FROM get_dashboard_agrostar_v1(%s, %s);", [from_date, to_date])
#                 columns = [col[0] for col in cursor.description]
#                 results = [
#                     dict(zip(columns, row))
#                     for row in cursor.fetchall()
#                 ]

#             return Response(results, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response(
#                 {"error": str(e)},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
 
class EngagementAPIView(APIView):
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
