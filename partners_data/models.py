from django.db import models

# Create your models here.

class DebtCollectionCallQueue(models.Model):
    call_id = models.CharField(max_length=1000, primary_key=True)  # made it primary key
    phone_number = models.CharField(max_length=15, blank=True, default="")
    customer_name = models.CharField(max_length=200, blank=True)
    partner_company_name = models.CharField(max_length=200, blank=True)
    customer_id = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=50, blank=True)
    invoice_no = models.CharField(max_length=100, blank=True)
    product = models.CharField(max_length=200, blank=True)
    total_outstanding = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    ocp = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    invoice_overdue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    interest_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    call_connected = models.BooleanField(default=False, null=True)
    call_tried = models.IntegerField(default=0, null=True)
    calling_status = models.BooleanField(default=False)
    call_date = models.DateField(auto_now_add=True, null=True)
    last_payment_date = models.DateField(blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    reattempt_count = models.IntegerField(default=0)
    last_call_tried = models.DateTimeField(null=True, blank=True)
    offer = models.CharField(max_length=1000, blank=True, null=True)
    cd_valid_till = models.DateField(blank=True, null=True)
    cd_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_cd_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        managed = False
        db_table = 'debtcollectioncallqueue'


class DebtCollectionCallHistory(models.Model):
    phone_number = models.CharField(max_length=15, blank=True, default="")
    customer_name = models.CharField(max_length=200, blank=True)
    customer_id = models.CharField(max_length=200, blank=True)
    call_id = models.OneToOneField(  # Changed to OneToOneField to ensure uniqueness
        DebtCollectionCallQueue,
        on_delete=models.CASCADE,
        db_column='call_id',
        to_field='call_id'
    )
    call_time = models.DateTimeField(null=True)
    recording = models.FileField(upload_to="CallRecordings", null=True)
    call_duration = models.IntegerField(null=True)
    conclusion = models.CharField(max_length=512, default="Nothing", blank=True)
    call_summary_notes = models.CharField(max_length=1024, blank=True, default="")
    conversation_json = models.JSONField(default=dict)
    mode_of_payment = models.CharField(max_length=50, null=True)
    promise_date = models.DateField(null=True)
    promise_amount = models.FloatField(null=True, blank=True)
    disconnect_type = models.CharField(max_length=20, null=True)

    class Meta:
        managed = False
        db_table = 'debtcollectioncallhistory'


