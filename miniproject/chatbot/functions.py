import requests
from django.http import HttpResponse
import nltk
import random
import string
import warnings
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem import PorterStemmer,WordNetLemmatizer


def sentence_tokenize(user_string):
    sent_tokens = sent_tokenize(user_string)
    return sent_tokens

def wordwise_tokenize(inputstring):
    word_tokens = []
    for sent in inputstring:
        l=word_tokenize(sent)
        for i in l:
            word_tokens.append(i)
    return word_tokens

def stopwordremoval(word_tokens):
    stop_words = set(stopwords.words('english'))
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    return filtered_sentence

def remove_punctuation(stop_words):
    stopwords_en = set(stopwords.words('english'))
    stopwords_en_withpunct = stopwords_en.union(set(punctuation))
    stop_words_without_punct = [word for word in stop_words if word not in stopwords_en_withpunct]
    return stop_words_without_punct

def stemming(stop_words):
    ps = PorterStemmer()
    sw=[]
    for w in stop_words:
        sw.append(ps.stem(w))
    return sw

def lemmatization(stem_words):
    lemmatizer = WordNetLemmatizer()
    lem_words = [lemmatizer.lemmatize(word) for word in stem_words]
    return lem_words

def searchRailwayStation(searchValue):
    # searchValue = "Chennai"
    url = "https://indianrailways.p.rapidapi.com/findstations.php"
    querystring = {"station": searchValue}
    headers = {
        'x-rapidapi-host': "indianrailways.p.rapidapi.com",
        'x-rapidapi-key': "6ec2fdd9c9msh434f364619314f9p142174jsn42ea28ccc186"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    res = response.json()
    output = ""
    for station in res['stations']:
        output += station['stationName'] + '-' + station['stationCode'] + ", "
    return output

def searchTrain(searchValue):
    # searchValue = '12797'
    url = "https://trains.p.rapidapi.com/"
    payload = "{\r\"search\": \"" + searchValue + "\"\r}"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "trains.p.rapidapi.com",
        'x-rapidapi-key': "6ec2fdd9c9msh434f364619314f9p142174jsn42ea28ccc186"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    res = response.json()
    output = ""
    for train in res:
        output = output + "train no: " + str(train["train_num"]) + ', Train Name: ' + train[
            "name"] + ", Travels from: " + train["train_from"] + " to " + train["train_to"]
    return output

def botReply(usermessage):
    sent_tokens = sentence_tokenize(usermessage)
    word_tokens = wordwise_tokenize(sent_tokens)
    stop_words = stopwordremoval(word_tokens)
    stop_words = remove_punctuation(stop_words)
    stem_words = stemming(stop_words)
    lemmatized_words = set(lemmatization(stem_words))
    print(lemmatized_words)
    station = set(["railway", "station", "what"])
    train_name = set(['number', 'train', 'which'])
    train_number = set(['number', 'train'])
    output="Sorry I didn't find any answer!"
    if(station.issubset(lemmatized_words)):
        searchWord = lemmatized_words.difference(station)
        output = searchRailwayStation(searchWord)
    if(train_number.issubset(lemmatized_words)):
        searchWord = list(lemmatized_words.difference(train_number))[0]
        print(searchWord)
        output = searchTrain(searchWord)
    if(train_name.issubset(lemmatized_words)):
        print(lemmatized_words)
        searchWord = list(lemmatized_words.difference(train_name))[0]
        print(searchWord)
        print(searchWord)
        output = searchTrain(searchWord)
    return output