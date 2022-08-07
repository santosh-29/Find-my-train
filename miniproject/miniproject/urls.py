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
from django.urls import path,include
from findmytrain import views as fmt_views
from questionsapp import views as qa_views
from chatbot import views as cb_views
# from chatbot import functions as cb_functions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fmt_views.index, name='index'),
    path('findstation/', fmt_views.findstation, name='findstation'),
    path('findstationresult/', fmt_views.findstationresult, name='findstationresult'),
    path('findtrainbyname/', fmt_views.findtrainbyname, name='findtrainbyname'),
    path('findtrainbynum/', fmt_views.findtrainbynum, name='findtrainbynum'),
    path('findtrainresult/', fmt_views.findtrainresult, name='findtrainresult'),
    path('findtrainsrcdest/', fmt_views.findtrainsrcdest, name='findtrainsrcdest'),
    path('findtrainsrcdestresult/', fmt_views.findtrainsrcdestresult, name='findtrainsrcdestresult'),
    path('pnrstatus/', fmt_views.pnrstatus, name='pnrstatus'),
    path('pnrstatusresult/', fmt_views.pnrstatusresult, name='pnrstatusresult'),
    path('livestation/', fmt_views.livestation, name='livestation'),
    path('livestationresult/', fmt_views.livestationresult, name='livestationresult'),
    path('nearestrailwaystations',fmt_views.nearestrailwaystations,name='nearestrailwaystations'),
    path('findtrainfares',fmt_views.findtrainfares,name='findtrainfares'),
    path('findtrainfaresresult/',fmt_views.findtrainfaresresult,name='findtrainfaresresult'),


    # path('', include('questionsapp.urls')),

    path('accounts/', include('django.contrib.auth.urls')),

    path('home',qa_views.home,name='home'),
    path('detail/<int:id>',qa_views.detail,name='detail'),
    path('save-comment',qa_views.save_comment,name='save-comment'),
    path('save-upvote',qa_views.save_upvote,name='save-upvote'),
    path('save-downvote',qa_views.save_downvote,name='save-downvote'),
    # User Register
    path('accounts/register/',qa_views.register,name='register'),
    # Profile
    path('accounts/profile/',qa_views.profile,name='profile'),
    # Ask Question
    path('ask-question',qa_views.ask_form,name='ask-question'),
    # Tag Page
    path('tag/<str:tag>',qa_views.tag,name='tag'),
    # Tags Page
    path('tags',qa_views.tags,name='tags'),


    path('chatbotui',cb_views.chatbotui,name='chatbotui'),
    path('send', cb_views.giveResponse,name='send'),
]
