from django.shortcuts import render,redirect 
from django.views import View
from patient.forms import Patient_form
from patient.models import Patient_details,Appointment
from . import forms
from django.contrib.auth.models import auth


class Home(View):
    def get(self,request):
        content = {
            'patient_form':Patient_form(),
            'patient_details':Patient_details.objects.all()
        }
        return render(request,'index.html',content)

class Login(View):
    def get(self,request):
        content={
            'login_form':forms.Login_forms
        }
        return render(request,'login.html',content)
        

    def post(self,request):
        user_name= request.POST['user_name']
        password = request.POST['password']
        user=auth.authenticate(username = user_name,password=password)
        if user is not None:
            auth.login(request,user)
        return redirect('/')

class Booked_appointment(View):
    def get(self,request):
        if request.user.is_authenticated:
            content = {
                'updated_appoint':Appointment.objects.all()
            }
            return render(request,'display_booking.html',content)
        
        else:
            page = '404page.html'
            return render(request,page)



class Logout(View):
    def get(self,request):
        auth.logout(request)
        return redirect('/')
        


    
        
        
