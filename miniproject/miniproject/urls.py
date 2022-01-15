"""miniproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from findmytrain import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('findstation', views.findstation, name='findstation'),
    path('findstationresult', views.findstationresult, name='findstationresult'),
    path('findtrainbyname', views.findtrainbyname, name='findtrainbyname'),
    path('findtrainbynum', views.findtrainbynum, name='findtrainbynum'),
    path('findtrainresult', views.findtrainresult, name='findtrainresult'),
    path('pnrstatus', views.pnrstatus, name='pnrstatus'),
    path('pnrstatusresult', views.pnrstatusresult, name='pnrstatusresult'),
    path('livestation', views.livestation, name='livestation'),
    path('livestationresult', views.livestationresult, name='livestationresult'),
]
