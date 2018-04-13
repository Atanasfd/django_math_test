from django import forms


class HomePageForm(forms.Form):
    firstQuestion = forms.DecimalField(label='5+6=')
    secondQuestion = forms.DecimalField(label='5*6=')
    thirdQuestion = forms.DecimalField(label='12/3=')
    fourthQuestion = forms.DecimalField(label='8-3=')
    
    
