from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    x = 1
    x = 2
    return render(request, "hello.html")
