
from django.db import reset_queries
from django.shortcuts import redirect, render
from django.views import View
from . import forms
from .import models


class New_patient(View):
    def get(self,request):
        content = {
            'patient_form':forms.Patient_form()
        }
        return render(request,'patient.html',content)

    def post(self,request):
        patient_name = request.POST['patient_name']
        patient_age = request.POST['patient_age']
        disease = request.POST['disease']
        ward_no= request.POST['ward_no']
        contact_no = request.POST['contact_no']
        amount_paid = request.POST['amount_paid']
        print("tata bye")
        new_data = models.Patient_details(patient_name=patient_name,
        patient_age=patient_age,
        disease=disease,
        ward_no=ward_no,
        contact_no=contact_no,
        amount_paid=amount_paid)
        new_data.save()
        return redirect('/')

class Details(View):
    def get(self,request): 
        patient_id = request.GET['patient_id']
        print(patient_id)
        content = {
            'patient_details': models.Patient_details.objects.get(id = patient_id)
        }
        return render(request,'details.html',content)

class Update_info(View):
    def get(self,request):
        patient_id = request.GET['patient_id']
        content={
            'update_form':forms.Update_form(),
            'update_model':models.Patient_details.objects.get(id=patient_id)
        }
        return render(request,'update_info.html',content)
    
    def post(self,request):
        patient_id = request.POST['patient_id']
        disease = request.POST['disease']
        ward_no = request.POST['ward_no']
        amount_paid = request.POST['amount_paid']
        patient_discharge = request.POST.get('patient_discharge',False)
        updated_data= models.Patient_details.objects.get(id=patient_id)
        updated_data.disease=updated_data.disease if disease== "" else disease
        updated_data.ward_no=updated_data.ward_no if ward_no== "" else ward_no
        updated_data.amount_paid=updated_data.amount if amount_paid== "" else updated_data.amount_paid + eval(amount_paid)
        updated_data.discharge = patient_discharge
        updated_data.save()
        return redirect('/')

class Book_appointment(View):
    def get(self,request):
        content = {
            'appointment_form':forms.Appointment_form()
        }        
        return render(request,'book_appointment.html',content)

    def post(self,request):
        patient_name = request.POST['patient_name']
        patient_age = request.POST['patient_age']
        disease = request.POST['disease']
        contact_no = request.POST['contact_no']
        appointment_date = request.POST['appointment_date']

        new_appointment = models.Appointment(
            patient_name=patient_name,
            patient_age=patient_age,
            disease=disease,
            contact_no=contact_no,
            appointment_date=appointment_date
        )

        new_appointment.save()
        return redirect('/')