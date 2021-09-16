from django import forms

class Patient_form(forms.Form):
    patient_name = forms.CharField(max_length=50)
    patient_age = forms.IntegerField()
    disease = forms.CharField(max_length=50)
    ward_no = forms.IntegerField()
    contact_no = forms.CharField(max_length=12)
    amount_paid = forms.IntegerField()


class Update_form(Patient_form):
    patient_name = forms.CharField(required=False)
    patient_age = forms.IntegerField(required=False)
    disease = forms.CharField(required=False)
    ward_no = forms.IntegerField(required=False)
    contact_no = forms.CharField(required=False)
    amount_paid = forms.IntegerField(required=False)
    