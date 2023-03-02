from django.shortcuts import render
from django.http import HttpResponse
import requests
import json


def hello(request):
    return render(request, "hello.html")


def test(request):
    f = open("C:/Users/main4/Desktop/Gutenberg Projekt/Gutemberg-Graph-Network/gutenbergCorpus/data/dummy/DataFrontEnd.json")
    data = json.load(f)
    good = json.dumps(data)
    print(good)
    return HttpResponse(good)
  