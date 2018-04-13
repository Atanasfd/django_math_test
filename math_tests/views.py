from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from math_tests.forms import Test_1_Form

# Create your views here.


@login_required
def Test_1(request):
    if request.method == "GET":
        form = Test_1_Form(request.GET or None)
        if form.is_valid():
            firstQuestion=form.cleaned_data['firstQuestion']
            return HttpResponseRedirect("/thank_you/")


    return render(request,'math_test_1.html',{'form':form})

def thank_you(request):
    return render(request,'thank_you.html')

