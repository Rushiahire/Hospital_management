from django.shortcuts import render,redirect 
from django.views import View
from patient.forms import Patient_form
from patient.models import Patient_details
from . import forms


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
        print(user_name,password)
        return redirect('/')

class Logout(View):
    def get(self,request):
        return redirect('/')
        


    
        
        
