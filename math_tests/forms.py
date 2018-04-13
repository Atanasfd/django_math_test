from django import forms


class Test_1_Form(forms.Form):
    firstQuestion = forms.CharField(label='A triangle has 2 angles each equal to 60 degrees. What type of triangle is it?')
    secondQuestion = forms.DecimalField(label='The triangle ABC has  angles A=90 degrees, B=30. If side AC is 5 cm, how many cms is BC?')
    thirdQuestion = forms.DecimalField(label='47/5=')
    fourthQuestion = forms.DecimalField(label='13-2.3=')
    
    
