from django.db.models.base import Model
from .models import Input,Region
from django.forms import ModelForm,HiddenInput,ModelChoiceField,Select
from .widget import DateTimePickerInput
from django import forms

class DetailsForm(ModelForm):
  class Meta:
    model=Input
    fields=['time','address','region','day']
    widgets={"time": DateTimePickerInput(format="%m/%d/%y %H:%M:%S"),
    "day": HiddenInput(),}
  region=ModelChoiceField(queryset=Region.objects.all(),to_field_name='name',required=True,widget=Select,)

class PastForm(forms.Form):
  CHOICE1=[('', '--Select a Day--'),('Sunday','Sunday'),('Monday','Monday'),('Tuesday','Tuesday'),('Wednesday','Wednesday'),('Thursday','Thursday'),('Friday','Friday'),('Saturday','Saturday'),]
  
  CHOICE2= [('', '--Select a Region--'),('A','A'),('B','B'),('C','C'),('D','D'),('E','E'),('F','F'),('G','G'),]
  region=forms.ChoiceField(choices=CHOICE2)
  day=forms.ChoiceField(choices=CHOICE1)
  
  
  

  
    
    