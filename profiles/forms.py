from django import forms


class HomePageForm(forms.Form):
    firstQuestion = forms.FloatField(label='5+6=')
    secondQuestion = forms.FloatField(label='5*6=')
    thirdQuestion = forms.FloatField(label='12/3=')
    fourthQuestion = forms.FloatField(label='8-3=')
    
    
