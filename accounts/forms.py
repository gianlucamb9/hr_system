from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63,widget=forms.TextInput(attrs={"class":"form-control","name":"username","placeholder":"Enter Username"}))
    password = forms.CharField(max_length=63,widget=forms.PasswordInput(attrs={"class":"form-control","password":"password","placeholder":"Enter Password"}))

class PassResetForm(forms.Form):
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={"class":"form-control","email":"email","placeholder":"Enter Email"}))