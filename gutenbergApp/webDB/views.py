from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .models import Book, Character, Topic, Sentence,sent2char
import json
from django.core import serializers
from django.forms.models import model_to_dict


def api_home(request,*args, **kwargs):
    return JsonResponse({"message":"Hello From the API!!!"})


def collection(request,*args, **kwargs):
   
    response = serializers.serialize("json", Book.objects.all())
    print(response)
    print(JsonResponse(response, safe=False))
    return JsonResponse(response, safe=False)


def book(request,*args, **kwargs):
    book = Book.objects.get(pk=1)
    print(book)
    #response=serializers.serialize("json",Book.objects.all())
    return JsonResponse(model_to_dict(book))


def character(request,*args, **kwargs):
    character = model_to_dict(Character.objects.get(pk=1))
    sent2chars= sent2char.objects.all().values()
    sentences=Sentence.objects.all().values()
    topics=Topic.objects.all().values()

    # CreateDistr
    list_of_Sent=list(filter(lambda x: x['fields']['charID']==id, sent2chars))

    for sent in list_of_Sent:
        toSearch=sent['fields']['sentID']
        sentences=list(filter(lambda x: x['pk']==toSearch,sentences))

    bookid=next(filter(lambda x: x['pk']==id, character))['fields']['bookID']
    allTopics=list(filter(lambda x: x['fields']['bookindex']==bookid, topics))

    distr_=dict()
    for topic in allTopics:
        distr_[topic['fields']['TopicID']]= {'TopicName:':topic['fields']['Name'], 'Count':0}
    for sent in sentences:
        distr_[sent['fields']['topicID']]['Count']+=1


    print(distr_)

    return JsonResponse(dict_)


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
