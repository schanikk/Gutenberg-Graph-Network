from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .models import Book, Character#Topic, Sentence, Character2Sentence
import json
from django.core import serializers

def api_home(request,*args, **kwargs):
    return JsonResponse({"message":"Hello From the API!!!"})


def collection(request,*args, **kwargs):
   
    response = serializers.serialize("json", Book.objects.all())
    print(response)
    print(JsonResponse(response, safe=False))
    return JsonResponse(response, safe=False)


def book(request,*args, **kwargs):
    book = Book.objects.get(id=id)
    response = book.characters.all()
    return JsonResponse({"data" : list(response)})


def character(request,*args, **kwargs):
    character = Character.objects.get(id=id)
    sentence = character.sentences.all()
    response = sentence.topics.all()
    return JsonResponse(response)


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)