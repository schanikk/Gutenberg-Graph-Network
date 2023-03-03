from django.shortcuts import render
from django.http import HttpResponse
import json


def hello(request):
    return render(request, "hello.html")

