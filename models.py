# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# Unable to inspect table '"9thJuneVinayanaBasedata_upto"'
# The error was: relation "9thJuneVinayanaBasedata_upto" does not exist
LINE 1: SELECT * FROM "9thJuneVinayanaBasedata_upto" LIMIT 1
                      ^


class AiRoute(models.Model):
    loanmstids = models.CharField(db_column='LoanMstIDS', blank=True, null=True)  # Field name made lowercase.
    fo_id = models.IntegerField(db_column='FO_ID', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    branchmstid = models.IntegerField(db_column='BranchMstID', blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.IntegerField(db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    route_name = models.CharField(db_column='Route_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AI_Route'


class Accountsummary(models.Model):
    branchmstid = models.ForeignKey('Branchmst', models.DO_NOTHING, db_column='BranchMstID')  # Field name made lowercase.
    bankmstid = models.ForeignKey('Bankmst', models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    customermstid = models.IntegerField(db_column='CustomerMstID')  # Field name made lowercase.
    customercode = models.CharField(db_column='CustomerCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mobilenumber = models.CharField(db_column='MobileNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateOfBirth', blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', max_length=255)  # Field name made lowercase.
    disbursementdate = models.DateField(db_column='DisbursementDate', blank=True, null=True)  # Field name made lowercase.
    disbursementamt = models.DecimalField(db_column='DisbursementAmt', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dpd = models.IntegerField(db_column='DPD', blank=True, null=True)  # Field name made lowercase.
    loanclassification = models.CharField(db_column='LoanClassification', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastpaymentdate = models.DateField(db_column='LastPaymentDate', blank=True, null=True)  # Field name made lowercase.
    lastcollectedamount = models.DecimalField(db_column='LastCollectedAmount', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    currentbalance = models.DecimalField(db_column='CurrentBalance', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    overdueamt = models.DecimalField(db_column='OverDueAmt', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    principleoutstanding = models.DecimalField(db_column='PrincipleOutstanding', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    interestoutstanding = models.DecimalField(db_column='InterestOutstanding', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totaloutstanding = models.DecimalField(db_column='TotalOutstanding', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    principlepending = models.DecimalField(db_column='PrinciplePending', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    interestpending = models.DecimalField(db_column='InterestPending', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totalpending = models.DecimalField(db_column='TotalPending', max_digits=18, decimal_places=2)  # Field name made lowercase.
    closingdate = models.DateField(db_column='ClosingDate', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    emiamount = models.DecimalField(db_column='EMIAmount', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nextemidate = models.DateField(db_column='NextEMIDate', blank=True, null=True)  # Field name made lowercase.
    loanmstid = models.ForeignKey('Loanmst', models.DO_NOTHING, db_column='LoanMstID')  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    branch_id = models.CharField(db_column='Branch_id', max_length=255, blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region_id = models.CharField(db_column='Region_id', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=255, blank=True, null=True)  # Field name made lowercase.
    state_id = models.CharField(db_column='State_id', max_length=255, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)  # Field name made lowercase.
    collectionofficerid = models.CharField(db_column='CollectionOfficerID', blank=True, null=True)  # Field name made lowercase.
    collectionofficername = models.CharField(db_column='CollectionOfficerName', blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(blank=True, null=True)
    groupname = models.CharField(blank=True, null=True)
    currentdpd = models.CharField(db_column='CurrentDPD', blank=True, null=True)  # Field name made lowercase.
    lastmonthdpd = models.CharField(db_column='LastMonthDPD', blank=True, null=True)  # Field name made lowercase.
    division = models.CharField(db_column='Division', max_length=100, blank=True, null=True)  # Field name made lowercase.
    district_id = models.CharField(db_column='District_id', max_length=50, blank=True, null=True)  # Field name made lowercase.
    co = models.CharField(db_column='CO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    circle_id = models.CharField(db_column='Circle_id', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zone = models.CharField(db_column='Zone', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zone_id = models.CharField(db_column='Zone_id', max_length=50, blank=True, null=True)  # Field name made lowercase.
    circle = models.CharField(db_column='Circle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    division_id = models.CharField(db_column='Division_id', max_length=50, blank=True, null=True)  # Field name made lowercase.
    co_id = models.CharField(db_column='CO_id', max_length=50, blank=True, null=True)  # Field name made lowercase.
    headoffice_id = models.CharField(db_column='HeadOffice_id', max_length=50, blank=True, null=True)  # Field name made lowercase.
    headoffice = models.CharField(db_column='HeadOffice', max_length=100, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=100, blank=True, null=True)  # Field name made lowercase.
    previousemidate = models.DateField(blank=True, null=True)
    isallocation = models.BooleanField(blank=True, null=True)
    first_time_arrear_clients = models.BooleanField(db_column='First_Time_Arrear_Clients', blank=True, null=True)  # Field name made lowercase.
    callinguserid = models.ForeignKey('Usermst', models.DO_NOTHING, db_column='CallingUserID', blank=True, null=True)  # Field name made lowercase.
    primarylanguage = models.CharField(blank=True, null=True)
    secondarylanguage = models.CharField(blank=True, null=True)
    originaldisbursementid = models.CharField(blank=True, null=True)
    promisedate = models.DateField(blank=True, null=True)
    customer_onboard_date = models.DateField(blank=True, null=True)
    loan_onboard_date = models.DateField(blank=True, null=True)
    pending_emis = models.CharField(blank=True, null=True)
    centername = models.CharField(blank=True, null=True)
    campaignmstid = models.IntegerField(db_column='CampaignMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountSummary'


class Accountsummaryhistory(models.Model):
    historyid = models.AutoField(db_column='HistoryID', primary_key=True)  # Field name made lowercase.
    branchmstid = models.IntegerField(db_column='BranchMstID')  # Field name made lowercase.
    bankmstid = models.IntegerField(db_column='BankMstID')  # Field name made lowercase.
    customermstid = models.IntegerField(db_column='CustomerMstID')  # Field name made lowercase.
    customercode = models.CharField(db_column='CustomerCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mobilenumber = models.CharField(db_column='MobileNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateOfBirth', blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', max_length=255)  # Field name made lowercase.
    disbursementdate = models.DateField(db_column='DisbursementDate', blank=True, null=True)  # Field name made lowercase.
    disbursementamt = models.DecimalField(db_column='DisbursementAmt', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dpd = models.IntegerField(db_column='DPD', blank=True, null=True)  # Field name made lowercase.
    loanclassification = models.CharField(db_column='LoanClassification', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastpaymentdate = models.DateField(db_column='LastPaymentDate', blank=True, null=True)  # Field name made lowercase.
    lastcollectedamount = models.DecimalField(db_column='LastCollectedAmount', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    currentbalance = models.DecimalField(db_column='CurrentBalance', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    overdueamt = models.DecimalField(db_column='OverDueAmt', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    principleoutstanding = models.DecimalField(db_column='PrincipleOutstanding', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    interestoutstanding = models.DecimalField(db_column='InterestOutstanding', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totaloutstanding = models.DecimalField(db_column='TotalOutstanding', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    principlepending = models.DecimalField(db_column='PrinciplePending', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    interestpending = models.DecimalField(db_column='InterestPending', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totalpending = models.DecimalField(db_column='TotalPending', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    closingdate = models.DateField(db_column='ClosingDate', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    emiamount = models.DecimalField(db_column='EMIAmount', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nextemidate = models.DateField(db_column='NextEMIDate', blank=True, null=True)  # Field name made lowercase.
    loanmstid = models.IntegerField(db_column='LoanMstID')  # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    branch_id = models.CharField(db_column='Branch_id', max_length=255, blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region_id = models.CharField(db_column='Region_id', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=255, blank=True, null=True)  # Field name made lowercase.
    state_id = models.CharField(db_column='State_id', max_length=255, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)  # Field name made lowercase.
    collectionofficerid = models.CharField(db_column='CollectionOfficerID', blank=True, null=True)  # Field name made lowercase.
    collectionofficername = models.CharField(db_column='CollectionOfficerName', blank=True, null=True)  # Field name made lowercase.
    groupid = models.IntegerField(blank=True, null=True)
    groupname = models.CharField(blank=True, null=True)
    currentdpd = models.IntegerField(db_column='CurrentDPD', blank=True, null=True)  # Field name made lowercase.
    lastmonthdpd = models.IntegerField(db_column='LastMonthDPD', blank=True, null=True)  # Field name made lowercase.
    as_created = models.DateField(blank=True, null=True)
    primarylanguage = models.CharField(blank=True, null=True)
    secondarylanguage = models.CharField(blank=True, null=True)
    originaldisbursementid = models.CharField(blank=True, null=True)
    customer_onboard_date = models.DateField(blank=True, null=True)
    loan_onboard_date = models.DateField(blank=True, null=True)
    centername = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AccountSummaryHistory'


class Activeconversation(models.Model):
    uuid = models.UUIDField(primary_key=True)
    user_id = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    last_updated = models.DateTimeField()
    conversation_status = models.CharField(max_length=20)
    form_data = models.TextField(blank=True, null=True)
    title = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ActiveConversation'


class Bmallocation(models.Model):
    bmallocationid = models.AutoField(db_column='BMAllocationID', primary_key=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey('Bankmst', models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    branchmstid = models.ForeignKey('Branchmst', models.DO_NOTHING, db_column='BranchMstID')  # Field name made lowercase.
    customermstid = models.ForeignKey('Customermst', models.DO_NOTHING, db_column='CustomerMstID')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    contactnumber = models.CharField(db_column='ContactNumber', max_length=15)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=255)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=100)  # Field name made lowercase.
    isaction = models.BooleanField(db_column='IsAction')  # Field name made lowercase.
    lngmstid = models.ForeignKey('Languagemst', models.DO_NOTHING, db_column='LngMstID')  # Field name made lowercase.
    loanmstid = models.ForeignKey('Loanmst', models.DO_NOTHING, db_column='LoanMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BMAllocation'


class Bankmst(models.Model):
    bankmstid = models.AutoField(db_column='BankMstID', primary_key=True)  # Field name made lowercase.
    onboardingdate = models.DateField(db_column='OnBoardingDate', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    updateddate = models.DateField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    subscriptionid = models.IntegerField(db_column='SubscriptionID', blank=True, null=True)  # Field name made lowercase.
    subscriptiontype = models.CharField(db_column='SubscriptionType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=255)  # Field name made lowercase.
    whatsapp = models.BooleanField(db_column='WhatsApp', blank=True, null=True)  # Field name made lowercase.
    voicebot = models.BooleanField(db_column='VoiceBot', blank=True, null=True)  # Field name made lowercase.
    blaster = models.BooleanField(db_column='Blaster', blank=True, null=True)  # Field name made lowercase.
    ivr = models.BooleanField(db_column='IVR', blank=True, null=True)  # Field name made lowercase.
    sms = models.BooleanField(db_column='SMS', blank=True, null=True)  # Field name made lowercase.
    is_upi = models.BooleanField(db_column='Is_UPI', blank=True, null=True)  # Field name made lowercase.
    key_id = models.CharField(db_column='Key_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    secret_key = models.CharField(db_column='Secret_Key', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_recipt = models.BooleanField(db_column='Is_recipt', blank=True, null=True)  # Field name made lowercase.
    geolocation = models.BooleanField(db_column='Geolocation', blank=True, null=True)  # Field name made lowercase.
    whatsappservice = models.CharField(db_column='WhatsappService', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bank_details = models.JSONField(db_column='Bank_Details', blank=True, null=True)  # Field name made lowercase.
    claim_period = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BankMst'


class Blasterhistory(models.Model):
    blasterhistoryid = models.AutoField(db_column='BlasterHistoryID', primary_key=True)  # Field name made lowercase.
    blasterqueueid = models.IntegerField(db_column='BlasterQueueID', unique=True, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    branchmstid = models.ForeignKey('Branchmst', models.DO_NOTHING, db_column='BranchMstID')  # Field name made lowercase.
    loanmstid = models.ForeignKey('Loanmst', models.DO_NOTHING, db_column='LoanMstID')  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID')  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', max_length=255)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='ContactNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255)  # Field name made lowercase.
    next_emi_amount = models.DecimalField(db_column='Next_EMI_Amount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    next_emi_date = models.DateField(db_column='Next_EMI_Date', blank=True, null=True)  # Field name made lowercase.
    total_collection = models.DecimalField(db_column='Total_Collection', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    latest_collecteddate = models.DateField(db_column='Latest_CollectedDate', blank=True, null=True)  # Field name made lowercase.
    latest_collectedamt = models.DecimalField(db_column='Latest_CollectedAmt', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    issent = models.BooleanField(db_column='IsSent', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    identifier = models.CharField(db_column='Identifier', max_length=255, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', blank=True, null=True)  # Field name made lowercase.
    callid = models.CharField(db_column='CallID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    recording = models.CharField(db_column='Recording', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conversation_json = models.JSONField(db_column='Conversation_json', blank=True, null=True)  # Field name made lowercase.
    conclusion = models.CharField(db_column='Conclusion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    calltried = models.IntegerField(db_column='CallTried', blank=True, null=True)  # Field name made lowercase.
    callduration = models.FloatField(db_column='CallDuration', blank=True, null=True)  # Field name made lowercase.
    callconnected = models.BooleanField(db_column='CallConnected', blank=True, null=True)  # Field name made lowercase.
    slot = models.CharField(db_column='Slot', blank=True, null=True)  # Field name made lowercase.
    basedon = models.CharField(db_column='BasedOn', blank=True, null=True)  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    customercode = models.CharField(db_column='CustomerCode', blank=True, null=True)  # Field name made lowercase.
    flowid = models.IntegerField(db_column='FlowID', blank=True, null=True)  # Field name made lowercase.
    blastertemplatemappingid = models.IntegerField(db_column='BlasterTemplateMappingID', blank=True, null=True)  # Field name made lowercase.
    isdelivered = models.BooleanField(db_column='IsDelivered', blank=True, null=True)  # Field name made lowercase.
    isread = models.BooleanField(db_column='IsRead', blank=True, null=True)  # Field name made lowercase.
    isresponded = models.BooleanField(db_column='IsResponded', blank=True, null=True)  # Field name made lowercase.
    overdueamt = models.DecimalField(db_column='OverDueAmt', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    alternativemobilenumber = models.CharField(db_column='AlternativeMobileNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    secondarycustmstid = models.IntegerField(db_column='SecondaryCustMstID', blank=True, null=True)  # Field name made lowercase.
    applicantname = models.CharField(db_column='ApplicantName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coapplicantcontact = models.CharField(db_column='CoApplicantContact', max_length=20, blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', blank=True, null=True)  # Field name made lowercase.
    campaignmstid = models.IntegerField(db_column='CampaignMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BlasterHistory'


class Blasterqueue(models.Model):
    blasterqueueid = models.AutoField(db_column='BlasterQueueID', primary_key=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    branchmstid = models.ForeignKey('Branchmst', models.DO_NOTHING, db_column='BranchMstID')  # Field name made lowercase.
    loanmstid = models.ForeignKey('Loanmst', models.DO_NOTHING, db_column='LoanMstID')  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', max_length=50)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=100)  # Field name made lowercase.
    customercode = models.CharField(db_column='CustomerCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=255)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    slot = models.CharField(db_column='Slot', max_length=255, blank=True, null=True)  # Field name made lowercase.
    calltried = models.IntegerField(db_column='CallTried', blank=True, null=True)  # Field name made lowercase.
    callconnected = models.BooleanField(db_column='CallConnected', blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    basedon = models.CharField(db_column='BasedOn', blank=True, null=True)  # Field name made lowercase.
    commflowid = models.ForeignKey('Commflow', models.DO_NOTHING, db_column='CommFlowID', blank=True, null=True)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='ContactNumber', blank=True, null=True)  # Field name made lowercase.
    callduration = models.FloatField(db_column='CallDuration', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', blank=True, null=True)  # Field name made lowercase.
    flowid = models.IntegerField(db_column='FlowID', blank=True, null=True)  # Field name made lowercase.
    blastertemplatemappingid = models.IntegerField(db_column='BlasterTemplateMappingID', blank=True, null=True)  # Field name made lowercase.
    total_collection = models.IntegerField(db_column='Total_Collection', blank=True, null=True)  # Field name made lowercase.
    latest_collecteddate = models.DateField(db_column='Latest_CollectedDate', blank=True, null=True)  # Field name made lowercase.
    latest_collectedamt = models.IntegerField(db_column='Latest_CollectedAmt', blank=True, null=True)  # Field name made lowercase.
    next_emi_amount = models.IntegerField(db_column='Next_EMI_Amount', blank=True, null=True)  # Field name made lowercase.
    next_emi_date = models.DateField(db_column='Next_EMI_Date', blank=True, null=True)  # Field name made lowercase.
    identifier = models.CharField(db_column='Identifier', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    overdueamt = models.DecimalField(db_column='OverDueAmt', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    alternativemobilenumber = models.CharField(db_column='AlternativeMobileNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    secondarycustmstid = models.IntegerField(db_column='SecondaryCustMstID', blank=True, null=True)  # Field name made lowercase.
    applicantname = models.CharField(db_column='ApplicantName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coapplicantcontact = models.CharField(db_column='CoApplicantContact', max_length=20, blank=True, null=True)  # Field name made lowercase.
    campaignmstid = models.IntegerField(db_column='CampaignMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BlasterQueue'


class Blastertemplatemapping(models.Model):
    blastertemplatemappingid = models.AutoField(db_column='BlasterTemplateMappingID', primary_key=True)  # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
    templatename = models.CharField(db_column='TemplateName', max_length=255)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    lngmstid = models.ForeignKey('Languagemst', models.DO_NOTHING, db_column='LngMstID')  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isadmincreated = models.BooleanField(db_column='IsAdminCreated')  # Field name made lowercase.
    recordingurl = models.CharField(db_column='RecordingURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    templatebody = models.CharField(db_column='TemplateBody', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BlasterTemplateMapping'


class Blasterusertemplate(models.Model):
    blasterusertemplateid = models.AutoField(db_column='BlasterUserTemplateID', primary_key=True)  # Field name made lowercase.
    templatename = models.CharField(db_column='TemplateName', max_length=255)  # Field name made lowercase.
    templatebody = models.TextField(db_column='TemplateBody', blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    employeemstid = models.ForeignKey('Employeemst', models.DO_NOTHING, db_column='EmployeeMstID', blank=True, null=True)  # Field name made lowercase.
    variablenumber = models.IntegerField(db_column='VariableNumber')  # Field name made lowercase.
    variablefield = models.CharField(db_column='VariableField', max_length=255)  # Field name made lowercase.
    blastertemplatemappingid = models.ForeignKey(Blastertemplatemapping, models.DO_NOTHING, db_column='BlasterTemplateMappingID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BlasterUserTemplate'


class Branchmst(models.Model):
    branchmstid = models.AutoField(db_column='BranchMstID', primary_key=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=255)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    updateddate = models.DateField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    lngmstid = models.ForeignKey('Languagemst', models.DO_NOTHING, db_column='LngMstID', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=100, blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BranchMst'


class Callinghistory(models.Model):
    callinghistoryid = models.AutoField(db_column='CallingHistoryID', primary_key=True)  # Field name made lowercase.
    callingqueueid = models.IntegerField(db_column='CallingQueueID')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    branchmstid = models.ForeignKey(Branchmst, models.DO_NOTHING, db_column='BranchMstID')  # Field name made lowercase.
    loanmstid = models.ForeignKey('Loanmst', models.DO_NOTHING, db_column='LoanMstID')  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID')  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', max_length=255)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='ContactNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255)  # Field name made lowercase.
    next_emi_amount = models.DecimalField(db_column='Next_EMI_Amount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    next_emi_date = models.DateField(db_column='Next_EMI_Date', blank=True, null=True)  # Field name made lowercase.
    total_collection = models.DecimalField(db_column='Total_Collection', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    latest_collecteddate = models.DateField(db_column='Latest_CollectedDate', blank=True, null=True)  # Field name made lowercase.
    latest_collectedamt = models.DecimalField(db_column='Latest_CollectedAmt', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    issent = models.BooleanField(db_column='IsSent', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    identifier = models.CharField(db_column='Identifier', max_length=255, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', blank=True, null=True)  # Field name made lowercase.
    callid = models.CharField(db_column='CallID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    recording = models.CharField(db_column='Recording', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conversation_json = models.JSONField(db_column='Conversation_json', blank=True, null=True)  # Field name made lowercase.
    conclusion = models.CharField(db_column='Conclusion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    calltried = models.IntegerField(db_column='CallTried', blank=True, null=True)  # Field name made lowercase.
    callduration = models.FloatField(db_column='CallDuration', blank=True, null=True)  # Field name made lowercase.
    callconnected = models.BooleanField(db_column='CallConnected', blank=True, null=True)  # Field name made lowercase.
    slot = models.CharField(db_column='Slot', blank=True, null=True)  # Field name made lowercase.
    basedon = models.CharField(db_column='BasedOn', blank=True, null=True)  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    customercode = models.CharField(db_column='CustomerCode', blank=True, null=True)  # Field name made lowercase.
    flowid = models.IntegerField(db_column='FlowID', blank=True, null=True)  # Field name made lowercase.
    callingtemplatemappingid = models.IntegerField(db_column='CallingTemplateMappingID', blank=True, null=True)  # Field name made lowercase.
    isdelivered = models.BooleanField(db_column='IsDelivered', blank=True, null=True)  # Field name made lowercase.
    isread = models.BooleanField(db_column='IsRead', blank=True, null=True)  # Field name made lowercase.
    isresponded = models.BooleanField(db_column='IsResponded', blank=True, null=True)  # Field name made lowercase.
    overdueamt = models.DecimalField(db_column='OverDueAmt', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    alternativemobilenumber = models.CharField(db_column='AlternativeMobileNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    secondarycustmstid = models.IntegerField(db_column='SecondaryCustMstID', blank=True, null=True)  # Field name made lowercase.
    applicantname = models.CharField(db_column='ApplicantName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coapplicantcontact = models.CharField(db_column='CoApplicantContact', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CallingHistory'


class Callingqueue(models.Model):
    callingqueueid = models.AutoField(db_column='CallingQueueID', primary_key=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    branchmstid = models.ForeignKey(Branchmst, models.DO_NOTHING, db_column='BranchMstID')  # Field name made lowercase.
    loanmstid = models.ForeignKey('Loanmst', models.DO_NOTHING, db_column='LoanMstID')  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', max_length=50)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=100)  # Field name made lowercase.
    customercode = models.CharField(db_column='CustomerCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=255)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    slot = models.CharField(db_column='Slot', max_length=255, blank=True, null=True)  # Field name made lowercase.
    calltried = models.IntegerField(db_column='CallTried', blank=True, null=True)  # Field name made lowercase.
    callconnected = models.BooleanField(db_column='CallConnected', blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    basedon = models.CharField(db_column='BasedOn', blank=True, null=True)  # Field name made lowercase.
    commflowid = models.ForeignKey('Commflow', models.DO_NOTHING, db_column='CommFlowID', blank=True, null=True)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='ContactNumber', blank=True, null=True)  # Field name made lowercase.
    callduration = models.FloatField(db_column='CallDuration', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', blank=True, null=True)  # Field name made lowercase.
    flowid = models.IntegerField(db_column='FlowID', blank=True, null=True)  # Field name made lowercase.
    callingtemplatemappingid = models.IntegerField(db_column='CallingTemplateMappingID', blank=True, null=True)  # Field name made lowercase.
    total_collection = models.IntegerField(db_column='Total_Collection', blank=True, null=True)  # Field name made lowercase.
    latest_collecteddate = models.DateField(db_column='Latest_CollectedDate', blank=True, null=True)  # Field name made lowercase.
    latest_collectedamt = models.IntegerField(db_column='Latest_CollectedAmt', blank=True, null=True)  # Field name made lowercase.
    next_emi_amount = models.IntegerField(db_column='Next_EMI_Amount', blank=True, null=True)  # Field name made lowercase.
    next_emi_date = models.DateField(db_column='Next_EMI_Date', blank=True, null=True)  # Field name made lowercase.
    identifier = models.CharField(db_column='Identifier', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    overdueamt = models.DecimalField(db_column='OverDueAmt', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    alternativemobilenumber = models.CharField(db_column='AlternativeMobileNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    secondarycustmstid = models.IntegerField(db_column='SecondaryCustMstID', blank=True, null=True)  # Field name made lowercase.
    applicantname = models.CharField(db_column='ApplicantName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coapplicantcontact = models.CharField(db_column='CoApplicantContact', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CallingQueue'


class Callingtemplatemapping(models.Model):
    callingtemplatemappingid = models.AutoField(db_column='CallingTemplateMappingID', primary_key=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    templatename = models.CharField(db_column='TemplateName', max_length=255)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    isadmincreated = models.BooleanField(db_column='IsAdminCreated', blank=True, null=True)  # Field name made lowercase.
    recordingurl = models.CharField(db_column='RecordingURL', max_length=512, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    templatebody = models.TextField(db_column='TemplateBody', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CallingTemplateMapping'


class Callingusertemplate(models.Model):
    callingusertemplateid = models.AutoField(db_column='CallingUserTemplateID', primary_key=True)  # Field name made lowercase.
    templatename = models.CharField(db_column='TemplateName', max_length=255)  # Field name made lowercase.
    templatebody = models.TextField(db_column='TemplateBody', blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    employeemstid = models.ForeignKey('Employeemst', models.DO_NOTHING, db_column='EmployeeMstID', blank=True, null=True)  # Field name made lowercase.
    callingtemplatemappingid = models.ForeignKey(Callingtemplatemapping, models.DO_NOTHING, db_column='CallingTemplateMappingID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CallingUserTemplate'


class Campaignmst(models.Model):
    campaignmstid = models.AutoField(db_column='CampaignMstID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    priority = models.CharField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    campaigntype = models.CharField(db_column='CampaignType', blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CampaignMst'
        unique_together = (('name', 'bankmstid'),)


class Coappmst(models.Model):
    coappmstid = models.AutoField(db_column='CoAppMstID', primary_key=True)  # Field name made lowercase.
    loanmstid = models.ForeignKey('Loanmst', models.DO_NOTHING, db_column='LoanMstID', blank=True, null=True)  # Field name made lowercase.
    secondarycustmstid = models.ForeignKey('Secondarycustmst', models.DO_NOTHING, db_column='SecondaryCustMstID', blank=True, null=True)  # Field name made lowercase.
    coapptype = models.CharField(db_column='CoAppType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    inserted_on = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CoAppMst'


class Collectionfile(models.Model):
    collectionfileid = models.AutoField(db_column='CollectionFileID', primary_key=True)  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', max_length=255)  # Field name made lowercase.
    principlecollected = models.DecimalField(db_column='PrincipleCollected', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    interestcollected = models.DecimalField(db_column='InterestCollected', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    inststartdate = models.DateField(db_column='InstStartDate', blank=True, null=True)  # Field name made lowercase.
    collectedamount = models.DecimalField(db_column='CollectedAmount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    collectiondate = models.DateField(db_column='CollectionDate', blank=True, null=True)  # Field name made lowercase.
    bmid = models.IntegerField(db_column='BMID', blank=True, null=True)  # Field name made lowercase.
    pos = models.CharField(db_column='POS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.IntegerField(db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    branchmstid = models.IntegerField(db_column='BranchMstID', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', blank=True, null=True)  # Field name made lowercase.
    customerid = models.CharField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    transactionnumber = models.CharField(db_column='TransactionNumber', blank=True, null=True)  # Field name made lowercase.
    inserted_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CollectionFile'


class Collectionofficerallocation(models.Model):
    collectionofficerallocationid = models.AutoField(db_column='CollectionOfficerAllocationID', primary_key=True)  # Field name made lowercase.
    bankmstid = models.IntegerField(db_column='BankMstID')  # Field name made lowercase.
    branchmstid = models.IntegerField(db_column='BranchMstID')  # Field name made lowercase.
    customermstid = models.IntegerField(db_column='CustomerMstID')  # Field name made lowercase.
    loanmstid = models.IntegerField(db_column='LoanMstID', blank=True, null=True)  # Field name made lowercase.
    collectionofficerid = models.CharField(db_column='CollectionOfficerID')  # Field name made lowercase.
    collectionofficername = models.CharField(db_column='CollectionOfficerName', max_length=255)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='ContactNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isaction = models.BooleanField(db_column='IsAction', blank=True, null=True)  # Field name made lowercase.
    lngmstid = models.ForeignKey('Languagemst', models.DO_NOTHING, db_column='LngMstID', blank=True, null=True)  # Field name made lowercase.
    basedon = models.CharField(db_column='BasedOn', blank=True, null=True)  # Field name made lowercase.
    status = models.BooleanField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CollectionOfficerAllocation'


class Commflow(models.Model):
    commflowid = models.AutoField(db_column='CommFlowID', primary_key=True)  # Field name made lowercase.
    communicationtype = models.CharField(db_column='CommunicationType', max_length=100)  # Field name made lowercase.
    commflowmstid = models.ForeignKey('Commflowmst', models.DO_NOTHING, db_column='CommFlowMstID')  # Field name made lowercase.
    days = models.CharField(db_column='Days', blank=True, null=True)  # Field name made lowercase.
    beforeafter = models.CharField(db_column='BeforeAfter', max_length=10)  # Field name made lowercase.
    flowid = models.IntegerField(db_column='FlowID', blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    basedon = models.CharField(db_column='BasedOn', blank=True, null=True)  # Field name made lowercase.
    basedontable = models.CharField(db_column='BasedOnTable', blank=True, null=True)  # Field name made lowercase.
    templateid = models.CharField(db_column='TemplateID', blank=True, null=True)  # Field name made lowercase.
    campaignmstid = models.ForeignKey(Campaignmst, models.DO_NOTHING, db_column='CampaignMstID', blank=True, null=True)  # Field name made lowercase.
    campaign_type = models.CharField(blank=True, null=True)
    periodtype = models.CharField(db_column='PeriodType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    frequency = models.TextField(blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    interval = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    until = models.DateField(blank=True, null=True)
    bysetpos = models.TextField(blank=True, null=True)
    bymonth = models.TextField(blank=True, null=True)
    bymonthday = models.TextField(blank=True, null=True)
    byyearday = models.TextField(blank=True, null=True)
    byweekno = models.TextField(blank=True, null=True)
    byweekday = models.TextField(blank=True, null=True)
    weekstart = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CommFlow'


class Commflowmst(models.Model):
    commflowmstid = models.AutoField(db_column='CommFlowMstID', primary_key=True)  # Field name made lowercase.
    columnname = models.CharField(db_column='ColumnName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    basedontable = models.CharField(db_column='BasedOnTable', blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=255)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50)  # Field name made lowercase.
    basedoncolumn = models.CharField(db_column='BasedOnColumn', max_length=255, blank=True, null=True)  # Field name made lowercase.
    flowname = models.CharField(db_column='FlowName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CommFlowMst'


class Communicationmapping(models.Model):
    bankmstid = models.IntegerField(db_column='BankMstID')  # Field name made lowercase.
    whatsapp = models.BooleanField(db_column='WhatsApp', blank=True, null=True)  # Field name made lowercase.
    voicebot = models.BooleanField(db_column='VoiceBot', blank=True, null=True)  # Field name made lowercase.
    blaster = models.BooleanField(db_column='Blaster', blank=True, null=True)  # Field name made lowercase.
    ivr = models.BooleanField(db_column='IVR', blank=True, null=True)  # Field name made lowercase.
    sms = models.BooleanField(db_column='SMS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CommunicationMapping'


class Communicationqueue(models.Model):
    communicationqueueid = models.AutoField(db_column='CommunicationQueueID', primary_key=True)  # Field name made lowercase.
    branchmstid = models.ForeignKey(Branchmst, models.DO_NOTHING, db_column='BranchMstID', blank=True, null=True)  # Field name made lowercase.
    iswhatsapp = models.BooleanField(db_column='IsWhatsApp', blank=True, null=True)  # Field name made lowercase.
    isblaster = models.BooleanField(db_column='IsBlaster', blank=True, null=True)  # Field name made lowercase.
    isvoicebot = models.BooleanField(db_column='IsVoiceBot', blank=True, null=True)  # Field name made lowercase.
    issms = models.BooleanField(db_column='IsSMS', blank=True, null=True)  # Field name made lowercase.
    slot = models.CharField(db_column='Slot', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    loanmstid = models.ForeignKey('Loanmst', models.DO_NOTHING, db_column='LoanMstID', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    isivr = models.BooleanField(db_column='IsIVR', blank=True, null=True)  # Field name made lowercase.
    basedondate = models.CharField(db_column='BasedOnDate', blank=True, null=True)  # Field name made lowercase.
    bmallocate = models.CharField(db_column='BMAllocate', blank=True, null=True)  # Field name made lowercase.
    collectionofficerallocate = models.CharField(db_column='CollectionOfficerAllocate', blank=True, null=True)  # Field name made lowercase.
    campaignmstid = models.IntegerField(db_column='CampaignMstID', blank=True, null=True)  # Field name made lowercase.
    flowid = models.IntegerField(db_column='FlowID', blank=True, null=True)  # Field name made lowercase.
    secondarycustmstid = models.IntegerField(db_column='SecondaryCustMstID', blank=True, null=True)  # Field name made lowercase.
    callinguserid = models.IntegerField(db_column='CallingUserID', blank=True, null=True)  # Field name made lowercase.
    iscalling = models.BooleanField(db_column='IsCalling', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CommunicationQueue'


class Componentmst(models.Model):
    bankmstid = models.IntegerField(db_column='BankMstID')  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=100)  # Field name made lowercase.
    screens = models.JSONField(db_column='Screens', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ComponentMst'


class Conversationhistory(models.Model):
    uuid = models.UUIDField(primary_key=True)
    user_id = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    completed_at = models.DateTimeField()
    form_data = models.TextField(blank=True, null=True)
    full_conversation = models.TextField()
    title = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ConversationHistory'


class Conversationmessage(models.Model):
    conversation = models.ForeignKey(Activeconversation, models.DO_NOTHING)
    user_message = models.TextField()
    ai_response = models.TextField()
    created_at = models.DateTimeField()
    is_edited = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ConversationMessage'


class Customermst(models.Model):
    customermstid = models.AutoField(db_column='CustomerMstID', primary_key=True)  # Field name made lowercase.
    branchmstid = models.ForeignKey(Branchmst, models.DO_NOTHING, db_column='BranchMstID', blank=True, null=True)  # Field name made lowercase.
    customerid = models.CharField(db_column='CustomerID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customercode = models.CharField(db_column='CustomerCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mobilenumber = models.CharField(db_column='MobileNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateOfBirth', blank=True, null=True)  # Field name made lowercase.
    isdeath = models.BooleanField(db_column='IsDeath', blank=True, null=True)  # Field name made lowercase.
    deathdate = models.DateField(db_column='DeathDate', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    updateddate = models.DateField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=255, blank=True, null=True)  # Field name made lowercase.
    panno = models.CharField(db_column='PanNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pincode = models.CharField(db_column='Pincode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    customeraddress = models.TextField(db_column='CustomerAddress', blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    inserted_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CustomerMst'


class Dndhistory(models.Model):
    dndhistoryid = models.AutoField(db_column='DNDHistoryID', primary_key=True)  # Field name made lowercase.
    loanmstid = models.ForeignKey('Loanmst', models.DO_NOTHING, db_column='LoanMstID')  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    insertiondate = models.DateTimeField(db_column='InsertionDate', blank=True, null=True)  # Field name made lowercase.
    deletiondate = models.DateTimeField(db_column='DeletionDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DNDHistory'


class Dpdcategory(models.Model):
    dpdcategoryid = models.AutoField(db_column='DPDCategoryID', primary_key=True)  # Field name made lowercase.
    rangestart = models.IntegerField(db_column='RangeStart')  # Field name made lowercase.
    rangeend = models.IntegerField(db_column='RangeEnd')  # Field name made lowercase.
    categorylabel = models.CharField(db_column='CategoryLabel', max_length=255)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn')  # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='UpdatedOn', blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    deletedon = models.DateTimeField(db_column='DeletedOn', blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DPDCategory'


class Designationmst(models.Model):
    designationmstid = models.AutoField(db_column='DesignationMstID', primary_key=True)  # Field name made lowercase.
    designationname = models.CharField(db_column='DesignationName', max_length=255)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DesignationMst'


class Dialer(models.Model):
    dialerid = models.AutoField(db_column='DialerID', primary_key=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    branchmstid = models.ForeignKey(Branchmst, models.DO_NOTHING, db_column='BranchMstID')  # Field name made lowercase.
    loanmstid = models.ForeignKey('Loanmst', models.DO_NOTHING, db_column='LoanMstID')  # Field name made lowercase.
    call_id = models.CharField(db_column='Call_ID', max_length=50)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    recordingurl = models.TextField(db_column='RecordingURL')  # Field name made lowercase.
    customermstid = models.IntegerField(db_column='CustomerMstID', blank=True, null=True)  # Field name made lowercase.
    initiatingnumber = models.CharField(db_column='InitiatingNumber', blank=True, null=True)  # Field name made lowercase.
    campaignmstid = models.IntegerField(db_column='CampaignMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dialer'


class Disbursementfile(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customerid = models.CharField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dataopen = models.DateField(db_column='DATAOPEN', blank=True, null=True)  # Field name made lowercase.
    dateclose = models.DateField(db_column='DateClose', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    disburseamount = models.DecimalField(db_column='DisburseAmount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rateofinterest = models.DecimalField(db_column='RateOfInterest', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    repaymenttenure = models.IntegerField(db_column='RepaymentTenure', blank=True, null=True)  # Field name made lowercase.
    emiamount = models.DecimalField(db_column='EMIAmount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paymentfrequency = models.IntegerField(db_column='PaymentFrequency', blank=True, null=True)  # Field name made lowercase.
    numberofdayspastdue = models.IntegerField(db_column='NumberOfDaysPastDue', blank=True, null=True)  # Field name made lowercase.
    buid = models.IntegerField(db_column='BUID', blank=True, null=True)  # Field name made lowercase.
    bu_name = models.CharField(db_column='BU NAME', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bmid = models.IntegerField(db_column='BMID', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mobile_no = models.CharField(db_column='Mobile No', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    alternate_mobile_no = models.CharField(db_column='Alternate Mobile No', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    panno = models.CharField(db_column='PANNo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    pincode = models.CharField(db_column='Pincode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    inststartdate = models.DateField(db_column='InstStartDate', blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateOfBirth', blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    collectionofficerid = models.CharField(db_column='CollectionOfficerID', blank=True, null=True)  # Field name made lowercase.
    collectionofficername = models.CharField(db_column='CollectionOfficerName', blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', blank=True, null=True)  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    customercode = models.CharField(db_column='CustomerCode', blank=True, null=True)  # Field name made lowercase.
    dnd = models.BooleanField(db_column='DND', blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(blank=True, null=True)
    groupname = models.CharField(blank=True, null=True)
    datainsertedon = models.DateField(blank=True, null=True)
    overdueamt = models.IntegerField(blank=True, null=True)
    productname = models.CharField(max_length=255, blank=True, null=True)
    extracolumn1 = models.CharField(blank=True, null=True)
    extracolumn2 = models.CharField(blank=True, null=True)
    extracolumn3 = models.CharField(blank=True, null=True)
    extracolumn4 = models.CharField(blank=True, null=True)
    extracolumn5 = models.CharField(blank=True, null=True)
    currentbalance = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    first_time_arrear_clients = models.BooleanField(db_column='First_Time_Arrear_Clients', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DisbursementFile'
        unique_together = (('customerid', 'disbursementid', 'bankmstid', 'datainsertedon'),)


class Employeeaccess(models.Model):
    employeeaccessid = models.AutoField(db_column='EmployeeAccessID', primary_key=True)  # Field name made lowercase.
    employeemstid = models.ForeignKey('Employeemst', models.DO_NOTHING, db_column='EmployeeMstID')  # Field name made lowercase.
    buid = models.ForeignKey('Geographymst', models.DO_NOTHING, db_column='BUID')  # Field name made lowercase.
    designationid = models.ForeignKey(Designationmst, models.DO_NOTHING, db_column='DesignationID')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmployeeAccess'


class Employeemst(models.Model):
    employeemstid = models.AutoField(db_column='EmployeeMstID', primary_key=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    usercode = models.CharField(db_column='UserCode', max_length=50)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.
    employeename = models.CharField(db_column='EmployeeName', max_length=255)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=20)  # Field name made lowercase.
    designationid = models.ForeignKey(Designationmst, models.DO_NOTHING, db_column='DesignationID')  # Field name made lowercase.
    reportingid = models.IntegerField(db_column='ReportingID', blank=True, null=True)  # Field name made lowercase.
    buid = models.ForeignKey('Geographymst', models.DO_NOTHING, db_column='BUID')  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmployeeMst'


class Filtermst(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    commflowid = models.ForeignKey(Commflow, models.DO_NOTHING, db_column='CommFlowID', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    filtersid = models.ForeignKey('Filters', models.DO_NOTHING, db_column='FiltersID', blank=True, null=True)  # Field name made lowercase.
    campaignmstid = models.ForeignKey(Campaignmst, models.DO_NOTHING, db_column='CampaignMstID', blank=True, null=True)  # Field name made lowercase.
    commflowmstid = models.ForeignKey(Commflowmst, models.DO_NOTHING, db_column='CommFlowMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FilterMst'


class Filters(models.Model):
    filtersid = models.AutoField(db_column='FiltersID', primary_key=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    column = models.CharField(db_column='Column', max_length=255)  # Field name made lowercase.
    comparison = models.CharField(db_column='Comparison', max_length=50)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Filters'


class Geographymst(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    bucode = models.CharField(db_column='BUCode', max_length=50)  # Field name made lowercase.
    buname = models.CharField(db_column='BUName', max_length=255)  # Field name made lowercase.
    butype = models.CharField(db_column='BUType', max_length=50)  # Field name made lowercase.
    reportingbuid = models.CharField(db_column='ReportingBUID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reportingbutype = models.CharField(db_column='ReportingBUType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bumobile = models.CharField(db_column='BUMobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    buemail = models.CharField(db_column='BUEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    updateddate = models.DateField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GeographyMst'


class Ivrcallhistory(models.Model):
    ivrcallhistoryid = models.AutoField(db_column='IVRCallHistoryID', primary_key=True)  # Field name made lowercase.
    ivrcallqueueid = models.IntegerField(db_column='IVRCallQueueID', unique=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    branchmstid = models.ForeignKey(Branchmst, models.DO_NOTHING, db_column='BranchMstID')  # Field name made lowercase.
    loanmstid = models.ForeignKey('Loanmst', models.DO_NOTHING, db_column='LoanMstID')  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', max_length=255)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='ContactNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255)  # Field name made lowercase.
    next_emi_amount = models.DecimalField(db_column='Next_EMI_Amount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    next_emi_date = models.DateField(db_column='Next_EMI_Date', blank=True, null=True)  # Field name made lowercase.
    total_collection = models.DecimalField(db_column='Total_Collection', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    latest_collecteddate = models.DateField(db_column='Latest_CollectedDate', blank=True, null=True)  # Field name made lowercase.
    latest_collectedamt = models.DecimalField(db_column='Latest_CollectedAmt', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    issent = models.BooleanField(db_column='IsSent')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=255)  # Field name made lowercase.
    identifier = models.CharField(db_column='Identifier', max_length=255, blank=True, null=True)  # Field name made lowercase.
    callid = models.CharField(db_column='CallID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    recording = models.CharField(db_column='Recording', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conversation_json = models.JSONField(db_column='Conversation_json', blank=True, null=True)  # Field name made lowercase.
    conclusion = models.CharField(db_column='Conclusion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    calltried = models.IntegerField(db_column='CallTried', blank=True, null=True)  # Field name made lowercase.
    callduration = models.FloatField(db_column='CallDuration', blank=True, null=True)  # Field name made lowercase.
    customercode = models.CharField(db_column='CustomerCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    overdueamt = models.DecimalField(db_column='OverDueAmt', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=100, blank=True, null=True)  # Field name made lowercase.
    slot = models.CharField(db_column='Slot', max_length=255, blank=True, null=True)  # Field name made lowercase.
    callconnected = models.BooleanField(db_column='CallConnected', blank=True, null=True)  # Field name made lowercase.
    basedon = models.CharField(db_column='BasedOn', blank=True, null=True)  # Field name made lowercase.
    commflowid = models.IntegerField(db_column='CommFlowID', blank=True, null=True)  # Field name made lowercase.
    flowid = models.IntegerField(db_column='FlowID', blank=True, null=True)  # Field name made lowercase.
    ivrtemplatemappingid = models.IntegerField(db_column='IVRTemplateMappingID', blank=True, null=True)  # Field name made lowercase.
    isdelivered = models.BooleanField(db_column='IsDelivered', blank=True, null=True)  # Field name made lowercase.
    isread = models.BooleanField(db_column='IsRead', blank=True, null=True)  # Field name made lowercase.
    isresponded = models.BooleanField(db_column='IsResponded', blank=True, null=True)  # Field name made lowercase.
    alternativemobilenumber = models.CharField(db_column='AlternativeMobileNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    secondarycustmstid = models.IntegerField(db_column='SecondaryCustMstID', blank=True, null=True)  # Field name made lowercase.
    applicantname = models.CharField(db_column='ApplicantName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coapplicantcontact = models.CharField(db_column='CoApplicantContact', max_length=20, blank=True, null=True)  # Field name made lowercase.
    campaignmstid = models.IntegerField(db_column='CampaignMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IVRCallHistory'


class Ivrflowmapping(models.Model):
    ivrflowid = models.AutoField(db_column='IVRFlowID', primary_key=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    flowid = models.IntegerField(db_column='FlowID')  # Field name made lowercase.
    flowname = models.CharField(db_column='FlowName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    response = models.TextField(db_column='Response', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    lngmstid = models.ForeignKey('Languagemst', models.DO_NOTHING, db_column='LngMstID', blank=True, null=True)  # Field name made lowercase.
    ivrtemplatemappingid = models.ForeignKey('Ivrtemplatemapping', models.DO_NOTHING, db_column='IVRTemplateMappingID', blank=True, null=True)  # Field name made lowercase.
    ivrflowmstid = models.ForeignKey('Ivrflowmst', models.DO_NOTHING, db_column='IVRFlowMstID', blank=True, null=True)  # Field name made lowercase.
    isstart = models.BooleanField(db_column='IsStart', blank=True, null=True)  # Field name made lowercase.
    buttonpressed = models.CharField(db_column='ButtonPressed', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nexttemplate = models.IntegerField(db_column='NextTemplate', blank=True, null=True)  # Field name made lowercase.
    currenttemplate = models.IntegerField(db_column='CurrentTemplate', blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IVRFlowMapping'


class Ivrflowmst(models.Model):
    ivrflowmstid = models.AutoField(db_column='IVRFlowMstID', primary_key=True)  # Field name made lowercase.
    flowname = models.CharField(db_column='FlowName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IVRFlowMst'


class Ivrqueue(models.Model):
    ivrqueueid = models.AutoField(db_column='IVRQueueID', primary_key=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    branchmstid = models.ForeignKey(Branchmst, models.DO_NOTHING, db_column='BranchMstID')  # Field name made lowercase.
    loanmstid = models.ForeignKey('Loanmst', models.DO_NOTHING, db_column='LoanMstID')  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', max_length=50)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=100)  # Field name made lowercase.
    customercode = models.CharField(db_column='CustomerCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255)  # Field name made lowercase.
    overdueamt = models.DecimalField(db_column='OverDueAmt', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=100)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=255)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    slot = models.CharField(db_column='Slot', max_length=255, blank=True, null=True)  # Field name made lowercase.
    calltried = models.IntegerField(db_column='CallTried', blank=True, null=True)  # Field name made lowercase.
    callconnected = models.BooleanField(db_column='CallConnected', blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    basedon = models.CharField(db_column='BasedOn', blank=True, null=True)  # Field name made lowercase.
    commflowid = models.ForeignKey(Commflow, models.DO_NOTHING, db_column='CommFlowID', blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='ContactNumber', blank=True, null=True)  # Field name made lowercase.
    next_emi_amount = models.DecimalField(db_column='Next_EMI_Amount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    next_emi_date = models.DateField(db_column='Next_EMI_Date', blank=True, null=True)  # Field name made lowercase.
    total_collection = models.DecimalField(db_column='Total_Collection', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    latest_collecteddate = models.DateField(db_column='Latest_CollectedDate', blank=True, null=True)  # Field name made lowercase.
    latest_collectedamt = models.DecimalField(db_column='Latest_CollectedAmt', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    flowid = models.IntegerField(db_column='FlowID', blank=True, null=True)  # Field name made lowercase.
    ivrtemplatemappingid = models.IntegerField(db_column='IVRTemplateMappingID', blank=True, null=True)  # Field name made lowercase.
    identifier = models.CharField(db_column='Identifier', blank=True, null=True)  # Field name made lowercase.
    alternativemobilenumber = models.CharField(db_column='AlternativeMobileNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    secondarycustmstid = models.IntegerField(db_column='SecondaryCustMstID', blank=True, null=True)  # Field name made lowercase.
    applicantname = models.CharField(db_column='ApplicantName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coapplicantcontact = models.CharField(db_column='CoApplicantContact', max_length=20, blank=True, null=True)  # Field name made lowercase.
    campaignmstid = models.IntegerField(db_column='CampaignMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IVRQueue'


class Ivrtemplatemapping(models.Model):
    ivrtemplatemappingid = models.AutoField(db_column='IVRTemplateMappingID', primary_key=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
    templatename = models.CharField(db_column='TemplateName', max_length=255)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    lngmstid = models.ForeignKey('Languagemst', models.DO_NOTHING, db_column='LngMstID')  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isadmincreated = models.BooleanField(db_column='IsAdminCreated')  # Field name made lowercase.
    recordingurl = models.CharField(db_column='RecordingURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    templatebody = models.TextField(db_column='TemplateBody', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IVRTemplateMapping'


class Ivrusertemplate(models.Model):
    ivrusertemplateid = models.AutoField(db_column='IVRUserTemplateID', primary_key=True)  # Field name made lowercase.
    templatename = models.CharField(db_column='TemplateName', max_length=255)  # Field name made lowercase.
    bankmstid = models.IntegerField(db_column='BankMstID')  # Field name made lowercase.
    employeemstid = models.IntegerField(db_column='EmployeeMstID', blank=True, null=True)  # Field name made lowercase.
    variablenumber = models.IntegerField(db_column='VariableNumber', blank=True, null=True)  # Field name made lowercase.
    variablefield = models.CharField(db_column='VariableField', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ivrtemplatemappingid = models.ForeignKey(Ivrtemplatemapping, models.DO_NOTHING, db_column='IVRTemplateMappingID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IVRUserTemplate'


class Ivrvariablemapping(models.Model):
    ivrvariablemappingid = models.AutoField(db_column='IVRVariableMappingID', primary_key=True)  # Field name made lowercase.
    ivrtemplatemappingid = models.ForeignKey(Ivrtemplatemapping, models.DO_NOTHING, db_column='IVRTemplateMappingID', blank=True, null=True)  # Field name made lowercase.
    variableno = models.IntegerField(db_column='VariableNo', blank=True, null=True)  # Field name made lowercase.
    variablefield = models.CharField(db_column='VariableField', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IVRVariableMapping'


class Languagemst(models.Model):
    lngmstid = models.AutoField(db_column='LngMstID', primary_key=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=255)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    updateddate = models.DateField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LanguageMst'


class Loaninstallmentmst(models.Model):
    installmentmstid = models.AutoField(db_column='InstallmentMstID', primary_key=True)  # Field name made lowercase.
    loanmstid = models.ForeignKey('Loanmst', models.DO_NOTHING, db_column='LoanMstID')  # Field name made lowercase.
    scheduleid = models.IntegerField(db_column='ScheduleID', blank=True, null=True)  # Field name made lowercase.
    scheduledate = models.DateField(db_column='ScheduleDate', blank=True, null=True)  # Field name made lowercase.
    principleamt = models.DecimalField(db_column='PrincipleAmt', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    interestamt = models.DecimalField(db_column='InterestAmt', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    demand = models.DecimalField(db_column='Demand', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    customermstid = models.ForeignKey(Customermst, models.DO_NOTHING, db_column='CustomerMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoanInstallmentMst'


class Loanmst(models.Model):
    loanmstid = models.AutoField(db_column='LoanMstID', primary_key=True)  # Field name made lowercase.
    customermstid = models.ForeignKey(Customermst, models.DO_NOTHING, db_column='CustomerMstID', blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    disbursementdate = models.DateField(db_column='DisbursementDate', blank=True, null=True)  # Field name made lowercase.
    disbursementamt = models.DecimalField(db_column='DisbursementAmt', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    branchmstid = models.ForeignKey(Branchmst, models.DO_NOTHING, db_column='BranchMstID', blank=True, null=True)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    closingdate = models.DateField(db_column='ClosingDate', blank=True, null=True)  # Field name made lowercase.
    installmentstartdate = models.DateField(db_column='InstallmentStartDate', blank=True, null=True)  # Field name made lowercase.
    rateofinterest = models.DecimalField(db_column='RateOfInterest', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    repaymenttenure = models.IntegerField(db_column='RepaymentTenure', blank=True, null=True)  # Field name made lowercase.
    emiamount = models.DecimalField(db_column='EMIAmount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paymentfrequency = models.IntegerField(db_column='PaymentFrequency', blank=True, null=True)  # Field name made lowercase.
    lastmodifieddate = models.DateTimeField(db_column='LastModifiedDate', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    bmid = models.IntegerField(db_column='BMID', blank=True, null=True)  # Field name made lowercase.
    collectionofficerid = models.CharField(db_column='CollectionOfficerID', blank=True, null=True)  # Field name made lowercase.
    collectionofficername = models.CharField(db_column='CollectionOfficerName', blank=True, null=True)  # Field name made lowercase.
    dnd = models.BooleanField(db_column='DND', blank=True, null=True)  # Field name made lowercase.
    groupid = models.IntegerField(blank=True, null=True)
    groupname = models.CharField(blank=True, null=True)
    inserted_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LoanMst'
        unique_together = (('disbursementid', 'branchmstid', 'customermstid'),)


class Loginhistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    ip = models.GenericIPAddressField()
    ip_info = models.JSONField()
    city = models.CharField(max_length=80)
    region = models.CharField(max_length=80)
    region_code = models.CharField(max_length=10)
    country_code = models.CharField(max_length=2)
    country_name = models.CharField(max_length=80)
    currency = models.CharField(max_length=5)
    user_agent = models.TextField()
    created_at = models.DateTimeField()
    user = models.ForeignKey('Usermst', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'LoginHistory'


class Months(models.Model):
    monthnumber = models.IntegerField(db_column='MonthNumber', primary_key=True)  # Field name made lowercase. The composite primary key (MonthNumber, language) found, that is not supported. The first column is selected.
    monthname = models.CharField(db_column='MonthName', max_length=50)  # Field name made lowercase.
    language = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Months'
        unique_together = (('monthnumber', 'language'),)


class Overduereport(models.Model):
    disbursementid = models.CharField(db_column='DisbursementID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customerid = models.CharField(db_column='CustomerID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    oddays = models.IntegerField(db_column='OdDays', blank=True, null=True)  # Field name made lowercase.
    reportdate = models.DateField(db_column='ReportDate', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mobilenumber = models.CharField(db_column='MobileNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    disbursementdate = models.DateField(db_column='DisbursementDate', blank=True, null=True)  # Field name made lowercase.
    disbursementamt = models.DecimalField(db_column='DisbursementAmt', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    emiamount = models.DecimalField(db_column='EMIAmount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lastcollecteddate = models.DateField(db_column='LastCollectedDate', blank=True, null=True)  # Field name made lowercase.
    lastcollectedamount = models.DecimalField(db_column='LastCollectedAmount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    overdueamt = models.DecimalField(db_column='OverDueAmt', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.IntegerField(db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OverdueReport'


class PtExtracolumn(models.Model):
    pt_ec_id = models.AutoField(db_column='PT_EC_ID', primary_key=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=255)  # Field name made lowercase.
    columnname = models.CharField(db_column='ColumnName', max_length=255)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    user_columnname = models.CharField(db_column='User_ColumnName', max_length=255)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PT_ExtraColumn'


class Paymentlogs(models.Model):
    custmstid = models.IntegerField(db_column='CustMstID', blank=True, null=True)  # Field name made lowercase.
    qr_id = models.CharField(db_column='QR_ID', blank=True, null=True)  # Field name made lowercase.
    payment_link = models.CharField(db_column='Payment_Link', max_length=200, blank=True, null=True)  # Field name made lowercase.
    qr_link = models.CharField(db_column='QR_Link', max_length=200, blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=200, blank=True, null=True)  # Field name made lowercase.
    responseid = models.IntegerField(db_column='ResponseID', blank=True, null=True)  # Field name made lowercase.
    link_id = models.CharField(db_column='Link_ID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loanmstid = models.IntegerField(db_column='LoanMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentLogs'


class Periodiccommunication(models.Model):
    periodiccommid = models.AutoField(db_column='PeriodicCommID', primary_key=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    starttime = models.TimeField(db_column='StartTime')  # Field name made lowercase.
    endtime = models.TimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    until = models.DateField(db_column='Until', blank=True, null=True)  # Field name made lowercase.
    byweekday = models.CharField(db_column='ByWeekday', max_length=50, blank=True, null=True)  # Field name made lowercase.
    repeatfrequency = models.CharField(db_column='RepeatFrequency', max_length=50)  # Field name made lowercase.
    interval = models.IntegerField(db_column='Interval')  # Field name made lowercase.
    communicationtype = models.CharField(db_column='CommunicationType', max_length=100)  # Field name made lowercase.
    commflowmstid = models.ForeignKey(Commflowmst, models.DO_NOTHING, db_column='CommFlowMstID')  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PeriodicCommunication'


class Prioritytable(models.Model):
    bankmstid = models.OneToOneField(Bankmst, models.DO_NOTHING, db_column='BankMstID', primary_key=True)  # Field name made lowercase.
    iswhatsapp = models.BooleanField(db_column='IsWhatsApp', blank=True, null=True)  # Field name made lowercase.
    whatsappcomm = models.IntegerField(db_column='WhatsAppComm', blank=True, null=True)  # Field name made lowercase.
    isvoicebot = models.BooleanField(db_column='IsVoiceBot', blank=True, null=True)  # Field name made lowercase.
    voicebotcomm = models.IntegerField(db_column='VoiceBotComm', blank=True, null=True)  # Field name made lowercase.
    issms = models.BooleanField(db_column='IsSMS', blank=True, null=True)  # Field name made lowercase.
    smscomm = models.IntegerField(db_column='SMSComm', blank=True, null=True)  # Field name made lowercase.
    isivr = models.BooleanField(db_column='IsIVR', blank=True, null=True)  # Field name made lowercase.
    ivrcomm = models.IntegerField(db_column='IVRComm', blank=True, null=True)  # Field name made lowercase.
    isblaster = models.BooleanField(db_column='IsBlaster', blank=True, null=True)  # Field name made lowercase.
    blastercomm = models.IntegerField(db_column='BlasterComm', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PriorityTable'


class Reallocation(models.Model):
    reallocationid = models.AutoField(db_column='ReallocationID', primary_key=True)  # Field name made lowercase.
    loanmstid = models.IntegerField(db_column='LoanMstID')  # Field name made lowercase.
    customermstid = models.IntegerField(db_column='CustomerMstID')  # Field name made lowercase.
    oldofficerid = models.IntegerField(db_column='OldOfficerID')  # Field name made lowercase.
    oldofficername = models.CharField(db_column='OldOfficerName')  # Field name made lowercase.
    newofficerid = models.IntegerField(db_column='NewOfficerID')  # Field name made lowercase.
    newofficername = models.CharField(db_column='NewOfficerName')  # Field name made lowercase.
    actiontype = models.CharField(db_column='ActionType')  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    isreverted = models.BooleanField(db_column='IsReverted', blank=True, null=True)  # Field name made lowercase.
    revertdate = models.DateTimeField(db_column='RevertDate', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', blank=True, null=True)  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reallocation'


class Recordingsummary(models.Model):
    recording = models.CharField(db_column='Recording', blank=True, null=True)  # Field name made lowercase.
    summarization = models.CharField(db_column='Summarization', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RecordingSummary'


class Response(models.Model):
    responseid = models.AutoField(db_column='ResponseID', primary_key=True)  # Field name made lowercase.
    loanmstid = models.ForeignKey(Loanmst, models.DO_NOTHING, db_column='LoanMstID', blank=True, null=True)  # Field name made lowercase.
    blasterqueueid = models.IntegerField(db_column='BlasterQueueID', blank=True, null=True)  # Field name made lowercase.
    ivrqueueid = models.IntegerField(db_column='IVRQueueID', blank=True, null=True)  # Field name made lowercase.
    voicebotqueueid = models.IntegerField(db_column='VoiceBotQueueID', blank=True, null=True)  # Field name made lowercase.
    whatsappqueueid = models.IntegerField(db_column='WhatsappQueueID', blank=True, null=True)  # Field name made lowercase.
    allocationid = models.IntegerField(db_column='AllocationID', blank=True, null=True)  # Field name made lowercase.
    feedbackid = models.IntegerField(db_column='FeedbackID', blank=True, null=True)  # Field name made lowercase.
    modeofpayment = models.CharField(db_column='ModeOfPayment', max_length=50, blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    promisedatetime = models.DateTimeField(db_column='PromiseDateTime', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    responsedatetime = models.DateTimeField(db_column='ResponseDateTime', blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    branchmstid = models.ForeignKey(Branchmst, models.DO_NOTHING, db_column='BranchMstID', blank=True, null=True)  # Field name made lowercase.
    wrong_number = models.BooleanField(blank=True, null=True)
    id = models.BigAutoField()
    despute = models.CharField(db_column='Despute', blank=True, null=True)  # Field name made lowercase.
    extracolumn1_0 = models.CharField(db_column='extracolumn1', blank=True, null=True)  # Field renamed because of name conflict.
    campaignmstid = models.IntegerField(db_column='CampaignMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Response'


class Smshistory(models.Model):
    smshistoryid = models.AutoField(db_column='SMSHistoryID', primary_key=True)  # Field name made lowercase.
    smsqueueid = models.IntegerField(db_column='SMSQueueID', unique=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    branchmstid = models.ForeignKey(Branchmst, models.DO_NOTHING, db_column='BranchMstID')  # Field name made lowercase.
    loanmstid = models.ForeignKey(Loanmst, models.DO_NOTHING, db_column='LoanMstID')  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID')  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', max_length=255)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='ContactNumber', max_length=15)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=100)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255)  # Field name made lowercase.
    next_emi_amount = models.DecimalField(db_column='Next_EMI_Amount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    next_emi_date = models.DateField(db_column='Next_EMI_Date', blank=True, null=True)  # Field name made lowercase.
    total_collection = models.DecimalField(db_column='Total_Collection', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    latest_collecteddate = models.DateField(db_column='Latest_CollectedDate', blank=True, null=True)  # Field name made lowercase.
    latest_collectedamt = models.DecimalField(db_column='Latest_CollectedAmt', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    issent = models.BooleanField(db_column='IsSent')  # Field name made lowercase.
    isdelivered = models.BooleanField(db_column='IsDelivered')  # Field name made lowercase.
    isread = models.BooleanField(db_column='IsRead')  # Field name made lowercase.
    isresponded = models.BooleanField(db_column='IsResponded')  # Field name made lowercase.
    response = models.TextField(db_column='Response', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=255)  # Field name made lowercase.
    identifier = models.CharField(db_column='Identifier', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conversation_json = models.JSONField(db_column='Conversation_json', blank=True, null=True)  # Field name made lowercase.
    conclusion = models.CharField(db_column='Conclusion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attempts = models.IntegerField(db_column='Attempts', blank=True, null=True)  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customercode = models.CharField(db_column='CustomerCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    overdueamt = models.DecimalField(db_column='OverDueAmt', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=100, blank=True, null=True)  # Field name made lowercase.
    slot = models.CharField(db_column='Slot', max_length=255, blank=True, null=True)  # Field name made lowercase.
    basedon = models.CharField(db_column='BasedOn', blank=True, null=True)  # Field name made lowercase.
    commflowid = models.IntegerField(db_column='CommFlowID', blank=True, null=True)  # Field name made lowercase.
    flowid = models.IntegerField(db_column='FlowID', blank=True, null=True)  # Field name made lowercase.
    smstemplatemappingid = models.IntegerField(db_column='SMSTemplateMappingID', blank=True, null=True)  # Field name made lowercase.
    alternativemobilenumber = models.CharField(db_column='AlternativeMobileNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    secondarycustmstid = models.IntegerField(db_column='SecondaryCustMstID', blank=True, null=True)  # Field name made lowercase.
    applicantname = models.CharField(db_column='ApplicantName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coapplicantcontact = models.CharField(db_column='CoApplicantContact', max_length=20, blank=True, null=True)  # Field name made lowercase.
    campaignmstid = models.IntegerField(db_column='CampaignMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SMSHistory'


class Smsqueue(models.Model):
    smsqueueid = models.AutoField(db_column='SMSQueueID', primary_key=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    branchmstid = models.ForeignKey(Branchmst, models.DO_NOTHING, db_column='BranchMstID')  # Field name made lowercase.
    loanmstid = models.ForeignKey(Loanmst, models.DO_NOTHING, db_column='LoanMstID')  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', max_length=50)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=100)  # Field name made lowercase.
    customercode = models.CharField(db_column='CustomerCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=255)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    slot = models.CharField(db_column='Slot', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    basedon = models.CharField(db_column='BasedOn', blank=True, null=True)  # Field name made lowercase.
    commflowid = models.ForeignKey(Commflow, models.DO_NOTHING, db_column='CommFlowID', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='ContactNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    next_emi_amount = models.DecimalField(db_column='Next_EMI_Amount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    next_emi_date = models.DateField(db_column='Next_EMI_Date', blank=True, null=True)  # Field name made lowercase.
    total_collection = models.DecimalField(db_column='Total_Collection', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    latest_collecteddate = models.DateField(db_column='Latest_CollectedDate', blank=True, null=True)  # Field name made lowercase.
    latest_collectedamt = models.DecimalField(db_column='Latest_CollectedAmt', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    languageid = models.IntegerField(db_column='LanguageID', blank=True, null=True)  # Field name made lowercase.
    identifier = models.CharField(db_column='Identifier', max_length=255, blank=True, null=True)  # Field name made lowercase.
    flowid = models.IntegerField(db_column='FlowID', blank=True, null=True)  # Field name made lowercase.
    smstemplatemappingid = models.IntegerField(db_column='SMSTemplateMappingID', blank=True, null=True)  # Field name made lowercase.
    overdueamt = models.DecimalField(db_column='OverDueAmt', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    alternativemobilenumber = models.CharField(db_column='AlternativeMobileNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    secondarycustmstid = models.IntegerField(db_column='SecondaryCustMstID', blank=True, null=True)  # Field name made lowercase.
    applicantname = models.CharField(db_column='ApplicantName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coapplicantcontact = models.CharField(db_column='CoApplicantContact', max_length=20, blank=True, null=True)  # Field name made lowercase.
    campaignmstid = models.IntegerField(db_column='CampaignMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SMSQueue'


class Smstemplatemapping(models.Model):
    smstemplatemappingid = models.AutoField(db_column='SMSTemplateMappingID', primary_key=True)  # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
    templatename = models.CharField(db_column='TemplateName', max_length=255)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    lngmstid = models.ForeignKey(Languagemst, models.DO_NOTHING, db_column='LngMstID')  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=255)  # Field name made lowercase.
    isadmincreated = models.BooleanField(db_column='IsAdminCreated')  # Field name made lowercase.
    recordingurl = models.CharField(db_column='RecordingURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    templatebody = models.CharField(db_column='TemplateBody', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SMSTemplateMapping'


class Smsusertemplate(models.Model):
    smsusertemplateid = models.AutoField(db_column='SMSUserTemplateID', primary_key=True)  # Field name made lowercase.
    templatename = models.CharField(db_column='TemplateName', max_length=255)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    employeemstid = models.ForeignKey(Employeemst, models.DO_NOTHING, db_column='EmployeeMstID', blank=True, null=True)  # Field name made lowercase.
    variablenumber = models.IntegerField(db_column='VariableNumber')  # Field name made lowercase.
    variablefield = models.CharField(db_column='VariableField', max_length=255)  # Field name made lowercase.
    smstemplatemappingid = models.ForeignKey(Smstemplatemapping, models.DO_NOTHING, db_column='SMSTemplateMappingID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SMSUserTemplate'


class Splogs(models.Model):
    logid = models.AutoField(db_column='LogID', primary_key=True)  # Field name made lowercase.
    bankmstid = models.IntegerField(db_column='BankMstID')  # Field name made lowercase.
    functionname = models.CharField(db_column='FunctionName', max_length=100)  # Field name made lowercase.
    executiontimestamp = models.DateTimeField(db_column='ExecutionTimestamp', blank=True, null=True)  # Field name made lowercase.
    rowsaffected = models.IntegerField(db_column='RowsAffected', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10)  # Field name made lowercase.
    errormessage = models.TextField(db_column='ErrorMessage', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SPLogs'


class Secondarycustmst(models.Model):
    secondarycustmstid = models.AutoField(db_column='SecondaryCustMstID', primary_key=True)  # Field name made lowercase.
    branchmstid = models.ForeignKey(Branchmst, models.DO_NOTHING, db_column='BranchMstID', blank=True, null=True)  # Field name made lowercase.
    applicantname = models.CharField(db_column='ApplicantName', max_length=255)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateOfBirth', blank=True, null=True)  # Field name made lowercase.
    coapplicantcontact = models.CharField(db_column='CoApplicantContact', max_length=20, blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    lastmodifieddate = models.DateField(db_column='LastModifiedDate', blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    loanmstid = models.ForeignKey(Loanmst, models.DO_NOTHING, db_column='LoanMstID', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mobilenumber = models.CharField(db_column='MobileNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    alternativemobilenumber = models.CharField(db_column='AlternativeMobileNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    inserted_on = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SecondaryCustMst'


class Subscriptionmst(models.Model):
    subscriptionmstid = models.AutoField(db_column='SubscriptionMstID', primary_key=True)  # Field name made lowercase.
    subscriptiontype = models.CharField(db_column='SubscriptionType', max_length=255)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    lastupdated = models.DateField(db_column='LastUpdated', blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    screens = models.JSONField(db_column='Screens', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubscriptionMst'


class TblCommunicationqueueSwamiSamarth(models.Model):
    communicationqueueid = models.TextField(db_column='CommunicationQueueID', blank=True, null=True)  # Field name made lowercase.
    branchmstid = models.TextField(db_column='BranchMstID', blank=True, null=True)  # Field name made lowercase.
    iswhatsapp = models.BooleanField(db_column='IsWhatsApp', blank=True, null=True)  # Field name made lowercase.
    isblaster = models.BooleanField(db_column='IsBlaster', blank=True, null=True)  # Field name made lowercase.
    isvoicebot = models.BooleanField(db_column='IsVoiceBot', blank=True, null=True)  # Field name made lowercase.
    issms = models.TextField(db_column='IsSMS', blank=True, null=True)  # Field name made lowercase.
    slot = models.TextField(db_column='Slot', blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.IntegerField(db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    concat = models.TextField(blank=True, null=True)
    disbursmentid = models.TextField(blank=True, null=True)
    loanmstid = models.TextField(db_column='LoanMstID', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.TextField(db_column='ExtraColumn1', blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.TextField(db_column='ExtraColumn2', blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.TextField(db_column='ExtraColumn3', blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.TextField(db_column='ExtraColumn4', blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.TextField(db_column='ExtraColumn5', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    isivr = models.TextField(db_column='IsIVR', blank=True, null=True)  # Field name made lowercase.
    basedondate = models.TextField(db_column='BasedOnDate', blank=True, null=True)  # Field name made lowercase.
    bmallocate = models.BooleanField(db_column='BMAllocate', blank=True, null=True)  # Field name made lowercase.
    collectionofficerallocate = models.TextField(db_column='CollectionOfficerAllocate', blank=True, null=True)  # Field name made lowercase.
    campaignmstid = models.TextField(db_column='CampaignMstID', blank=True, null=True)  # Field name made lowercase.
    flowid = models.TextField(db_column='FlowID', blank=True, null=True)  # Field name made lowercase.
    secondarycustmstid = models.TextField(db_column='SecondaryCustMstID', blank=True, null=True)  # Field name made lowercase.
    callinguserid = models.TextField(db_column='CallingUserID', blank=True, null=True)  # Field name made lowercase.
    iscalling = models.TextField(db_column='IsCalling', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_CommunicationQueue_Swami_samarth'


class TempTblAicallHistSwamiSamarth(models.Model):
    voicebothistoryid = models.TextField(db_column='VoiceBotHistoryID', blank=True, null=True)  # Field name made lowercase.
    voicebotqueueid = models.TextField(db_column='VoiceBotQueueID', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.IntegerField(db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    branchmstid = models.TextField(db_column='BranchMstID', blank=True, null=True)  # Field name made lowercase.
    loanmstid = models.TextField(db_column='LoanMstID', blank=True, null=True)  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customerid = models.TextField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.TextField(db_column='DisbursementID', blank=True, null=True)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='ContactNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    loantype = models.TextField(db_column='LoanType', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    overdue_amount = models.DecimalField(db_column='Overdue_Amount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    next_emi_amount = models.DecimalField(db_column='Next_EMI_Amount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    next_emi_date = models.DateField(db_column='Next_EMI_Date', blank=True, null=True)  # Field name made lowercase.
    total_collection = models.DecimalField(db_column='Total_Collection', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    latest_collecteddate = models.DateField(db_column='Latest_CollectedDate', blank=True, null=True)  # Field name made lowercase.
    latest_collectedamt = models.DecimalField(db_column='Latest_CollectedAmt', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    issent = models.TextField(db_column='IsSent', blank=True, null=True)  # Field name made lowercase.
    isdelivered = models.TextField(db_column='IsDelivered', blank=True, null=True)  # Field name made lowercase.
    isread = models.TextField(db_column='IsRead', blank=True, null=True)  # Field name made lowercase.
    isresponded = models.TextField(db_column='IsResponded', blank=True, null=True)  # Field name made lowercase.
    response = models.TextField(db_column='Response', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    identifier = models.TextField(db_column='Identifier', blank=True, null=True)  # Field name made lowercase.
    callid = models.CharField(db_column='CallID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    recording = models.CharField(db_column='Recording', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conversation_json = models.JSONField(db_column='Conversation_json', blank=True, null=True)  # Field name made lowercase.
    conclusion = models.CharField(db_column='Conclusion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    calltried = models.TextField(db_column='CallTried', blank=True, null=True)  # Field name made lowercase.
    callduration = models.FloatField(db_column='CallDuration', blank=True, null=True)  # Field name made lowercase.
    basedon = models.TextField(db_column='BasedOn', blank=True, null=True)  # Field name made lowercase.
    commflowid = models.TextField(db_column='CommFlowID', blank=True, null=True)  # Field name made lowercase.
    customercode = models.TextField(db_column='CustomerCode', blank=True, null=True)  # Field name made lowercase.
    language = models.TextField(db_column='Language', blank=True, null=True)  # Field name made lowercase.
    overdueamt = models.DecimalField(db_column='OverdueAmt', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    slot = models.TextField(db_column='Slot', blank=True, null=True)  # Field name made lowercase.
    flowid = models.TextField(db_column='FlowID', blank=True, null=True)  # Field name made lowercase.
    voicebottemplatemappingid = models.TextField(db_column='VoiceBotTemplateMappingID', blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.TextField(db_column='Extracolumn1', blank=True, null=True)  # Field name made lowercase.
    alternativemobilenumber = models.TextField(db_column='AlternativeMobileNumber', blank=True, null=True)  # Field name made lowercase.
    secondarycustmstid = models.TextField(db_column='SecondaryCustMstID', blank=True, null=True)  # Field name made lowercase.
    applicantname = models.TextField(db_column='ApplicantName', blank=True, null=True)  # Field name made lowercase.
    coapplicantcontact = models.TextField(db_column='CoApplicantContact', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Temp_TBL_AICall_Hist_Swami_Samarth'


class TempTblBlasterHistSwamiSamarth(models.Model):
    blasterhistoryid = models.TextField(db_column='BlasterHistoryID', blank=True, null=True)  # Field name made lowercase.
    blasterqueueid = models.TextField(db_column='BlasterQueueID', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.IntegerField(db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    branchmstid = models.TextField(db_column='BranchMstID', blank=True, null=True)  # Field name made lowercase.
    loanmstid = models.TextField(db_column='LoanMstID', blank=True, null=True)  # Field name made lowercase.
    customerid = models.TextField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.TextField(db_column='DisbursementID', blank=True, null=True)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='ContactNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    loantype = models.TextField(db_column='LoanType', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    next_emi_amount = models.DecimalField(db_column='Next_EMI_Amount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    next_emi_date = models.DateField(db_column='Next_EMI_Date', blank=True, null=True)  # Field name made lowercase.
    total_collection = models.DecimalField(db_column='Total_Collection', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    latest_collecteddate = models.DateField(db_column='Latest_CollectedDate', blank=True, null=True)  # Field name made lowercase.
    latest_collectedamt = models.DecimalField(db_column='Latest_CollectedAmt', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    issent = models.TextField(db_column='IsSent', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    identifier = models.TextField(db_column='Identifier', blank=True, null=True)  # Field name made lowercase.
    language = models.TextField(db_column='Language', blank=True, null=True)  # Field name made lowercase.
    callid = models.CharField(db_column='CallID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    recording = models.CharField(db_column='Recording', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conversation_json = models.JSONField(db_column='Conversation_json', blank=True, null=True)  # Field name made lowercase.
    conclusion = models.CharField(db_column='Conclusion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    calltried = models.IntegerField(db_column='CallTried', blank=True, null=True)  # Field name made lowercase.
    callduration = models.IntegerField(db_column='CallDuration', blank=True, null=True)  # Field name made lowercase.
    callconnected = models.BooleanField(db_column='CallConnected', blank=True, null=True)  # Field name made lowercase.
    slot = models.TextField(db_column='Slot', blank=True, null=True)  # Field name made lowercase.
    basedon = models.TextField(db_column='BasedOn', blank=True, null=True)  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customercode = models.TextField(db_column='CustomerCode', blank=True, null=True)  # Field name made lowercase.
    flowid = models.TextField(db_column='FlowID', blank=True, null=True)  # Field name made lowercase.
    blastertemplatemappingid = models.TextField(db_column='BlasterTemplateMappingID', blank=True, null=True)  # Field name made lowercase.
    isdelivered = models.TextField(db_column='IsDelivered', blank=True, null=True)  # Field name made lowercase.
    isread = models.TextField(db_column='IsRead', blank=True, null=True)  # Field name made lowercase.
    isresponded = models.TextField(db_column='IsResponded', blank=True, null=True)  # Field name made lowercase.
    overdueamt = models.DecimalField(db_column='OverDueAmt', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    alternativemobilenumber = models.TextField(db_column='AlternativeMobileNumber', blank=True, null=True)  # Field name made lowercase.
    secondarycustmstid = models.TextField(db_column='SecondaryCustMstID', blank=True, null=True)  # Field name made lowercase.
    applicantname = models.TextField(db_column='ApplicantName', blank=True, null=True)  # Field name made lowercase.
    coapplicantcontact = models.TextField(db_column='CoApplicantContact', blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.IntegerField(db_column='ExtraColumn1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Temp_TBL_Blaster_Hist_Swami_Samarth'


class TempTblChannelResponseSwamiSamarth(models.Model):
    responseid = models.TextField(db_column='ResponseID', blank=True, null=True)  # Field name made lowercase.
    loanmstid = models.TextField(db_column='LoanMstID', blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.TextField(blank=True, null=True)
    blasterqueueid = models.TextField(db_column='BlasterQueueID', blank=True, null=True)  # Field name made lowercase.
    ivrqueueid = models.TextField(db_column='IVRQueueID', blank=True, null=True)  # Field name made lowercase.
    voicebotqueueid = models.TextField(db_column='VoiceBotQueueID', blank=True, null=True)  # Field name made lowercase.
    whatsappqueueid = models.TextField(db_column='WhatsappQueueID', blank=True, null=True)  # Field name made lowercase.
    allocationid = models.TextField(db_column='AllocationID', blank=True, null=True)  # Field name made lowercase.
    feedbackid = models.TextField(db_column='FeedbackID', blank=True, null=True)  # Field name made lowercase.
    modeofpayment = models.CharField(db_column='ModeOfPayment', max_length=50, blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=10485760, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=10485760, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=10485760, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.TextField(db_column='ExtraColumn4', blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.TextField(db_column='ExtraColumn5', blank=True, null=True)  # Field name made lowercase.
    promisedatetime = models.DateField(db_column='PromiseDateTime', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10485760, blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    responsedatetime = models.DateField(db_column='ResponseDateTime', blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.IntegerField(db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    branchmstid = models.TextField(db_column='BranchMstID', blank=True, null=True)  # Field name made lowercase.
    wrong_number = models.BooleanField(blank=True, null=True)
    id = models.TextField(blank=True, null=True)
    despute = models.CharField(db_column='Despute', max_length=50, blank=True, null=True)  # Field name made lowercase.
    extracolumn1_0 = models.TextField(db_column='extracolumn1', blank=True, null=True)  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'Temp_TBL_Channel_Response_Swami_Samarth'


class TempTblTransactionsSwamiSamarth(models.Model):
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    loanmstid = models.TextField(db_column='LoanMstID', blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.TextField(db_column='DisbursementID', blank=True, null=True)  # Field name made lowercase.
    collectedamt = models.DecimalField(db_column='CollectedAmt', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    collecteddate = models.DateField(db_column='CollectedDate')  # Field name made lowercase.
    principlecollected = models.TextField(db_column='PrincipleCollected', blank=True, null=True)  # Field name made lowercase.
    interestcollected = models.TextField(db_column='InterestCollected', blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.TextField(db_column='ExtraColumn1', blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.TextField(db_column='ExtraColumn2', blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.TextField(db_column='ExtraColumn3', blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.TextField(db_column='ExtraColumn4', blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.TextField(db_column='ExtraColumn5', blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.IntegerField(db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    loantype = models.TextField(db_column='LoanType', blank=True, null=True)  # Field name made lowercase.
    customerid = models.TextField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Temp_TBL_Transactions_Swami_Samarth'


class TempTblWhatsappHistSwamiSamarth(models.Model):
    whatsapphistoryid = models.TextField(db_column='WhatsAppHistoryID', blank=True, null=True)  # Field name made lowercase.
    whatsappqueueid = models.TextField(db_column='WhatsAppQueueID', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.IntegerField(db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    branchmstid = models.TextField(db_column='BranchMstID', blank=True, null=True)  # Field name made lowercase.
    loanmstid = models.TextField(db_column='LoanMstID', blank=True, null=True)  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customerid = models.TextField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.TextField(db_column='DisbursementID', blank=True, null=True)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='ContactNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    loantype = models.TextField(db_column='LoanType', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    overdue_amount = models.DecimalField(db_column='Overdue_Amount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    next_emi_amount = models.DecimalField(db_column='Next_EMI_Amount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    next_emi_date = models.DateField(db_column='Next_EMI_Date', blank=True, null=True)  # Field name made lowercase.
    total_collection = models.DecimalField(db_column='Total_Collection', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    latest_collecteddate = models.DateField(db_column='Latest_CollectedDate', blank=True, null=True)  # Field name made lowercase.
    latest_collectedamt = models.DecimalField(db_column='Latest_CollectedAmt', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    issent = models.BooleanField(db_column='IsSent', blank=True, null=True)  # Field name made lowercase.
    isdelivered = models.BooleanField(db_column='IsDelivered', blank=True, null=True)  # Field name made lowercase.
    isread = models.BooleanField(db_column='IsRead', blank=True, null=True)  # Field name made lowercase.
    isresponded = models.BooleanField(db_column='IsResponded', blank=True, null=True)  # Field name made lowercase.
    response = models.CharField(db_column='Response', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    identifier = models.CharField(db_column='Identifier', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lngmstid = models.TextField(db_column='LngMstID', blank=True, null=True)  # Field name made lowercase.
    basedon = models.TextField(db_column='BasedOn', blank=True, null=True)  # Field name made lowercase.
    commflowid = models.TextField(db_column='CommFlowID', blank=True, null=True)  # Field name made lowercase.
    customercode = models.TextField(db_column='CustomerCode', blank=True, null=True)  # Field name made lowercase.
    language = models.TextField(db_column='Language', blank=True, null=True)  # Field name made lowercase.
    flowid = models.TextField(db_column='FlowID', blank=True, null=True)  # Field name made lowercase.
    whatsapptemplatemappingid = models.TextField(db_column='WhatsAppTemplateMappingID', blank=True, null=True)  # Field name made lowercase.
    overdueamt = models.DecimalField(db_column='OverdueAmt', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    slot = models.TextField(db_column='Slot', blank=True, null=True)  # Field name made lowercase.
    alternativemobilenumber = models.TextField(db_column='AlternativeMobileNumber', blank=True, null=True)  # Field name made lowercase.
    secondarycustmstid = models.TextField(db_column='SecondaryCustMstID', blank=True, null=True)  # Field name made lowercase.
    applicantname = models.TextField(db_column='ApplicantName', blank=True, null=True)  # Field name made lowercase.
    coapplicantcontact = models.TextField(db_column='CoApplicantContact', blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.IntegerField(db_column='ExtraColumn1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Temp_TBL_WhatsApp_Hist_Swami_Samarth'


class TempTblWhatsappMessagesSwamiSamarth(models.Model):
    whatsappmessageid = models.TextField(db_column='WhatsAppMessageID', blank=True, null=True)  # Field name made lowercase.
    messagedate = models.DateTimeField(db_column='MessageDate', blank=True, null=True)  # Field name made lowercase.
    whatsappqueueid = models.TextField(db_column='WhatsAppQueueID', blank=True, null=True)  # Field name made lowercase.
    messageid = models.CharField(db_column='MessageID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    assignedto = models.CharField(db_column='AssignedTo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sender = models.CharField(db_column='Sender', max_length=100, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=250, blank=True, null=True)  # Field name made lowercase.
    customernumber = models.CharField(db_column='CustomerNumber', max_length=250, blank=True, null=True)  # Field name made lowercase.
    loanmstid = models.IntegerField(db_column='LoanMstID', blank=True, null=True)  # Field name made lowercase.
    button = models.CharField(db_column='Button', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=100, blank=True, null=True)  # Field name made lowercase.
    identifier = models.CharField(db_column='Identifier', max_length=50, blank=True, null=True)  # Field name made lowercase.
    whatsappusertemplateid = models.TextField(db_column='WhatsAppUserTemplateID', blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.IntegerField(db_column='ExtraColumn1', blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.TextField(db_column='ExtraColumn2', blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.IntegerField(db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    extracolumn = models.TextField(blank=True, null=True)
    gapshapreplyid = models.TextField(db_column='GapshapReplyID', blank=True, null=True)  # Field name made lowercase.
    id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Temp_TBL_WhatsApp_Messages_Swami_Samarth'


class TransactionLogs(models.Model):
    qr_id = models.CharField(db_column='QR_ID', blank=True, null=True)  # Field name made lowercase.
    link_id = models.CharField(db_column='Link_ID', blank=True, null=True)  # Field name made lowercase.
    payment_id = models.CharField(db_column='Payment_ID', blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    method = models.CharField(db_column='Method', blank=True, null=True)  # Field name made lowercase.
    vpa = models.CharField(db_column='VPA', blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', blank=True, null=True)  # Field name made lowercase.
    payment_cust_id = models.CharField(db_column='Payment_Cust_ID', blank=True, null=True)  # Field name made lowercase.
    transaction_date = models.DateTimeField(db_column='Transaction_date', blank=True, null=True)  # Field name made lowercase.
    body = models.TextField(db_column='Body', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    datetime = models.DateTimeField(db_column='DateTime', blank=True, null=True)  # Field name made lowercase.
    custmstid = models.IntegerField(db_column='CustMstID', blank=True, null=True)  # Field name made lowercase.
    loanmstid = models.IntegerField(db_column='LoanMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Transaction_Logs'


class Transactions(models.Model):
    transactionid = models.AutoField(db_column='TransactionID', primary_key=True)  # Field name made lowercase.
    branchmstid = models.ForeignKey(Branchmst, models.DO_NOTHING, db_column='BranchMstID')  # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    loanmstid = models.ForeignKey(Loanmst, models.DO_NOTHING, db_column='LoanMstID')  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    collectedamt = models.DecimalField(db_column='CollectedAmt', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    collecteddate = models.DateField(db_column='CollectedDate', blank=True, null=True)  # Field name made lowercase.
    processed = models.BooleanField(db_column='Processed', blank=True, null=True)  # Field name made lowercase.
    principlecollected = models.DecimalField(db_column='PrincipleCollected', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    interestcollected = models.DecimalField(db_column='InterestCollected', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', blank=True, null=True)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Transactions'


class Userconversations(models.Model):
    user_id = models.CharField(max_length=255)
    last_active_conversation = models.ForeignKey(Activeconversation, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserConversations'


class UserconversationsActiveConversations(models.Model):
    userconversations = models.ForeignKey(Userconversations, models.DO_NOTHING)
    activeconversation = models.ForeignKey(Activeconversation, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'UserConversations_active_conversations'
        unique_together = (('userconversations', 'activeconversation'),)


class UserconversationsCompletedConversations(models.Model):
    userconversations = models.ForeignKey(Userconversations, models.DO_NOTHING)
    conversationhistory = models.ForeignKey(Conversationhistory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'UserConversations_completed_conversations'
        unique_together = (('userconversations', 'conversationhistory'),)


class Userfeedback(models.Model):
    userfeedbackid = models.AutoField(db_column='UserFeedbackID', primary_key=True)  # Field name made lowercase.
    branchmstid = models.ForeignKey(Branchmst, models.DO_NOTHING, db_column='BranchMstID', blank=True, null=True)  # Field name made lowercase.
    loanmstid = models.ForeignKey(Loanmst, models.DO_NOTHING, db_column='LoanMstID')  # Field name made lowercase.
    feedbackdate = models.DateField(db_column='FeedbackDate')  # Field name made lowercase.
    agreedtopay = models.BooleanField(db_column='AgreedToPay')  # Field name made lowercase.
    refusedtopay = models.BooleanField(db_column='RefusedToPay')  # Field name made lowercase.
    wrongnumber = models.BooleanField(db_column='WrongNumber')  # Field name made lowercase.
    customerbusy = models.BooleanField(db_column='CustomerBusy')  # Field name made lowercase.
    promise_date = models.DateField(blank=True, null=True)
    promise_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    reasonfordenial = models.TextField(db_column='ReasonForDenial', blank=True, null=True)  # Field name made lowercase.
    mode_of_payment = models.CharField(max_length=255, blank=True, null=True)
    collectiondate = models.CharField(db_column='CollectionDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    collectionamount = models.CharField(db_column='CollectionAmount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customernotreply = models.CharField(db_column='CustomerNotReply', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othercomments = models.CharField(db_column='OtherComments', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=300, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=300, blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserFeedback'


class Usermst(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    branchid = models.CharField(db_column='BranchID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mobilenumber = models.CharField(db_column='MobileNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    is_admin = models.BooleanField()
    bankmaster = models.BooleanField(db_column='BankMaster')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate')  # Field name made lowercase.
    extracolumn_1 = models.TextField(db_column='ExtraColumn_1', blank=True, null=True)  # Field name made lowercase.
    extracolumn_2 = models.TextField(db_column='ExtraColumn_2', blank=True, null=True)  # Field name made lowercase.
    extracolumn_3 = models.TextField(db_column='ExtraColumn_3', blank=True, null=True)  # Field name made lowercase.
    extracolumn_4 = models.TextField(db_column='ExtraColumn_4', blank=True, null=True)  # Field name made lowercase.
    extracolumn_5 = models.TextField(db_column='ExtraColumn_5', blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID_id', blank=True, null=True)  # Field name made lowercase.
    branchmstid = models.ForeignKey(Branchmst, models.DO_NOTHING, db_column='BranchMstID_id', blank=True, null=True)  # Field name made lowercase.
    fo_id = models.IntegerField(db_column='FO_id', blank=True, null=True)  # Field name made lowercase.
    bucode = models.CharField(db_column='BUcode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserMst'


class UsermstGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    usermst = models.ForeignKey(Usermst, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'UserMst_groups'
        unique_together = (('usermst', 'group'),)


class UsermstUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    usermst = models.ForeignKey(Usermst, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'UserMst_user_permissions'
        unique_together = (('usermst', 'permission'),)


class Voicebothistory(models.Model):
    voicebothistoryid = models.AutoField(db_column='VoiceBotHistoryID', primary_key=True)  # Field name made lowercase.
    voicebotqueueid = models.IntegerField(db_column='VoiceBotQueueID', unique=True, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    branchmstid = models.ForeignKey(Branchmst, models.DO_NOTHING, db_column='BranchMstID', blank=True, null=True)  # Field name made lowercase.
    loanmstid = models.ForeignKey(Loanmst, models.DO_NOTHING, db_column='LoanMstID', blank=True, null=True)  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    customerid = models.CharField(db_column='CustomerID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='ContactNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    overdue_amount = models.DecimalField(db_column='Overdue_Amount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    next_emi_amount = models.DecimalField(db_column='Next_EMI_Amount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    next_emi_date = models.DateField(db_column='Next_EMI_Date', blank=True, null=True)  # Field name made lowercase.
    total_collection = models.DecimalField(db_column='Total_Collection', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    latest_collecteddate = models.DateField(db_column='Latest_CollectedDate', blank=True, null=True)  # Field name made lowercase.
    latest_collectedamt = models.DecimalField(db_column='Latest_CollectedAmt', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    issent = models.BooleanField(db_column='IsSent', blank=True, null=True)  # Field name made lowercase.
    isdelivered = models.BooleanField(db_column='IsDelivered', blank=True, null=True)  # Field name made lowercase.
    isread = models.BooleanField(db_column='IsRead', blank=True, null=True)  # Field name made lowercase.
    isresponded = models.BooleanField(db_column='IsResponded', blank=True, null=True)  # Field name made lowercase.
    response = models.TextField(db_column='Response', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    identifier = models.CharField(db_column='Identifier', max_length=255, blank=True, null=True)  # Field name made lowercase.
    callid = models.CharField(db_column='CallID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    recording = models.CharField(db_column='Recording', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conversation_json = models.JSONField(db_column='Conversation_json', blank=True, null=True)  # Field name made lowercase.
    conclusion = models.CharField(db_column='Conclusion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    calltried = models.IntegerField(db_column='CallTried', blank=True, null=True)  # Field name made lowercase.
    callduration = models.FloatField(db_column='CallDuration', blank=True, null=True)  # Field name made lowercase.
    basedon = models.CharField(db_column='BasedOn', blank=True, null=True)  # Field name made lowercase.
    commflowid = models.IntegerField(db_column='CommFlowID', blank=True, null=True)  # Field name made lowercase.
    customercode = models.CharField(db_column='CustomerCode', blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', blank=True, null=True)  # Field name made lowercase.
    overdueamt = models.DecimalField(db_column='OverdueAmt', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    slot = models.CharField(db_column='Slot', max_length=255, blank=True, null=True)  # Field name made lowercase.
    flowid = models.IntegerField(db_column='FlowID', blank=True, null=True)  # Field name made lowercase.
    voicebottemplatemappingid = models.IntegerField(db_column='VoiceBotTemplateMappingID', blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='Extracolumn1', blank=True, null=True)  # Field name made lowercase.
    alternativemobilenumber = models.CharField(db_column='AlternativeMobileNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    secondarycustmstid = models.IntegerField(db_column='SecondaryCustMstID', blank=True, null=True)  # Field name made lowercase.
    applicantname = models.CharField(db_column='ApplicantName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coapplicantcontact = models.CharField(db_column='CoApplicantContact', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mixmonitorrecording = models.CharField(db_column='MixMonitorRecording', max_length=255, blank=True, null=True)  # Field name made lowercase.
    campaignmstid = models.IntegerField(db_column='CampaignMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VoiceBotHistory'


class Voicebotqueue(models.Model):
    voicebotqueueid = models.AutoField(db_column='VoiceBotQueueID', primary_key=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    branchmstid = models.ForeignKey(Branchmst, models.DO_NOTHING, db_column='BranchMstID', blank=True, null=True)  # Field name made lowercase.
    loanmstid = models.ForeignKey(Loanmst, models.DO_NOTHING, db_column='LoanMstID', blank=True, null=True)  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customercode = models.CharField(db_column='CustomerCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    overdueamt = models.DecimalField(db_column='OverdueAmt', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    slot = models.CharField(db_column='Slot', max_length=255, blank=True, null=True)  # Field name made lowercase.
    calltried = models.IntegerField(db_column='CallTried', blank=True, null=True)  # Field name made lowercase.
    callconnected = models.BooleanField(db_column='CallConnected', blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    basedon = models.CharField(db_column='BasedOn', blank=True, null=True)  # Field name made lowercase.
    commflowid = models.ForeignKey(Commflow, models.DO_NOTHING, db_column='CommFlowID', blank=True, null=True)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='ContactNumber', blank=True, null=True)  # Field name made lowercase.
    customerid = models.CharField(db_column='CustomerID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchID', blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    next_emi_amount = models.DecimalField(db_column='Next_EMI_Amount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    next_emi_date = models.DateField(db_column='Next_EMI_Date', blank=True, null=True)  # Field name made lowercase.
    total_collection = models.DecimalField(db_column='Total_Collection', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    latest_collecteddate = models.DateField(db_column='Latest_CollectedDate', blank=True, null=True)  # Field name made lowercase.
    latest_collectedamt = models.DecimalField(db_column='Latest_CollectedAmt', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    identifier = models.CharField(db_column='Identifier', max_length=255, blank=True, null=True)  # Field name made lowercase.
    flowid = models.IntegerField(db_column='FlowID', blank=True, null=True)  # Field name made lowercase.
    voicebottemplatemappingid = models.IntegerField(db_column='VoiceBotTemplateMappingID', blank=True, null=True)  # Field name made lowercase.
    alternativemobilenumber = models.CharField(db_column='AlternativeMobileNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    secondarycustmstid = models.IntegerField(db_column='SecondaryCustMstID', blank=True, null=True)  # Field name made lowercase.
    applicantname = models.CharField(db_column='ApplicantName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coapplicantcontact = models.CharField(db_column='CoApplicantContact', max_length=20, blank=True, null=True)  # Field name made lowercase.
    campaignmstid = models.IntegerField(db_column='CampaignMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VoiceBotQueue'


class Voicebottemplatemapping(models.Model):
    voicebottemplatemappingid = models.AutoField(db_column='VoiceBotTemplateMappingID', primary_key=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
    templatename = models.CharField(db_column='TemplateName', max_length=255)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    lngmstid = models.ForeignKey(Languagemst, models.DO_NOTHING, db_column='LngMstID')  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isadmincreated = models.BooleanField(db_column='IsAdminCreated', blank=True, null=True)  # Field name made lowercase.
    recordingurl = models.CharField(db_column='RecordingURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    templatebody = models.CharField(db_column='TemplateBody', blank=True, null=True)  # Field name made lowercase.
    startmsg = models.CharField(db_column='StartMsg', blank=True, null=True)  # Field name made lowercase.
    endmsg = models.CharField(db_column='EndMsg', blank=True, null=True)  # Field name made lowercase.
    systeminstructions = models.CharField(db_column='SystemInstructions', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VoiceBotTemplateMapping'


class Voicebotusertemplate(models.Model):
    voicebotusertemplateid = models.AutoField(db_column='VoiceBotUserTemplateID', primary_key=True)  # Field name made lowercase.
    templatename = models.CharField(db_column='TemplateName', max_length=255)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    employeemstid = models.ForeignKey(Employeemst, models.DO_NOTHING, db_column='EmployeeMstID', blank=True, null=True)  # Field name made lowercase.
    variablenumber = models.IntegerField(db_column='VariableNumber')  # Field name made lowercase.
    variablefield = models.CharField(db_column='VariableField', max_length=255)  # Field name made lowercase.
    voicebottemplatemappingid = models.ForeignKey(Voicebottemplatemapping, models.DO_NOTHING, db_column='VoiceBotTemplateMappingID', blank=True, null=True)  # Field name made lowercase.
    startend = models.CharField(db_column='StartEnd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VoiceBotUserTemplate'


class Whatsappflowmapping(models.Model):
    whatsappflowid = models.AutoField(db_column='WhatsAppFlowID', primary_key=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    flowid = models.IntegerField(db_column='FlowID')  # Field name made lowercase.
    flowname = models.CharField(db_column='FlowName', max_length=255)  # Field name made lowercase.
    response = models.TextField(db_column='Response')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    lngmstid = models.ForeignKey(Languagemst, models.DO_NOTHING, db_column='LngMstID')  # Field name made lowercase.
    whatsapptemplatemappingid = models.ForeignKey('Whatsapptemplatemapping', models.DO_NOTHING, db_column='WhatsAppTemplateMappingID')  # Field name made lowercase.
    whatsappflowmstid = models.ForeignKey('Whatsappflowmst', models.DO_NOTHING, db_column='WhatsAppFlowMstID')  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    isstart = models.BooleanField(db_column='IsStart', blank=True, null=True)  # Field name made lowercase.
    nexttemplate = models.CharField(db_column='NextTemplate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WhatsAppFlowMapping'


class Whatsappflowmst(models.Model):
    whatsappflowmstid = models.AutoField(db_column='WhatsAppFlowMstID', primary_key=True)  # Field name made lowercase.
    flowname = models.CharField(db_column='FlowName', max_length=255)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    bankid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankID', blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', related_name='whatsappflowmst_bankmstid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WhatsAppFlowMst'


class Whatsapphistory(models.Model):
    whatsapphistoryid = models.AutoField(db_column='WhatsAppHistoryID', primary_key=True)  # Field name made lowercase.
    whatsappqueueid = models.IntegerField(db_column='WhatsAppQueueID', unique=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    branchmstid = models.ForeignKey(Branchmst, models.DO_NOTHING, db_column='BranchMstID')  # Field name made lowercase.
    loanmstid = models.ForeignKey(Loanmst, models.DO_NOTHING, db_column='LoanMstID')  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    customerid = models.CharField(db_column='CustomerID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', max_length=255)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='ContactNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255)  # Field name made lowercase.
    overdue_amount = models.DecimalField(db_column='Overdue_Amount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    next_emi_amount = models.DecimalField(db_column='Next_EMI_Amount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    next_emi_date = models.DateField(db_column='Next_EMI_Date', blank=True, null=True)  # Field name made lowercase.
    total_collection = models.DecimalField(db_column='Total_Collection', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    latest_collecteddate = models.DateField(db_column='Latest_CollectedDate', blank=True, null=True)  # Field name made lowercase.
    latest_collectedamt = models.DecimalField(db_column='Latest_CollectedAmt', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    issent = models.BooleanField(db_column='IsSent', blank=True, null=True)  # Field name made lowercase.
    isdelivered = models.BooleanField(db_column='IsDelivered', blank=True, null=True)  # Field name made lowercase.
    isread = models.BooleanField(db_column='IsRead', blank=True, null=True)  # Field name made lowercase.
    isresponded = models.BooleanField(db_column='IsResponded', blank=True, null=True)  # Field name made lowercase.
    response = models.TextField(db_column='Response', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    identifier = models.CharField(db_column='Identifier', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lngmstid = models.ForeignKey(Languagemst, models.DO_NOTHING, db_column='LngMstID', blank=True, null=True)  # Field name made lowercase.
    basedon = models.CharField(db_column='BasedOn', blank=True, null=True)  # Field name made lowercase.
    commflowid = models.IntegerField(db_column='CommFlowID', blank=True, null=True)  # Field name made lowercase.
    customercode = models.CharField(db_column='CustomerCode', blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', blank=True, null=True)  # Field name made lowercase.
    flowid = models.IntegerField(db_column='FlowID', blank=True, null=True)  # Field name made lowercase.
    whatsapptemplatemappingid = models.IntegerField(db_column='WhatsAppTemplateMappingID', blank=True, null=True)  # Field name made lowercase.
    overdueamt = models.DecimalField(db_column='OverdueAmt', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    slot = models.CharField(db_column='Slot', max_length=255, blank=True, null=True)  # Field name made lowercase.
    alternativemobilenumber = models.CharField(db_column='AlternativeMobileNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    secondarycustmstid = models.IntegerField(db_column='SecondaryCustMstID', blank=True, null=True)  # Field name made lowercase.
    applicantname = models.CharField(db_column='ApplicantName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coapplicantcontact = models.CharField(db_column='CoApplicantContact', max_length=20, blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', blank=True, null=True)  # Field name made lowercase.
    campaignmstid = models.IntegerField(db_column='CampaignMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WhatsAppHistory'
        unique_together = (('whatsappqueueid', 'createddate'),)


class Whatsappkeymapping(models.Model):
    whatsappkeymappingid = models.AutoField(db_column='WhatsAppKeyMappingID', primary_key=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    authorizationkey = models.CharField(db_column='AuthorizationKey', max_length=255)  # Field name made lowercase.
    apiversion = models.CharField(db_column='APIVersion', max_length=50)  # Field name made lowercase.
    phonenumberid = models.CharField(db_column='PhoneNumberID')  # Field name made lowercase.
    service = models.CharField(db_column='Service', max_length=255)  # Field name made lowercase.
    extra_column1 = models.CharField(db_column='Extra_Column1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extra_column2 = models.CharField(db_column='Extra_Column2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extra_column3 = models.CharField(db_column='Extra_Column3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extra_column4 = models.CharField(db_column='Extra_Column4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extra_column5 = models.CharField(db_column='Extra_Column5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sp_projectid = models.CharField(db_column='SP_ProjectID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sp_password = models.CharField(db_column='SP_Password', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WhatsAppKeyMapping'


class Whatsappqueue(models.Model):
    whatsappqueueid = models.AutoField(db_column='WhatsAppQueueID', primary_key=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    branchmstid = models.ForeignKey(Branchmst, models.DO_NOTHING, db_column='BranchMstID', blank=True, null=True)  # Field name made lowercase.
    loanmstid = models.ForeignKey(Loanmst, models.DO_NOTHING, db_column='LoanMstID', blank=True, null=True)  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customercode = models.CharField(db_column='CustomerCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    overdueamt = models.DecimalField(db_column='OverdueAmt', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn3 = models.CharField(db_column='ExtraColumn3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn4 = models.CharField(db_column='ExtraColumn4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extracolumn5 = models.CharField(db_column='ExtraColumn5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    slot = models.CharField(db_column='Slot', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    basedon = models.CharField(db_column='BasedOn', blank=True, null=True)  # Field name made lowercase.
    commflowid = models.ForeignKey(Commflow, models.DO_NOTHING, db_column='CommFlowID', blank=True, null=True)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='ContactNumber', blank=True, null=True)  # Field name made lowercase.
    flowid = models.IntegerField(db_column='FlowID', blank=True, null=True)  # Field name made lowercase.
    whatsapptemplatemappingid = models.IntegerField(db_column='WhatsAppTemplateMappingID', blank=True, null=True)  # Field name made lowercase.
    customerid = models.CharField(db_column='CustomerID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    next_emi_amount = models.DecimalField(db_column='Next_EMI_Amount', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    next_emi_date = models.DateField(db_column='Next_EMI_Date', blank=True, null=True)  # Field name made lowercase.
    total_collection = models.DecimalField(db_column='Total_Collection', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    latest_collecteddate = models.DateField(db_column='Latest_CollectedDate', blank=True, null=True)  # Field name made lowercase.
    latest_collectedamt = models.DecimalField(db_column='Latest_CollectedAmt', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    response = models.TextField(db_column='Response', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    identifier = models.CharField(db_column='Identifier', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lngmstid = models.IntegerField(db_column='LngMstID', blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', blank=True, null=True)  # Field name made lowercase.
    alternativemobilenumber = models.CharField(db_column='AlternativeMobileNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    secondarycustmstid = models.IntegerField(db_column='SecondaryCustMstID', blank=True, null=True)  # Field name made lowercase.
    applicantname = models.CharField(db_column='ApplicantName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coapplicantcontact = models.CharField(db_column='CoApplicantContact', max_length=20, blank=True, null=True)  # Field name made lowercase.
    campaignmstid = models.IntegerField(db_column='CampaignMstID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WhatsAppQueue'


class Whatsapptemplatemapping(models.Model):
    whatsapptemplatemappingid = models.AutoField(db_column='WhatsAppTemplateMappingID', primary_key=True)  # Field name made lowercase.
    metatemplateid = models.CharField(db_column='MetaTemplateID', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
    templatename = models.CharField(db_column='TemplateName', max_length=255)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    lngmstid = models.ForeignKey(Languagemst, models.DO_NOTHING, db_column='LngMstID')  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=255)  # Field name made lowercase.
    isadmincreated = models.BooleanField(db_column='IsAdminCreated')  # Field name made lowercase.
    extra_column1 = models.CharField(db_column='Extra_Column1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extra_column2 = models.CharField(db_column='Extra_Column2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extra_column3 = models.CharField(db_column='Extra_Column3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extra_column4 = models.CharField(db_column='Extra_Column4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extra_column5 = models.CharField(db_column='Extra_Column5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    templatebody = models.CharField(db_column='TemplateBody', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WhatsAppTemplateMapping'


class Whatsappusertemplate(models.Model):
    whatsappusertemplateid = models.AutoField(db_column='WhatsAppUserTemplateID', primary_key=True)  # Field name made lowercase.
    templatename = models.CharField(db_column='TemplateName', max_length=255)  # Field name made lowercase.
    bankmstid = models.ForeignKey(Bankmst, models.DO_NOTHING, db_column='BankMstID')  # Field name made lowercase.
    employeemstid = models.ForeignKey(Employeemst, models.DO_NOTHING, db_column='EmployeeMstID', blank=True, null=True)  # Field name made lowercase.
    variable1 = models.CharField(db_column='Variable1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    variable2 = models.CharField(db_column='Variable2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    variable3 = models.CharField(db_column='Variable3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    variable4 = models.CharField(db_column='Variable4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    variable5 = models.CharField(db_column='Variable5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    variable6 = models.CharField(db_column='Variable6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    variable7 = models.CharField(db_column='Variable7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    variable8 = models.CharField(db_column='Variable8', max_length=255, blank=True, null=True)  # Field name made lowercase.
    variable9 = models.CharField(db_column='Variable9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    variable10 = models.CharField(db_column='Variable10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    button1 = models.CharField(db_column='Button1', blank=True, null=True)  # Field name made lowercase.
    button2 = models.CharField(db_column='Button2', blank=True, null=True)  # Field name made lowercase.
    button3 = models.CharField(db_column='Button3', blank=True, null=True)  # Field name made lowercase.
    button4 = models.CharField(db_column='Button4', blank=True, null=True)  # Field name made lowercase.
    whatsapptemplatemappingid = models.ForeignKey(Whatsapptemplatemapping, models.DO_NOTHING, db_column='WhatsAppTemplateMappingID', blank=True, null=True)  # Field name made lowercase.
    response1 = models.CharField(db_column='Response1', blank=True, null=True)  # Field name made lowercase.
    response2 = models.CharField(db_column='Response2', blank=True, null=True)  # Field name made lowercase.
    response3 = models.CharField(db_column='Response3', blank=True, null=True)  # Field name made lowercase.
    response4 = models.CharField(db_column='Response4', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WhatsAppUserTemplate'


class WhatsappMessages(models.Model):
    whatsappmessageid = models.AutoField(db_column='WhatsAppMessageID', primary_key=True)  # Field name made lowercase.
    messagedate = models.DateTimeField(db_column='MessageDate', blank=True, null=True)  # Field name made lowercase.
    whatsappqueueid = models.IntegerField(db_column='WhatsAppQueueID', blank=True, null=True)  # Field name made lowercase.
    messageid = models.CharField(db_column='MessageID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    assignedto = models.CharField(db_column='AssignedTo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sender = models.CharField(db_column='Sender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customernumber = models.CharField(db_column='CustomerNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    loanmstid = models.IntegerField(db_column='LoanMstID', blank=True, null=True)  # Field name made lowercase.
    button = models.CharField(db_column='Button', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    identifier = models.CharField(db_column='Identifier', blank=True, null=True)  # Field name made lowercase.
    whatsappusertemplateid = models.IntegerField(db_column='WhatsAppUserTemplateID', blank=True, null=True)  # Field name made lowercase.
    extracolumn1 = models.CharField(db_column='ExtraColumn1', blank=True, null=True)  # Field name made lowercase.
    extracolumn2 = models.CharField(db_column='ExtraColumn2', blank=True, null=True)  # Field name made lowercase.
    bankmstid = models.IntegerField(db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    extracolumn = models.CharField(blank=True, null=True)
    gapshapreplyid = models.CharField(db_column='GapshapReplyID', max_length=500, blank=True, null=True)  # Field name made lowercase.
    id = models.BigAutoField()
    campaignmstid = models.IntegerField(db_column='CampaignMstID', blank=True, null=True)  # Field name made lowercase.
    status_callback = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WhatsApp_Messages'


class Whatsappvariablemapping(models.Model):
    whatsappvariablemappingid = models.AutoField(db_column='WhatsappVariableMappingID', primary_key=True)  # Field name made lowercase.
    whatsapptemplatemappingid = models.ForeignKey(Whatsapptemplatemapping, models.DO_NOTHING, db_column='WhatsAppTemplateMappingID', blank=True, null=True)  # Field name made lowercase.
    variableno = models.IntegerField(db_column='VariableNo', blank=True, null=True)  # Field name made lowercase.
    variablefield = models.CharField(db_column='VariableField', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WhatsappVariableMapping'


class Wrongnumberhistory(models.Model):
    bankmstid = models.IntegerField(db_column='BankMstID')  # Field name made lowercase.
    customermstid = models.IntegerField(db_column='CustomerMstID', blank=True, null=True)  # Field name made lowercase.
    loanmstid = models.IntegerField(db_column='LoanMstID', blank=True, null=True)  # Field name made lowercase.
    previousnumber = models.CharField(db_column='PreviousNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    updatednumber = models.CharField(db_column='UpdatedNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WrongNumberHistory'


class Account(models.Model):
    credit_report_id = models.TextField(blank=True, null=True)
    los_app_id = models.CharField(db_column='LOS-APP-ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    candidate_id = models.CharField(db_column='CANDIDATE - ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    customer_id_mbr_id = models.FloatField(db_column='CUSTOMER ID/MBR ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    branch = models.TextField(db_column='BRANCH', blank=True, null=True)  # Field name made lowercase.
    kendra = models.TextField(db_column='KENDRA', blank=True, null=True)  # Field name made lowercase.
    self_indicator = models.BooleanField(db_column='SELF-INDICATOR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    match_type = models.TextField(db_column='MATCH-TYPE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    acc_num = models.TextField(db_column='ACC-NUM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    credit_grantor = models.TextField(blank=True, null=True)
    account_type = models.TextField(blank=True, null=True)
    contributor_type = models.TextField(db_column='CONTRIBUTOR-TYPE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_reported = models.TextField(db_column='DATE-REPORTED', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ownership_ind = models.TextField(db_column='OWNERSHIP-IND', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    account_status = models.TextField(db_column='ACCOUNT-STATUS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    disbursed_dt = models.TextField(db_column='DISBURSED-DT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    close_dt = models.TextField(db_column='CLOSE-DT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_payment_date = models.TextField(db_column='LAST-PAYMENT-DATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    credit_limit_sanc_amt = models.TextField(db_column='CREDIT-LIMIT/SANC AMT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_disbursed_amt_high_credit = models.TextField(db_column=' DISBURSED-AMT/HIGH CREDIT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_installment_amt = models.TextField(db_column=' INSTALLMENT-AMT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_current_bal = models.TextField(db_column=' CURRENT-BAL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    installment_frequency = models.TextField(db_column='INSTALLMENT-FREQUENCY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    write_off_date = models.TextField(db_column='WRITE-OFF-DATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_overdue_amt = models.TextField(db_column=' OVERDUE-AMT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_write_off_amt = models.FloatField(db_column=' WRITE-OFF-AMT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    asset_class = models.TextField(db_column='ASSET_CLASS', blank=True, null=True)  # Field name made lowercase.
    field_account_remarks = models.TextField(db_column=' ACCOUNT-REMARKS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    linked_accounts = models.TextField(db_column='LINKED-ACCOUNTS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reported_date_hist_field = models.TextField(db_column='REPORTED DATE - HIST ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    dpd_hist = models.TextField(db_column='DPD - HIST', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_class_hist_field = models.TextField(db_column='ASSET CLASS - HIST ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    high_crd_hist_field = models.TextField(db_column='HIGH CRD - HIST ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cur_bal_hist_field = models.TextField(db_column='CUR BAL - HIST ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    das_hist_field = models.TextField(db_column='DAS - HIST ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    amt_overdue_hist_field = models.TextField(db_column='AMT OVERDUE - HIST ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    amt_paid_hist_field = models.TextField(db_column='AMT PAID - HIST ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    income_field = models.FloatField(db_column='INCOME ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    field_income_indicator_field = models.TextField(db_column=' INCOME INDICATOR ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    tenure_field = models.FloatField(db_column='TENURE ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    field_occupation = models.TextField(db_column=' OCCUPATION', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    unnamed_41 = models.FloatField(db_column='Unnamed: 41', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'account'


class ArthsiddhiBankMobileNumberUpdateReportSheet1(models.Model):
    cust_id = models.CharField(db_column='Cust ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(max_length=50, blank=True, null=True)
    new_mobile_number = models.CharField(db_column='new mobile number', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'arthsiddhi_bank_mobile_number_update_report_sheet1'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthenticationBankdetails(models.Model):
    bankid = models.AutoField(db_column='BankID')  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bank_db = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField()
    bank_code = models.CharField(max_length=100, blank=True, null=True)
    gcp_folder = models.CharField(max_length=250, blank=True, null=True)
    otp_2fa = models.BooleanField(db_column='otp_2FA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'authentication_bankdetails'


class AuthenticationBranchdetails(models.Model):
    branchid = models.AutoField(db_column='BranchID')  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    status = models.BooleanField()
    bank_id_id = models.IntegerField(db_column='Bank_id_id')  # Field name made lowercase.
    cbsbranchid = models.BigIntegerField(db_column='CBSBranchID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'authentication_branchdetails'


class AuthenticationMstUsrtbl(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    id = models.AutoField()
    contactno = models.BigIntegerField(db_column='ContactNo', blank=True, null=True)  # Field name made lowercase.
    isadmin = models.BooleanField(db_column='IsAdmin')  # Field name made lowercase.
    bu_type = models.CharField(db_column='BU_type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(blank=True, null=True)
    callno = models.CharField(max_length=255, blank=True, null=True)
    smartplugin = models.CharField(db_column='smartPlugin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bank_id_id = models.IntegerField(db_column='Bank_id_id', blank=True, null=True)  # Field name made lowercase.
    branchid_id = models.IntegerField(db_column='BranchID_id', blank=True, null=True)  # Field name made lowercase.
    bank_user_id = models.CharField(max_length=250, blank=True, null=True)
    designation = models.CharField(max_length=250, blank=True, null=True)
    geography = models.CharField(max_length=250, blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authentication_mst_usrtbl'


class Bankcontrols(models.Model):
    controlid = models.AutoField(db_column='ControlID', primary_key=True)  # Field name made lowercase.
    bankmstid = models.OneToOneField(Bankmst, models.DO_NOTHING, db_column='BankMstID', blank=True, null=True)  # Field name made lowercase.
    json = models.JSONField(db_column='Json', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bankcontrols'


class BmViewCustomermst(models.Model):
    id = models.BigAutoField()
    customerinfoid = models.CharField(max_length=50, blank=True, null=True)
    applicantname = models.CharField(max_length=255, blank=True, null=True)
    mobile_no = models.CharField(max_length=15, blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    bank_code = models.IntegerField()
    assigned_to = models.CharField(max_length=20, blank=True, null=True)
    date_added = models.DateField()

    class Meta:
        managed = False
        db_table = 'bm_view_customermst'


class BmViewLoanmst(models.Model):
    id = models.BigAutoField()
    customerid = models.CharField(db_column='CustomerId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=150, blank=True, null=True)  # Field name made lowercase.
    paymentfrequency = models.CharField(db_column='PaymentFrequency', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dateopen = models.DateField(db_column='DateOpen', blank=True, null=True)  # Field name made lowercase.
    disburseamount = models.DecimalField(db_column='DisburseAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dateclose = models.DateField(db_column='DateClose', blank=True, null=True)  # Field name made lowercase.
    emiamount = models.DecimalField(db_column='EMIAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lastmodifieddate = models.DateField(db_column='LastModifiedDate', blank=True, null=True)  # Field name made lowercase.
    rateofinterest = models.DecimalField(db_column='RateOfInterest', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    repaymenttenure = models.IntegerField(db_column='RepaymentTenure', blank=True, null=True)  # Field name made lowercase.
    coapplicantcustomerid = models.CharField(db_column='COAPPLICANTCustomerID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coapplicanttype = models.IntegerField(db_column='COAPPLICANTType', blank=True, null=True)  # Field name made lowercase.
    guarantorid = models.CharField(db_column='GUARANTORID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    guarantortype = models.IntegerField(db_column='GuarantorType', blank=True, null=True)  # Field name made lowercase.
    bmid = models.IntegerField(db_column='BMID', blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.
    branchmanager = models.CharField(db_column='BranchManager', max_length=255, blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    datereported = models.DateField(db_column='DateReported', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bm_view_loanmst'


class BmViewPaymentclaims(models.Model):
    id = models.BigAutoField()
    bank_id = models.IntegerField()
    assigned_to = models.CharField(max_length=10, blank=True, null=True)
    disbursement_id = models.CharField(max_length=50, blank=True, null=True)
    claim_date = models.DateTimeField()
    claim_amount = models.IntegerField(blank=True, null=True)
    bot_channel = models.CharField(max_length=50, blank=True, null=True)
    bot_queue_id = models.IntegerField(blank=True, null=True)
    claim_status = models.BooleanField(blank=True, null=True)
    is_payment = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bm_view_paymentclaims'


class BmViewPaymentdenials(models.Model):
    id = models.BigAutoField()
    bank_id = models.IntegerField()
    assigned_to = models.CharField(max_length=10, blank=True, null=True)
    disbursement_id = models.CharField(max_length=50, blank=True, null=True)
    denial_date = models.DateTimeField()
    denial_amount = models.IntegerField(blank=True, null=True)
    bot_channel = models.CharField(max_length=50, blank=True, null=True)
    bot_queue_id = models.IntegerField(blank=True, null=True)
    denial_status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bm_view_paymentdenials'


class BmViewPromises(models.Model):
    id = models.BigAutoField()
    bank_id = models.IntegerField()
    created_on = models.DateField(blank=True, null=True)
    late_collections = models.BooleanField()
    disbursement_id = models.CharField(max_length=100, blank=True, null=True)
    promise_date = models.DateTimeField()
    promise_amount = models.IntegerField(blank=True, null=True)
    promise_status = models.IntegerField()
    bot_channel = models.CharField(max_length=50, blank=True, null=True)
    bot_queue_id = models.IntegerField(blank=True, null=True)
    customer_commit = models.BooleanField()
    mode = models.CharField(max_length=50, blank=True, null=True)
    assigned_to_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bm_view_promises'


class CampaignBlasterusertemplate(models.Model):
    blasterusertemplateid = models.AutoField(db_column='BlasterUserTemplateID', primary_key=True)  # Field name made lowercase.
    templatename = models.CharField(db_column='TemplateName', max_length=255)  # Field name made lowercase.
    templatebody = models.TextField(db_column='TemplateBody')  # Field name made lowercase.
    bankmstid = models.IntegerField(db_column='BankMstID')  # Field name made lowercase.
    employeemstid = models.IntegerField(db_column='EmployeeMstID')  # Field name made lowercase.
    variablenumber = models.IntegerField(db_column='VariableNumber')  # Field name made lowercase.
    variablefield = models.CharField(db_column='VariableField', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'campaign_blasterusertemplate'


class CampaignCount(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaign_count'


class Collection(models.Model):
    customerid = models.CharField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branchid = models.CharField(db_column='BranchID', blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mobile_number = models.CharField(db_column='Mobile Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    od_amount = models.CharField(db_column='OD AMOUNT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_outstanding = models.CharField(db_column='TOTAL OUTSTANDING', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    next_emi_amount = models.CharField(db_column='Next_EMI_Amount', blank=True, null=True)  # Field name made lowercase.
    next_emi_date = models.CharField(db_column='Next_EMI_Date', max_length=50, blank=True, null=True)  # Field name made lowercase.
    end_payment_date = models.CharField(db_column='End Payment Date', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dpd = models.CharField(db_column='DPD', blank=True, null=True)  # Field name made lowercase.
    number_03_05_2025 = models.IntegerField(db_column='03-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_04_05_2025 = models.IntegerField(db_column='04-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_05_05_2025 = models.IntegerField(db_column='05-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_06_05_2025 = models.IntegerField(db_column='06-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_07_05_2025 = models.IntegerField(db_column='07-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_08_05_2025 = models.IntegerField(db_column='08-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_09_05_2025 = models.IntegerField(db_column='09-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_10_05_2025 = models.IntegerField(db_column='10-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_11_05_2025 = models.IntegerField(db_column='11-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_05_2025 = models.IntegerField(db_column='12-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_13_05_2025 = models.IntegerField(db_column='13-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_14_05_2025 = models.IntegerField(db_column='14-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15_05_2025 = models.IntegerField(db_column='15-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_16_05_2025 = models.IntegerField(db_column='16-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_05_2025 = models.IntegerField(db_column='17-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_19_05_2025 = models.IntegerField(db_column='19-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_20_05_2025 = models.IntegerField(db_column='20-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_21_05_2025 = models.IntegerField(db_column='21-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_22_05_2025 = models.IntegerField(db_column='22-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_23_05_2025 = models.IntegerField(db_column='23-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_24_05_2025 = models.IntegerField(db_column='24-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_26_05_2025 = models.IntegerField(db_column='26-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_27_05_2025 = models.IntegerField(db_column='27-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_28_05_2025 = models.IntegerField(db_column='28-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_29_05_2025 = models.IntegerField(db_column='29-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_30_05_2025 = models.IntegerField(db_column='30-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_31_05_2025 = models.IntegerField(db_column='31-05-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_02_06_2025 = models.IntegerField(db_column='02-06-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_03_06_2025 = models.IntegerField(db_column='03-06-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_04_06_2025 = models.IntegerField(db_column='04-06-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_05_06_2025 = models.IntegerField(db_column='05-06-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_06_06_2025 = models.IntegerField(db_column='06-06-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_07_06_2025 = models.IntegerField(db_column='07-06-2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'collection'


class CommflowId(models.Model):
    commflowid = models.IntegerField(db_column='CommFlowID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'commflow_id'


class CommunicationType(models.Model):
    communicationtype = models.CharField(db_column='CommunicationType', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'communication_type'


class CustomerChannelCollectionData(models.Model):
    id = models.BigAutoField()
    disbursementid = models.CharField(max_length=200, blank=True, null=True)
    total_amt_collected = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    channel = models.IntegerField(blank=True, null=True)
    as_on_date = models.DateField(blank=True, null=True)
    assigned_to = models.CharField(max_length=50, blank=True, null=True)
    pending_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    collected_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_channel_collection_data'


class CustomerDayWizeSummarize(models.Model):
    id = models.BigAutoField()
    customerinfoid = models.CharField(max_length=255, blank=True, null=True)
    bankname = models.CharField(db_column='BankName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.CharField(max_length=100, blank=True, null=True)
    loantype = models.CharField(max_length=255, blank=True, null=True)
    productname = models.CharField(max_length=255, blank=True, null=True)
    repayment_frequency = models.CharField(max_length=50, blank=True, null=True)
    disbursementdate = models.DateField(blank=True, null=True)
    disbursedamt = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    loan_closing_date = models.DateField(blank=True, null=True)
    bank_code = models.IntegerField(blank=True, null=True)
    assigned_to = models.CharField(max_length=255, blank=True, null=True)
    applicantname = models.CharField(max_length=255, blank=True, null=True)
    mobile_no = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    latest_collected_date = models.DateTimeField(blank=True, null=True)
    latest_collected_amt = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    upcoming_emi_date = models.TextField(blank=True, null=True)
    upcoming_emi_amt = models.FloatField(blank=True, null=True)
    previous_emi_date = models.TextField(blank=True, null=True)
    previous_emi_amt = models.FloatField(blank=True, null=True)
    remaining_installments = models.IntegerField(blank=True, null=True)
    user_dpd_max = models.IntegerField(blank=True, null=True)
    pending_amount = models.FloatField(blank=True, null=True)
    loan_classification = models.TextField(blank=True, null=True)
    total_outstanding = models.FloatField(blank=True, null=True)
    principle_outstanding = models.FloatField(blank=True, null=True)
    as_on_date = models.DateField(blank=True, null=True)
    user_dpd_max_prev_day = models.IntegerField(blank=True, null=True)
    bucket = models.CharField(max_length=50, blank=True, null=True)
    payment_mode = models.IntegerField(blank=True, null=True)
    activity_start_date = models.DateField(blank=True, null=True)
    previous_ecs_date = models.TextField(blank=True, null=True)
    upcoming_ecs_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_day_wize_summarize'


class DashboardCallhistory(models.Model):
    id = models.UUIDField()
    call_id = models.CharField(max_length=1000, blank=True, null=True)
    call_time = models.DateTimeField(blank=True, null=True)
    client_name = models.CharField(max_length=300, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    option = models.CharField(max_length=1000, blank=True, null=True)
    conversation = models.TextField(blank=True, null=True)  # This field type is a guess.
    conversation_json = models.JSONField(blank=True, null=True)
    recording = models.CharField(max_length=1000, blank=True, null=True)
    call_duration = models.IntegerField(blank=True, null=True)
    sentiment = models.CharField(max_length=15, blank=True, null=True)
    last_modifiedby = models.CharField(max_length=512, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    view_count = models.IntegerField(blank=True, null=True)
    conclusion = models.CharField(max_length=512, blank=True, null=True)
    modified_time = models.CharField(max_length=512, blank=True, null=True)
    further_assistance = models.BooleanField(blank=True, null=True)
    right_party = models.BooleanField(blank=True, null=True)
    dispute_raised = models.BooleanField(blank=True, null=True)
    cust_threat = models.BooleanField(blank=True, null=True)
    reconfirm_ptp = models.BooleanField(blank=True, null=True)
    abusive_words = models.BooleanField(blank=True, null=True)
    user_time = models.TextField(blank=True, null=True)
    audio_name = models.CharField(max_length=512, blank=True, null=True)
    log_file_name = models.CharField(max_length=1000, blank=True, null=True)
    abnormal_disconnect = models.BooleanField(blank=True, null=True)
    customer_disconnect = models.BooleanField(blank=True, null=True)
    bot_disconnect = models.BooleanField(blank=True, null=True)
    date_by_customer = models.CharField(max_length=512, blank=True, null=True)
    time_by_customer = models.CharField(max_length=512, blank=True, null=True)
    intent_flow = models.TextField(blank=True, null=True)  # This field type is a guess.
    loan_number = models.CharField(max_length=512, blank=True, null=True)
    reallocate = models.BooleanField(blank=True, null=True)
    promise_date = models.DateField(blank=True, null=True)
    bank_code = models.CharField(max_length=200, blank=True, null=True)
    bank_name = models.CharField(max_length=200, blank=True, null=True)
    assigned_to = models.CharField(max_length=20, blank=True, null=True)
    emi_amount = models.FloatField(blank=True, null=True)
    dpd_days = models.IntegerField(blank=True, null=True)
    suggetion = models.CharField(max_length=2000, blank=True, null=True)
    customerinfo_id = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    mode_of_payment = models.CharField(max_length=50, blank=True, null=True)
    emi_date = models.DateField(blank=True, null=True)
    bucket = models.CharField(blank=True, null=True)
    loantype = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_callhistory'


class DashboardCallhistoryBackup(models.Model):
    id = models.UUIDField(blank=True, null=True)
    call_id = models.CharField(max_length=1000, blank=True, null=True)
    call_time = models.DateTimeField(blank=True, null=True)
    client_name = models.CharField(max_length=300, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    option = models.CharField(max_length=1000, blank=True, null=True)
    conversation = models.TextField(blank=True, null=True)  # This field type is a guess.
    conversation_json = models.JSONField(blank=True, null=True)
    recording = models.CharField(max_length=1000, blank=True, null=True)
    call_duration = models.IntegerField(blank=True, null=True)
    sentiment = models.CharField(max_length=15, blank=True, null=True)
    last_modifiedby = models.CharField(max_length=512, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    view_count = models.IntegerField(blank=True, null=True)
    conclusion = models.CharField(max_length=512, blank=True, null=True)
    modified_time = models.CharField(max_length=512, blank=True, null=True)
    further_assistance = models.BooleanField(blank=True, null=True)
    right_party = models.BooleanField(blank=True, null=True)
    dispute_raised = models.BooleanField(blank=True, null=True)
    cust_threat = models.BooleanField(blank=True, null=True)
    reconfirm_ptp = models.BooleanField(blank=True, null=True)
    abusive_words = models.BooleanField(blank=True, null=True)
    user_time = models.TextField(blank=True, null=True)
    audio_name = models.CharField(max_length=512, blank=True, null=True)
    log_file_name = models.CharField(max_length=1000, blank=True, null=True)
    abnormal_disconnect = models.BooleanField(blank=True, null=True)
    customer_disconnect = models.BooleanField(blank=True, null=True)
    bot_disconnect = models.BooleanField(blank=True, null=True)
    date_by_customer = models.CharField(max_length=512, blank=True, null=True)
    time_by_customer = models.CharField(max_length=512, blank=True, null=True)
    intent_flow = models.TextField(blank=True, null=True)  # This field type is a guess.
    loan_number = models.CharField(max_length=512, blank=True, null=True)
    reallocate = models.BooleanField(blank=True, null=True)
    promise_date = models.DateField(blank=True, null=True)
    bank_code = models.CharField(max_length=200, blank=True, null=True)
    bank_name = models.CharField(max_length=200, blank=True, null=True)
    assigned_to = models.CharField(max_length=20, blank=True, null=True)
    emi_amount = models.FloatField(blank=True, null=True)
    dpd_days = models.IntegerField(blank=True, null=True)
    suggetion = models.CharField(max_length=2000, blank=True, null=True)
    customerinfo_id = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    mode_of_payment = models.CharField(max_length=50, blank=True, null=True)
    emi_date = models.DateField(blank=True, null=True)
    loantype = models.CharField(max_length=250, blank=True, null=True)
    bucket = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_callhistory_backup'


class DashboardCallingqueue(models.Model):
    id = models.UUIDField()
    call_id = models.CharField(max_length=1000, blank=True, null=True)
    loan_number = models.CharField(max_length=50, blank=True, null=True)
    client_name = models.CharField(max_length=1000, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bank_code = models.CharField(max_length=200, blank=True, null=True)
    option = models.CharField(max_length=512, blank=True, null=True)
    allocated_on = models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(max_length=200, blank=True, null=True)
    emi_amount = models.FloatField(blank=True, null=True)
    dpd_days = models.IntegerField(blank=True, null=True)
    emi_date = models.DateField(blank=True, null=True)
    next_meet_date = models.DateField(blank=True, null=True)
    due_installments = models.IntegerField(blank=True, null=True)
    call_connected = models.BooleanField(blank=True, null=True)
    call_tried = models.IntegerField(blank=True, null=True)
    bank_name = models.CharField(max_length=2000, blank=True, null=True)
    assigned_to = models.CharField(max_length=200, blank=True, null=True)
    created_on = models.DateField(blank=True, null=True)
    call_date = models.DateField(blank=True, null=True)
    reallocated = models.BooleanField(blank=True, null=True)
    reallocated_on = models.DateField(blank=True, null=True)
    escalated = models.BooleanField(blank=True, null=True)
    autocomplete = models.BooleanField(blank=True, null=True)
    wrong_number = models.BooleanField(blank=True, null=True)
    promise = models.BooleanField(blank=True, null=True)
    mature_date = models.DateField(blank=True, null=True)
    fd_amount = models.FloatField(blank=True, null=True)
    is_ivr = models.BooleanField(blank=True, null=True)
    emi_count = models.CharField(max_length=200, blank=True, null=True)
    latest_date = models.DateField(blank=True, null=True)
    reattempt_count = models.IntegerField(blank=True, null=True)
    last_call_tried = models.DateTimeField(blank=True, null=True)
    customerinfo_id = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    div_name = models.CharField(max_length=100, blank=True, null=True)
    reg_name = models.CharField(max_length=100, blank=True, null=True)
    hub_name = models.CharField(max_length=100, blank=True, null=True)
    branch_name = models.CharField(max_length=100, blank=True, null=True)
    var1 = models.CharField(max_length=500, blank=True, null=True)
    var2 = models.CharField(max_length=500, blank=True, null=True)
    var3 = models.CharField(max_length=500, blank=True, null=True)
    var4 = models.CharField(max_length=500, blank=True, null=True)
    var5 = models.CharField(max_length=500, blank=True, null=True)
    var6 = models.CharField(max_length=500, blank=True, null=True)
    var7 = models.CharField(max_length=500, blank=True, null=True)
    var8 = models.CharField(max_length=500, blank=True, null=True)
    var9 = models.CharField(max_length=500, blank=True, null=True)
    var10 = models.CharField(max_length=500, blank=True, null=True)
    loantype = models.CharField(blank=True, null=True)
    bucket = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_callingqueue'


class DashboardCallingqueueBackup(models.Model):
    id = models.UUIDField(blank=True, null=True)
    call_id = models.CharField(max_length=1000, blank=True, null=True)
    loan_number = models.CharField(max_length=50, blank=True, null=True)
    client_name = models.CharField(max_length=1000, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bank_code = models.CharField(max_length=200, blank=True, null=True)
    option = models.CharField(max_length=512, blank=True, null=True)
    allocated_on = models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(max_length=200, blank=True, null=True)
    emi_amount = models.FloatField(blank=True, null=True)
    dpd_days = models.IntegerField(blank=True, null=True)
    emi_date = models.DateField(blank=True, null=True)
    next_meet_date = models.DateField(blank=True, null=True)
    due_installments = models.IntegerField(blank=True, null=True)
    call_connected = models.BooleanField(blank=True, null=True)
    call_tried = models.IntegerField(blank=True, null=True)
    bank_name = models.CharField(max_length=2000, blank=True, null=True)
    assigned_to = models.CharField(max_length=200, blank=True, null=True)
    created_on = models.DateField(blank=True, null=True)
    call_date = models.DateField(blank=True, null=True)
    reallocated = models.BooleanField(blank=True, null=True)
    reallocated_on = models.DateField(blank=True, null=True)
    escalated = models.BooleanField(blank=True, null=True)
    autocomplete = models.BooleanField(blank=True, null=True)
    wrong_number = models.BooleanField(blank=True, null=True)
    promise = models.BooleanField(blank=True, null=True)
    mature_date = models.DateField(blank=True, null=True)
    fd_amount = models.FloatField(blank=True, null=True)
    is_ivr = models.BooleanField(blank=True, null=True)
    emi_count = models.CharField(max_length=200, blank=True, null=True)
    latest_date = models.DateField(blank=True, null=True)
    reattempt_count = models.IntegerField(blank=True, null=True)
    last_call_tried = models.DateTimeField(blank=True, null=True)
    customerinfo_id = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    div_name = models.CharField(max_length=100, blank=True, null=True)
    reg_name = models.CharField(max_length=100, blank=True, null=True)
    hub_name = models.CharField(max_length=100, blank=True, null=True)
    branch_name = models.CharField(max_length=100, blank=True, null=True)
    var1 = models.CharField(max_length=500, blank=True, null=True)
    var2 = models.CharField(max_length=500, blank=True, null=True)
    var3 = models.CharField(max_length=500, blank=True, null=True)
    var4 = models.CharField(max_length=500, blank=True, null=True)
    var5 = models.CharField(max_length=500, blank=True, null=True)
    var6 = models.CharField(max_length=500, blank=True, null=True)
    var7 = models.CharField(max_length=500, blank=True, null=True)
    var8 = models.CharField(max_length=500, blank=True, null=True)
    var9 = models.CharField(max_length=500, blank=True, null=True)
    var10 = models.CharField(max_length=500, blank=True, null=True)
    loantype = models.CharField(max_length=250, blank=True, null=True)
    bucket = models.CharField(max_length=25, blank=True, null=True)
    rellocated_on = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_callingqueue_backup'


class DashboardData(models.Model):
    json_agg = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'dashboard_data'


class DatesTable(models.Model):
    date = models.DateField()
    periodicid = models.IntegerField(blank=True, null=True)
    commflowid = models.ForeignKey(Commflow, models.DO_NOTHING, db_column='commflowid')

    class Meta:
        managed = False
        db_table = 'dates_table'


class Debtcollectioncallhistory(models.Model):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    customer_name = models.CharField(max_length=200, blank=True, null=True)
    customer_id = models.CharField(max_length=200, blank=True, null=True)
    call_id = models.CharField(max_length=1000, blank=True, null=True)
    call_time = models.DateTimeField(blank=True, null=True)
    recording = models.TextField(blank=True, null=True)
    call_duration = models.IntegerField(blank=True, null=True)
    conclusion = models.CharField(max_length=512, blank=True, null=True)
    call_summary_notes = models.CharField(max_length=1024, blank=True, null=True)
    conversation_json = models.JSONField(blank=True, null=True)
    mode_of_payment = models.CharField(max_length=50, blank=True, null=True)
    promise_date = models.DateField(blank=True, null=True)
    promise_amount = models.FloatField(blank=True, null=True)
    disconnect_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'debtcollectioncallhistory'


class Debtcollectioncallqueue(models.Model):
    call_id = models.CharField(max_length=1000, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    customer_name = models.CharField(max_length=200, blank=True, null=True)
    partner_company_name = models.CharField(max_length=200, blank=True, null=True)
    customer_id = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    invoice_no = models.CharField(max_length=100, blank=True, null=True)
    product = models.CharField(max_length=200, blank=True, null=True)
    total_outstanding = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ocp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    invoice_overdue = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    interest_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    call_connected = models.BooleanField(blank=True, null=True)
    call_tried = models.IntegerField(blank=True, null=True)
    calling_status = models.BooleanField()
    call_date = models.DateField(blank=True, null=True)
    last_payment_date = models.DateField(blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    reattempt_count = models.IntegerField()
    last_call_tried = models.DateTimeField(blank=True, null=True)
    offer = models.CharField(max_length=1000, blank=True, null=True)
    cd_valid_till = models.DateField(blank=True, null=True)
    cd_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_cd_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'debtcollectioncallqueue'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(Usermst, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DynamicSql(models.Model):
    generated_query = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dynamic_sql'


class Employeeraw(models.Model):
    employeeid = models.CharField(max_length=50, blank=True, null=True)
    employeename = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    reportingto = models.CharField(max_length=50, blank=True, null=True)
    mobileno = models.CharField(max_length=20, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    bankmstid = models.IntegerField(blank=True, null=True)
    reportingtoname = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employeeraw'


class EngagementData(models.Model):
    json_agg = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'engagement_data'


class Envnv(models.Model):
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    disbursementid = models.CharField(db_column='DisbursementID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchID', blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mobile_number = models.IntegerField(db_column='Mobile Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    od_amount = models.IntegerField(db_column='OD AMOUNT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_outstanding = models.IntegerField(db_column='TOTAL OUTSTANDING', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    next_emi_amount = models.IntegerField(db_column='Next_EMI_Amount', blank=True, null=True)  # Field name made lowercase.
    next_emi_date = models.CharField(db_column='Next_EMI_Date', max_length=50, blank=True, null=True)  # Field name made lowercase.
    end_payment_date = models.CharField(db_column='End Payment Date', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_3_5_2025 = models.IntegerField(db_column='3/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_4_5_2025 = models.IntegerField(db_column='4/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5_5_2025 = models.IntegerField(db_column='5/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_6_5_2025 = models.IntegerField(db_column='6/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_7_5_2025 = models.IntegerField(db_column='7/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_8_5_2025 = models.IntegerField(db_column='8/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_9_5_2025 = models.IntegerField(db_column='9/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_10_5_2025 = models.IntegerField(db_column='10/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_11_5_2025 = models.IntegerField(db_column='11/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_5_2025 = models.IntegerField(db_column='12/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_13_5_2025 = models.IntegerField(db_column='13/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_14_5_2025 = models.IntegerField(db_column='14/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15_5_2025 = models.IntegerField(db_column='15/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_16_5_2025 = models.IntegerField(db_column='16/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_5_2025 = models.IntegerField(db_column='17/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_19_5_2025 = models.CharField(db_column='19/5/2025', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_20_5_2025 = models.IntegerField(db_column='20/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_21_5_2025 = models.IntegerField(db_column='21/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_22_5_2025 = models.IntegerField(db_column='22/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_23_5_2025 = models.IntegerField(db_column='23/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_24_5_2025 = models.IntegerField(db_column='24/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_26_5_2025 = models.IntegerField(db_column='26/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_27_5_2025 = models.IntegerField(db_column='27/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_28_5_2025 = models.IntegerField(db_column='28/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_29_5_2025 = models.IntegerField(db_column='29/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_30_5_2025 = models.IntegerField(db_column='30/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_31_5_2025 = models.IntegerField(db_column='31/5/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2_6_2025 = models.IntegerField(db_column='2/6/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_6_2025 = models.IntegerField(db_column='3/6/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_4_6_2025 = models.IntegerField(db_column='4/6/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5_6_2025 = models.IntegerField(db_column='5/6/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_6_6_2025 = models.IntegerField(db_column='6/6/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_7_6_2025 = models.IntegerField(db_column='7/6/2025', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'envnv'


class ExtracolumnMapping(models.Model):
    bankmstid = models.IntegerField(blank=True, null=True)
    columnname = models.CharField(max_length=255, blank=True, null=True)
    referencename = models.CharField(max_length=255, blank=True, null=True)
    tablename = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'extracolumn_mapping'


class Extratable(models.Model):
    extra_col_1 = models.CharField(max_length=255, blank=True, null=True)
    extra_col_2 = models.CharField(max_length=255, blank=True, null=True)
    extra_col_3 = models.IntegerField(blank=True, null=True)
    extra_col_4 = models.FloatField(blank=True, null=True)
    extra_col_5 = models.CharField(max_length=255, blank=True, null=True)
    extra_col_6 = models.CharField(max_length=255, blank=True, null=True)
    extra_col_7 = models.CharField(max_length=255, blank=True, null=True)
    extra_col_8 = models.CharField(max_length=255, blank=True, null=True)
    extra_col_9 = models.CharField(max_length=255, blank=True, null=True)
    extra_col_10 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'extratable'


class FilterCount(models.Model):
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filter_count'


class Geographyraw(models.Model):
    bucode = models.CharField(max_length=50, blank=True, null=True)
    buname = models.CharField(max_length=100, blank=True, null=True)
    reportingto = models.CharField(max_length=50, blank=True, null=True)
    butype = models.CharField(max_length=50, blank=True, null=True)
    bumobileno = models.CharField(max_length=20, blank=True, null=True)
    buemail = models.CharField(max_length=100, blank=True, null=True)
    bankmstid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geographyraw'


class Inquiry(models.Model):
    credt_rpt_id = models.TextField(db_column='CREDT-RPT-ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    los_app_id = models.CharField(db_column='LOS-APP-ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    branch_id = models.FloatField(db_column='BRANCH-ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    customer_id_mbr_id = models.FloatField(db_column='CUSTOMER ID/MBR ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    applicant_name = models.TextField(db_column='APPLICANT-NAME', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aka = models.FloatField(db_column='AKA', blank=True, null=True)  # Field name made lowercase.
    dob = models.TextField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    pan = models.TextField(db_column='PAN', blank=True, null=True)  # Field name made lowercase.
    passport = models.FloatField(db_column='PASSPORT', blank=True, null=True)  # Field name made lowercase.
    dl = models.FloatField(db_column='DL', blank=True, null=True)  # Field name made lowercase.
    rc = models.TextField(db_column='RC', blank=True, null=True)  # Field name made lowercase.
    uid = models.TextField(db_column='UID', blank=True, null=True)  # Field name made lowercase.
    voters = models.TextField(db_column='VOTERS', blank=True, null=True)  # Field name made lowercase.
    other_id = models.FloatField(db_column='OTHER-ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father = models.FloatField(db_column='FATHER', blank=True, null=True)  # Field name made lowercase.
    spouse = models.TextField(db_column='SPOUSE', blank=True, null=True)  # Field name made lowercase.
    mother = models.FloatField(db_column='MOTHER', blank=True, null=True)  # Field name made lowercase.
    other = models.FloatField(db_column='OTHER', blank=True, null=True)  # Field name made lowercase.
    phone_1 = models.BigIntegerField(db_column='PHONE 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phone_2 = models.FloatField(db_column='PHONE 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phone_3 = models.FloatField(db_column='PHONE 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email_1 = models.FloatField(db_column='EMAIL 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email_2 = models.FloatField(db_column='EMAIL 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gender = models.FloatField(db_column='GENDER', blank=True, null=True)  # Field name made lowercase.
    address_1 = models.TextField(db_column='ADDRESS-1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    state_1 = models.TextField(db_column='STATE-1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    address_2 = models.TextField(db_column='ADDRESS-2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    state_2 = models.TextField(db_column='STATE-2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    address_3 = models.FloatField(db_column='ADDRESS-3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    state_3 = models.FloatField(db_column='STATE-3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    retro_pr_dt = models.FloatField(db_column='RETRO-PR-DT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unnamed_31 = models.FloatField(db_column='Unnamed: 31', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'inquiry'


class Ioi(models.Model):
    credit_report_id = models.TextField(blank=True, null=True)
    los_app_id = models.CharField(blank=True, null=True)
    customer_id = models.FloatField(blank=True, null=True)
    credit_grantor = models.TextField(blank=True, null=True)
    inquiry_date = models.TextField(db_column='INQUIRY-DATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ownership_type = models.TextField(db_column='OWNERSHIP-TYPE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    purpose = models.TextField(db_column='PURPOSE', blank=True, null=True)  # Field name made lowercase.
    amount = models.TextField(db_column='AMOUNT', blank=True, null=True)  # Field name made lowercase.
    remarks = models.FloatField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    unnamed_9 = models.FloatField(db_column='Unnamed: 9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'ioi'


class LoanIds(models.Model):
    array_agg = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'loan_ids'


class Noncontactable(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    branchmstid = models.IntegerField(db_column='BranchMstID', blank=True, null=True)  # Field name made lowercase.
    loanmstid = models.IntegerField(db_column='LoanMstID', blank=True, null=True)  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    loantype = models.CharField(db_column='LoanType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customercode = models.CharField(db_column='CustomerCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    isnoncontactable = models.BooleanField(db_column='IsNonContactable', blank=True, null=True)  # Field name made lowercase.
    daysinnoncontactable = models.IntegerField(db_column='DaysInNonContactable', blank=True, null=True)  # Field name made lowercase.
    lastattemptedcontactdate = models.DateField(db_column='LastAttemptedContactDate', blank=True, null=True)  # Field name made lowercase.
    noncontactablereason = models.TextField(db_column='NonContactableReason', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'noncontactable'


class NotCollectedData(models.Model):
    demand_date = models.CharField(db_column='Demand Date', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mobile_number = models.CharField(db_column='Mobile Number', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    member = models.CharField(db_column='Member', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contact_no = models.CharField(db_column='Contact No', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    loan_scheme = models.CharField(db_column='Loan Scheme', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    loan_status = models.CharField(db_column='Loan Status', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    loan_date = models.CharField(db_column='Loan Date', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    loan_amount = models.IntegerField(db_column='Loan Amount', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    collection_date = models.CharField(db_column='Collection Date', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_receive_date = models.CharField(db_column='Last Receive Date', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_receive_amt = models.IntegerField(db_column='Last Receive Amt', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    savings_demand_amount = models.IntegerField(db_column='Savings Demand Amount', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_all_demand = models.IntegerField(db_column='Total All Demand', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    loan_no = models.CharField(db_column='Loan No', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emi_amount = models.IntegerField(db_column='EMI Amount', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pos = models.IntegerField(blank=True, null=True)
    collection = models.CharField(max_length=100, blank=True, null=True)
    inserted_date = models.DateField(blank=True, null=True)
    day_type = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'not_collected_data'


class Odsheet(models.Model):
    customerid = models.CharField(max_length=50, blank=True, null=True, db_comment='Customer ID with preserved leading zeros')
    disbursementid = models.CharField(max_length=50, blank=True, null=True, db_comment='Loan disbursement ID')
    customername = models.CharField(max_length=255, blank=True, null=True)
    mobileno = models.CharField(max_length=20, blank=True, null=True)
    lastpaymentdate = models.DateField(blank=True, null=True)
    lastcollectedamount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    emiamount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    overdueamount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, db_comment='Amount overdue for the loan')
    totaloutstanding = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    loantype = models.CharField(max_length=255, blank=True, null=True)
    disbursementdate = models.DateField(blank=True, null=True)
    disbursementamount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    branchname = models.CharField(max_length=255, blank=True, null=True)
    rateofinterest = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nextemidate = models.DateField(blank=True, null=True, db_comment='Next EMI due date')
    branchcode = models.CharField(max_length=20, blank=True, null=True)
    inststartdate = models.DateField(blank=True, null=True)
    bankmstid = models.IntegerField(blank=True, null=True)
    inserted_date = models.DateField(blank=True, null=True)
    fromfile = models.CharField(max_length=50, blank=True, null=True, db_comment='Source file identifier (csv_additional, overdue_excel, etc.)')
    first_time_arrear_clients = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'odsheet'
        db_table_comment = 'Overdue sheet data containing loan and customer information'
# Unable to inspect table 'public."DisbursementFile"_temp'
# The error was: syntax error at or near ""_temp""
LINE 1: SELECT * FROM "public."DisbursementFile"_temp" LIMIT 1
                                               ^


class Rawfile(models.Model):
    customerid = models.CharField(max_length=255, blank=True, null=True)
    disbursementid = models.CharField(max_length=255)
    loantype = models.CharField(max_length=100, blank=True, null=True)
    customername = models.CharField(max_length=255, blank=True, null=True)
    disbursementamount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    rateofinterest = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    repaymenttenure = models.IntegerField(blank=True, null=True)
    emiamount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    paymentfrequency = models.CharField(max_length=50, blank=True, null=True)
    numberofdayspastdue = models.IntegerField(blank=True, null=True)
    mobileno = models.CharField(max_length=20, blank=True, null=True)
    inststartdate = models.DateField(blank=True, null=True)
    collectionofficerid = models.CharField(max_length=255, blank=True, null=True)
    collectionofficername = models.CharField(max_length=255, blank=True, null=True)
    branchname = models.CharField(max_length=255, blank=True, null=True)
    branchcode = models.CharField(max_length=50, blank=True, null=True)
    applicanttype = models.CharField(max_length=50, blank=True, null=True)
    overdueamount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    totaloutstanding = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    principlecollected = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    interestcollected = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    collectedamount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    collectiondate = models.DateField(blank=True, null=True)
    pos = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bankmstid = models.IntegerField(blank=True, null=True)
    inserted_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    dateofbirth = models.DateField(blank=True, null=True)
    disbursementdate = models.DateField(blank=True, null=True)
    loanclassification = models.CharField(max_length=100, blank=True, null=True)
    lastpaymentdate = models.DateField(blank=True, null=True)
    lastcollectedamount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    currentbalance = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    interestoutstanding = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    totalpending = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    principlepending = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    interestpending = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    closingdate = models.DateField(blank=True, null=True)
    previousemidate = models.DateField(blank=True, null=True)
    guarantor = models.CharField(blank=True, null=True)
    guarantor_mobile = models.CharField(blank=True, null=True)
    extracolumn1 = models.CharField(blank=True, null=True)
    extracolumn2 = models.CharField(blank=True, null=True)
    extracolumn3 = models.CharField(blank=True, null=True)
    extracolumn4 = models.CharField(blank=True, null=True)
    extracolumn5 = models.CharField(blank=True, null=True)
    nextemidate = models.DateField(blank=True, null=True)
    first_time_arrear_clients = models.BooleanField(blank=True, null=True)
    language = models.CharField(blank=True, null=True)
    scheduledate = models.DateField(blank=True, null=True)
    originaldisbursementid = models.CharField(blank=True, null=True)
    guarantorid = models.CharField(blank=True, null=True)
    pending_emis = models.CharField(blank=True, null=True)
    centername = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rawfile'


class ResultJson(models.Model):
    json_object_agg = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'result_json'


class Summary(models.Model):
    credit_report_id = models.TextField(blank=True, null=True)
    los_app_id = models.CharField(blank=True, null=True)
    customer_id = models.FloatField(blank=True, null=True)
    account_status = models.TextField(blank=True, null=True)
    error = models.FloatField(blank=True, null=True)
    perform_cns_score = models.BigIntegerField(blank=True, null=True)
    perform_cns_score_description = models.FloatField(blank=True, null=True)
    pri_no_of_accts = models.BigIntegerField(blank=True, null=True)
    pri_active_accts = models.BigIntegerField(blank=True, null=True)
    pri_overdue_accts = models.BigIntegerField(blank=True, null=True)
    pri_current_balance = models.BigIntegerField(blank=True, null=True)
    pri_sanctioned_amount = models.BigIntegerField(blank=True, null=True)
    pri_disbursed_amount = models.BigIntegerField(blank=True, null=True)
    sec_no_of_accts = models.BigIntegerField(blank=True, null=True)
    sec_active_accts = models.BigIntegerField(blank=True, null=True)
    sec_overdue_accts = models.BigIntegerField(blank=True, null=True)
    sec_current_balance = models.BigIntegerField(blank=True, null=True)
    sec_sanctioned_amount = models.BigIntegerField(blank=True, null=True)
    sec_disbursed_amount = models.BigIntegerField(blank=True, null=True)
    primary_instal_amt = models.BigIntegerField(blank=True, null=True)
    sec_instal_amt = models.BigIntegerField(blank=True, null=True)
    new_accts_in_last_six_months = models.BigIntegerField(blank=True, null=True)
    delinquent_accts_in_last_six_months = models.BigIntegerField(blank=True, null=True)
    average_acct_age = models.TextField(blank=True, null=True)
    credit_history_length = models.TextField(blank=True, null=True)
    no_of_inquiries = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'summary'


class SummaryTable(models.Model):
    customerid = models.CharField(blank=True, null=True)
    disbursementid = models.CharField(blank=True, null=True)
    action = models.CharField(db_column='Action', max_length=50, blank=True, null=True)  # Field name made lowercase.
    currentoverdueamt = models.FloatField(blank=True, null=True)
    newoverdueamt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'summary_table'


class TempNull(models.Model):
    loanmstid = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_null'


class TempNullUniqueid(models.Model):
    loanmstid = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_null_uniqueid'


class UseRawClassification(models.Model):
    exists = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'use_raw_classification'


class UseRawDpd(models.Model):
    exists = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'use_raw_dpd'


class UseRawLastpayment(models.Model):
    exists = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'use_raw_lastpayment'


class UseRawOutstanding(models.Model):
    exists = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'use_raw_outstanding'


class UseRawOverdue(models.Model):
    exists = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'use_raw_overdue'


class VTemplate(models.Model):
    jsonb_build_object = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_template'


class WhBotViewWhatsappMessages(models.Model):
    id = models.BigAutoField()
    queue_id = models.BigIntegerField(blank=True, null=True)
    assigned_to = models.IntegerField(blank=True, null=True)
    message_datetime = models.DateTimeField(blank=True, null=True)
    sender = models.CharField(max_length=50, blank=True, null=True)
    message_content = models.CharField(max_length=1500, blank=True, null=True)
    button = models.BooleanField(blank=True, null=True)
    template_id = models.IntegerField(blank=True, null=True)
    message_id = models.CharField(max_length=1000, blank=True, null=True)
    message_status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wh_bot_view_whatsapp_messages'


class WhBotViewWhatsappqueue(models.Model):
    id = models.BigAutoField()
    bank_id = models.IntegerField(blank=True, null=True)
    receiver_id = models.CharField(max_length=200, blank=True, null=True)
    flow_name = models.CharField(max_length=200, blank=True, null=True)
    flow_id = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField()
    created_on = models.DateTimeField()
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    last_sent_message_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField()
    stage = models.CharField(max_length=50, blank=True, null=True)
    counter = models.IntegerField()
    field_1 = models.CharField(max_length=50, blank=True, null=True)
    field_2 = models.CharField(max_length=50, blank=True, null=True)
    field_3 = models.CharField(max_length=50, blank=True, null=True)
    field_4 = models.CharField(max_length=50, blank=True, null=True)
    field_5 = models.CharField(max_length=50, blank=True, null=True)
    field_6 = models.CharField(max_length=50, blank=True, null=True)
    field_7 = models.CharField(max_length=50, blank=True, null=True)
    field_8 = models.CharField(max_length=50, blank=True, null=True)
    field_9 = models.CharField(max_length=50, blank=True, null=True)
    exceptions_occured = models.CharField(max_length=500, blank=True, null=True)
    assigned_to = models.IntegerField(blank=True, null=True)
    assigned_on = models.DateField(blank=True, null=True)
    reallocated = models.BooleanField()
    rellocated_on = models.DateField(blank=True, null=True)
    autocomplete = models.BooleanField()
    wrong_number = models.BooleanField(blank=True, null=True)
    promise = models.BooleanField(blank=True, null=True)
    conversation = models.CharField(max_length=10000, blank=True, null=True)
    is_allocate = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'wh_bot_view_whatsappqueue'


class WhereConditions(models.Model):
    string_agg = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'where_conditions'
