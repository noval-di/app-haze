from django import forms
from datetime import datetime

from website.settings import DATE_INPUT_FORMATS
from website.settings import TIME_INPUT_FORMATS

    

class InputDataForm(forms.Form):
    latlong_input = forms.CharField(label="Latitude Logitude",  widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"(latitude, longitude)","rows":5}))
    date_input = forms.DateField( widget=forms.DateInput(attrs={'type':'date',"class":"form-control", "placeholder":"", "max":datetime.now().date()}))
    start_time_input = forms.TimeField(input_formats= TIME_INPUT_FORMATS, widget=forms.DateTimeInput(attrs={"type":"time","class":"form-control", "placeholder":"Time Format : HH:MM"}))
    altitude_input = forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":""}))
    runtime_input = forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":""}))
      
class UploadDataForm(forms.Form):
    file = forms.FileField()
    altitude_input = forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":""}))
    runtime_input = forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":""}))
    
class HazeInitialForm(forms.Form):
    # provinsi_input= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"", "type":"search","name":"provinsi_filtered"}))
    # kabkota_input= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"", "type":"search","name":"kab_kota_filtered"}))
    # kecamatan_input= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"", "type":"search","name":"kecamatan_filtered"}))
    # desa_input= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"", "type":"search","name":"desa_filtered"}))
    
    # date_input_min = forms.DateField(input_formats= DATE_INPUT_FORMATS, widget=forms.DateInput(attrs={"class":"form-control", "placeholder":"Date Format : DD-MM-YY", "type":"date", "name":"date_min"}))
    
    # date_input_max = forms.DateField(input_formats= DATE_INPUT_FORMATS, widget=forms.DateInput(attrs={"class":"form-control", "placeholder":"Date Format : DD-MM-YY", "type":"date", "name":"date_min"}))
    
    altitude_input = forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":""}))
    runtime_input = forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":""}))
    
    