from django.db import models

class Patient_details(models.Model):
    patient_name = models.CharField(max_length=50)
    patient_age = models.IntegerField()
    disease = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=10)
    ward_no = models.IntegerField()
    amount_paid = models.IntegerField()
    discharge = models.BooleanField(default=False)
