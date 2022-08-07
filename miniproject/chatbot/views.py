from django.shortcuts import render
from django.http import HttpResponse
from chatbot import functions as cb_fnc
#   Create your views here.
def chatbotui(request):
    return render(request, 'chatbotui.html')

def giveResponse(request):
    usermessage = request.POST.get('text')
    reply = cb_fnc.botReply(usermessage)
    return HttpResponse(reply)