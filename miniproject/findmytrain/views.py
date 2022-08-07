import time

from django.shortcuts import render
import requests
from django.http import HttpResponse
import winrt.windows.devices.geolocation as wdg, asyncio
from math import radians, cos, sin, asin, sqrt
import pandas as pd
import json
import subprocess
from findmytrain import functions as fnc
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


def findtrainsrcdest(request):
    return render(request, 'findtrainsrcdest.html')

def findtrainsrcdestresult(request):
    source = request.POST.get("sourcestation")
    destination = request.POST.get("destinationstation")
    result = subprocess.Popen(
        ['php', 'findmytrain//static//php-files//trainbetweensrcdestcall.php', source, destination],
        stdout=subprocess.PIPE, universal_newlines=False, stderr=subprocess.STDOUT)
    # print("result : ", result.stdout)
    # type(result.stdout)
    for line in result.stdout:
        res = line
        break
    data = str(res, 'UTF-8')
    json_object = json.loads(data)
    res=[]
    if (len(json_object['result']['found_trains']) > 0):
        for train in json_object['result']['found_trains'].values():
            res.append(train)
    return render(request, 'findtrainsrcdestresult.html',{'res': res})

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
    train_no = request.POST.get("trainID")
    date = request.POST.get("trainDate")
    result = subprocess.Popen(['php', 'findmytrain//static//php-files//livestationcall.php', train_no, date],
                              stdout=subprocess.PIPE, universal_newlines=False, stderr=subprocess.STDOUT)
    # print("result : ", result.stdout)
    type(result.stdout)
    for line in result.stdout:
        res = line
        break
    data = str(res, 'UTF-8')
    # data
    json_object = json.loads(data)
    result = json_object['result']
    # print(result)
    return render(request, 'livestationresult.html', {'res' : result})

def nearestrailwaystations(request):
    lat = request.POST.get("latitude")
    long = request.POST.get("longitude")
    # print(lat,long)
    # rad=10
    if(request.POST.get("radius") != None):
        rad = float(request.POST.get("radius"))
    # print(lat,long,rad)
    stations = pd.concat(map(pd.read_csv, ['./data/TestA.csv', './data/TestB.csv', './data/TestC.csv','./data/TestD.csv','./data/TestE.csv','./data/TestF.csv']), ignore_index=True)
    if(lat != None and long != None):
        stations["DISTANCE"] = stations.apply(lambda row: fnc.dist(lat, long, row["Latitude"], row["Longitude"]), axis=1)
        stations["DIRECTIONS"] = stations.apply (lambda row: fnc.directions(lat, long, row["Latitude"], row["Longitude"]), axis=1)
        # print(stations.head())
        # res = stations[stations['Distance'] <= rad]
        temp_res = stations[stations['DISTANCE'] <= rad]
        # res = json.dumps(json.loads(res.to_json()))
        # print(type(temp_res))
        # print(temp_res)
        json_records = temp_res.reset_index().to_json(orient='records')
        result = []
        result = json.loads(json_records)
        return render(request, 'nearestrailwaystations.html',{'res' : result})
    else:
        return render(request, 'nearestrailwaystations.html')

def findtrainfares(request):
    return render(request, 'findtrainfares.html')

def findtrainfaresresult(request):
    train = request.POST.get("trainNumber")
    source = request.POST.get("sourcestation")
    destination = request.POST.get("destinationstation")
    result = subprocess.Popen(
        ['php', 'findmytrain//static//php-files//trainfarescall.php', train, source, destination],
        stdout=subprocess.PIPE, universal_newlines=False, stderr=subprocess.STDOUT)
    print(result.stdout)
    for line in result.stdout:
        res = line
        break
    data = str(res, 'UTF-8')
    json_object = json.loads(data)
    traindet = json_object['result']['title']
    res = []
    if (len(json_object['result']['fare_details']) > 0):
        res.append(json_object['result']['fare_details'])
        # for r in json_object['result']['fare_details']:
        #     res.append(r)
        #     res.append(json_object['result']['fare_details'][r])
    return render(request, 'findtrainfaresresult.html', {'res' : res,'traindet' : {'tdetails':traindet}})