from django import forms

from website.settings import DATE_INPUT_FORMATS
from website.settings import TIME_INPUT_FORMATS

    
class InputDataForm_backup(forms.Form):
    lat_input = forms.FloatField(label="latitude", max_value=90, min_value=-90, widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":""}))
    long_input = forms.FloatField(label="logitude", max_value=180, min_value=-180, widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":""}))
    date_input = forms.DateField(input_formats= DATE_INPUT_FORMATS, widget=forms.DateInput(attrs={"class":"form-control", "placeholder":"Date Format : DD-MM-YY"}))
    start_time_input = forms.TimeField(input_formats= TIME_INPUT_FORMATS, widget=forms.DateTimeInput(attrs={"class":"form-control", "placeholder":"Time Format : HH:MM"}))
    altitude_input = forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":""}))
    runtime_input = forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":""}))

class InputDataForm(forms.Form):
    latlong_input = forms.CharField(label="latitude logitude",  widget=forms.Textarea(attrs={"class":"form-control", "placeholder":""}))
    date_input = forms.DateField(input_formats= DATE_INPUT_FORMATS, widget=forms.DateInput(attrs={"class":"form-control", "placeholder":"Date Format : DD-MM-YY"}))
    start_time_input = forms.TimeField(input_formats= TIME_INPUT_FORMATS, widget=forms.DateTimeInput(attrs={"class":"form-control", "placeholder":"Time Format : HH:MM"}))
    altitude_input = forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":""}))
    runtime_input = forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":""}))
      
class UploadDataForm(forms.Form):
    file = forms.FileField()
    altitude_input = forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":""}))
    runtime_input = forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":""}))
    
class UploadDataForm_additional(forms.Form):
    altitude_input = forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":""}))
    runtime_input = forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":""}))
    
    