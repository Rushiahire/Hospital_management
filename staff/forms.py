from django import forms

class Login_forms(forms.Form):
    user_name = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())