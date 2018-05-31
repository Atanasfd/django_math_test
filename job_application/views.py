from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from job_application.models import Job_1_Form,Job_1


# Create your views here.


@login_required
def job_application_1_view(request):
    if request.method == "POST":
        instance = Job_1.objects.filter(
            user=request.user).first()
        form = Job_1_Form(request.POST,instance=instance)
        if form.is_valid():
            instance=form.save(commit = False)
            instance.user = request.user.username
            instance.save()
            return HttpResponseRedirect("/done/")
    else:
        form=Job_1_Form()

    return render(request,'job_application_1.html',{'form':form})

def done(request):
    return render(request,'done.html')

