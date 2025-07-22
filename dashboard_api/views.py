# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.db import connection
# import datetime

# class EngagementAPIView(APIView):
#     def get(self, request):
#         from_date = request.GET.get("from_date")
#         to_date = request.GET.get("to_date")

#         # Automatically set to_date to today's date if not provided
#         if not to_date:
#             to_date = datetime.date.today().strftime('%Y-%m-%d')

#         if not from_date:
#             return Response({"error": "from_date is required as a query parameter."},
#                             status=status.HTTP_400_BAD_REQUEST)

#         return self._fetch_data(from_date, to_date)

#     def post(self, request):
#         from_date = request.data.get("from_date")
#         to_date = request.data.get("to_date")

#         # Automatically set to_date to today's date if not provided
#         if not to_date:
#             to_date = datetime.date.today().strftime('%Y-%m-%d')

#         if not from_date:
#             return Response({"error": "from_date is required in request body."},
#                             status=status.HTTP_400_BAD_REQUEST)

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
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.db import connection

# class EngagementAPIView(APIView):
#     def get(self, request):
#         from_date = request.GET.get("from_date")
#         to_date = request.GET.get("to_date")

#         if not from_date or not to_date:
#             return Response({"error": "from_date and to_date are required as query parameters."},
#                             status=status.HTTP_400_BAD_REQUEST)

#         return self._fetch_data(from_date, to_date)

#     def post(self, request):
#         from_date = request.data.get("from_date")
#         to_date = request.data.get("to_date")

#         if not from_date or not to_date:
#             return Response({"error": "from_date and to_date are required in request body."},
#                             status=status.HTTP_400_BAD_REQUEST)

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
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
     

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
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




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