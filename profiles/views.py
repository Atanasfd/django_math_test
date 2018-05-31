from django.shortcuts import render
from django.http import HttpResponseRedirect
from profiles.forms import HomePageForm
from django.urls import reverse

## DAVAI SUS SESII
##https://docs.djangoproject.com/en/1.11/topics/http/sessions/#module-django.contrib.sessions

questions=['firstQuestion','secondQuestion','thirdQuestion','fourthQuestion']

def home(request):
    if request.method == "GET":
        form = HomePageForm(request.GET or None)
        
        if form.is_valid():
            request.session['firstQuestion']=form.cleaned_data['firstQuestion']
            request.session['secondQuestion']=form.cleaned_data['secondQuestion']
            request.session['thirdQuestion']=form.cleaned_data['thirdQuestion']
            request.session['fourthQuestion']=form.cleaned_data['fourthQuestion']
            if form.cleaned_data['firstQuestion']==11 and form.cleaned_data['secondQuestion']==30:
                if form.cleaned_data['thirdQuestion']==4 and form.cleaned_data['fourthQuestion']==5:
                    return HttpResponseRedirect("/correct/")
                else:
                    return HttpResponseRedirect('wrong/')

            else:
                return HttpResponseRedirect('wrong/')
                #return HttpResponseRedirect(reverse('wrong.html'))
    else:
        form = HomePageForm()
    return render(request,'home.html',{'form':form})



def correct(request):
    return render(request,'correct.html')
def wrong(request):
     return render(request,'wrong.html')
def sign_up(request):
    return render(request,'sign_up.html')

        
