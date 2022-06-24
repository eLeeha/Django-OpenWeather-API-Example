from django import forms

class WetterForm(forms.Form):
    city_input = forms.CharField(label='city_input', max_length=100)
