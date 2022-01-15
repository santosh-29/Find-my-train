from django.shortcuts import render
import requests
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')


def findstation(request):
    return render(request, 'findstation.html')


def findstationresult(request):
    searchValue = request.POST.get("stationName")
    print(searchValue)
    url = "https://indianrailways.p.rapidapi.com/findstations.php"
    querystring = {"station": searchValue}
    headers = {
        'x-rapidapi-host': "indianrailways.p.rapidapi.com",
        'x-rapidapi-key': "6ec2fdd9c9msh434f364619314f9p142174jsn42ea28ccc186"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    # StationRes = response.json()
    # print(StationRes)
    # res = StationRes["stations"]
    res = response.json()
    return render(request, 'findstationresult.html',{'res' : res})


def findtrainbyname(request):
    return render(request, 'findtrainbyname.html')


def findtrainbynum(request):
    return render(request, 'findtrainbynum.html')


def findtrainresult(request):
    searchValue = request.POST.get("trainName")
    url = "https://trains.p.rapidapi.com/"
    payload = "{\r\"search\": \"" + searchValue + "\"\r}"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "trains.p.rapidapi.com",
        'x-rapidapi-key': "6ec2fdd9c9msh434f364619314f9p142174jsn42ea28ccc186"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    res = response.json()
    # print(response.text)
    return render(request, 'findtrainresult.html',{'res' : res})


def pnrstatus(request):
    return render(request, 'pnrstatus.html')


def pnrstatusresult(request):
    searchValue = request.POST.get("PNRStatus")
    url = "https://indianrailways.p.rapidapi.com/index.php"
    querystring = {"pnr": searchValue}
    headers = {
        'x-rapidapi-host': "indianrailways.p.rapidapi.com",
        'x-rapidapi-key': "6ec2fdd9c9msh434f364619314f9p142174jsn42ea28ccc186"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    res = response.json()
    print(res)
    return render(request, 'pnrstatusresult.html', {'res' : res})


def livestation(request):
    return render(request, 'livestation.html')


def livestationresult(request):
    trID = request.POST.get("trainID")
    trDt = request.POST.get("trainDate")
    url = "https://indian-railway-live-train.p.rapidapi.com/live-train"
    payload = "trainID="+trID+"&date="+trDt
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-host': "indian-railway-live-train.p.rapidapi.com",
        'x-rapidapi-key': "6ec2fdd9c9msh434f364619314f9p142174jsn42ea28ccc186"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    res = response.json()
    print(res)
    return render(request, 'livestationresult.html', {'res' : res})