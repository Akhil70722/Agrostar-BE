# from rest_framework import serializers
# from .models import DebtCollectionCallQueue, DebtCollectionCallHistory


# class DebtCollectionQueueSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DebtCollectionCallQueue
#         fields = '__all__'


# class DebtCollectionHistorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DebtCollectionCallHistory
#         fields = '__all__'




# serializers.py

# from rest_framework import serializers
# from .models import DebtCollectionCallQueue, DebtCollectionCallHistory

# class FlatDebtCollectionSerializer(serializers.ModelSerializer):
#     conclusion = serializers.SerializerMethodField()
#     duration = serializers.SerializerMethodField()
#     recording_url = serializers.SerializerMethodField()

#     class Meta:
#         model = DebtCollectionCallQueue
#         fields = [
#             'call_id',
#             'customer_name',
#             'phone_number',
#             'call_connected',
#             'call_tried',
#             'call_date',
#             'reattempt_count',
#             'conclusion',
#             'duration',
#             'recording_url',
#         ]

#     def get_conclusion(self, obj):
#         history = getattr(obj, 'history', None)
#         return history.conclusion if history else None

#     def get_duration(self, obj):
#         history = getattr(obj, 'history', None)
#         return history.call_duration if history else None

#     def get_recording_url(self, obj):
#         history = getattr(obj, 'history', None)
#         return history.recording.url if history and history.recording else None

# from rest_framework import serializers
# from .models import DebtCollectionCallQueue, DebtCollectionCallHistory


# class DebtCollectionHistorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DebtCollectionCallHistory
#         fields = '__all__'


# class DebtCollectionQueueSerializer(serializers.ModelSerializer):
#     history = DebtCollectionHistorySerializer(source='debtcollectioncallhistory', read_only=True)

#     class Meta:
#         model = DebtCollectionCallQueue
#         fields = '__all__'

