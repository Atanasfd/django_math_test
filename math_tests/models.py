from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

   
class Test_1_math(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    firstQuestion = models.CharField(verbose_name='A triangle has 2 angles each equal to 60 degrees. What type of triangle is it?',max_length=120)
    secondQuestion = models.FloatField(verbose_name='The triangle ABC has  angles A=90 degrees, B=30. If side AC is 5 cm, how many cms is BC?')
    thirdQuestion = models.FloatField(verbose_name='47/5=')
    fourthQuestion = models.FloatField(verbose_name='13-2.3=')
            


class Test_1_Form(ModelForm):
    class Meta:
        model = Test_1_math
        fields =['firstQuestion','secondQuestion','thirdQuestion','fourthQuestion']

