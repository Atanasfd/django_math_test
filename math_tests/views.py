from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from math_tests.models import Test_1_Form,Test_1_math


@login_required
def Test_1_view(request):
    if request.method == "POST":
        instance = Test_1_math.objects.filter(
            user=request.user).first()
        form = Test_1_Form(request.POST,instance=instance)
        if form.is_valid():
            instance=form.save(commit = False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect("/thank_you/")

    else:
        form=Test_1_Form()
    return render(request,'math_test_1.html',{'form':form})

def thank_you(request):
    return render(request,'thank_you.html')

