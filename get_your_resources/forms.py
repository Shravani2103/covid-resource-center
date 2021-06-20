from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.models import ModelFormMetaclass

class OrderResource(ModelForm):
    class Meta:
        model = Resource
        fields = ['Res_name','Res_id']

class OrderHospital(ModelForm):
    class Meta:
        model = Hospital_resource
        fields = ['H_id','Res_name','Res_quantity','Availability']

class OrderPharmacy(ModelForm):
    class Meta:
        model = Pharm_res
        fields = '__all__'    
  

class Ordervacc(ModelForm):
    class Meta:
        model = Vac_res
        fields = '__all__'    

class OrderStock(ModelForm):
    class Meta:
        model = Stockist_resource
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields=['username','email','password1','password2']