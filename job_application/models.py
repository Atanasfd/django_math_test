from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


# Create your models here.

class Job_1(models.Model):
    user = models.CharField(max_length=80,default='')
    firstQuestion = models.CharField(verbose_name='Tell us about yourself.',max_length=800)
    secondQuestion = models.FloatField(verbose_name='How much experience do you have in a similar position?',max_length=2)
    thirdQuestion = models.FloatField(verbose_name='What are your salary expectations?',max_length=5)
    fourthQuestion = models.CharField(verbose_name='What are your strengths and weaknesses?',max_length=600)
    fifthQuestion = models.CharField(verbose_name='When can you start?',max_length=100)

class Job_1_Form(ModelForm):
    class Meta:
        model = Job_1
        fields =['firstQuestion','secondQuestion','thirdQuestion','fourthQuestion','fifthQuestion']


