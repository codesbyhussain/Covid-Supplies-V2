from django import forms
from .models import Donor
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
import datetime

YorN=[
('yes','Yes'),
('no','No'),
]

class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = ['name', 'date_of_birth', 'phone', 'address', 'email', 'blood_group', 'gender', 'image','password']

class Eligible(forms.Form):
    donated = forms.CharField(label = 'Have you donated in the last 3 months? ', widget=forms.Select(choices=YorN))
    age = forms.CharField(label = 'Are you above the age of 18? ', widget=forms.Select(choices=YorN))
    disease = forms.CharField(label = mark_safe(' Do you engage or suffer from any of these :<li>Cancer</li><li>Cardiac disease</li><li>Sever lung disease</li><li>Hepatitis B and C</li><li>Infection, AIDS or Sexually Transmitted Diseases (STD)</li><li>High risk occupation (e.g. prostitution)</li><li>Unexplained weight loss of more than 5 kg over 6 months</li><li>Chronic alcoholism</li><li>Other conditions or disease stated in the Guide to Medical Assessment of Blood Donors.</li> '), widget=forms.Select(choices=YorN))

class appointment(forms.Form):
    setdate=forms.DateField(widget = forms.SelectDateWidget)

class loginform(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
