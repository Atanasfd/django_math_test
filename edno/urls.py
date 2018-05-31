"""edno URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.urls import re_path,include
from django.conf import settings


from profiles import views as profiles_views
from math_tests import views as math_tests_views
from job_application import views as job_application_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$',profiles_views.home,name='home'),
    re_path('correct/',profiles_views.correct,name='correct'),
    re_path(r'wrong/',profiles_views.wrong,name='wrong'),
    re_path('test_1/',math_tests_views.Test_1_view,name='test_1' ),
    re_path('thank_you/',math_tests_views.thank_you,name='thank_you' ),
    re_path('accounts/', include('allauth.urls')),
    re_path('job_application_1/',job_application_views.job_application_1_view,name='job_application_1'),
    re_path('done/',job_application_views.done,name='done'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   
