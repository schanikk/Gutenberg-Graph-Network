from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .models import Book, Character, Topic, Sentence,sent2char
import json
from django.core import serializers
from django.forms.models import model_to_dict
from django.db import connection


def api_home(request,*args, **kwargs):
    return JsonResponse({"message":"Hello From the API!!!"})


def collection(request,*args, **kwargs):
   
    response = serializers.serialize("json", Book.objects.all())
    print(response)
    print(JsonResponse(response, safe=False))
    return JsonResponse(response, safe=False)


def book(request,id):
    characters = Character.objects.filter(bookID=id)
    print(characters)
    print(book)
    res = serializers.serialize('json', characters)
    #response=serializers.serialize("json",Book.objects.all())
    return JsonResponse(res,safe=False)

def characters(request,id):
    rel_sent2char = sent2char.objects.filter(charID=id)
    sents_ = list()
    for rel in rel_sent2char:
        sents_.append(rel.sentID)

    topics_ = list()
    for sent in sents_:
        topics_.append(sent.topicID)
    print(sents_)
    print(topics_)



    res = serializers.serialize("json", sents_)
    res2 = serializers.serialize("json", topics_)

    characterBook = Character.objects.get(pk=id)
    all_topics = Topic.objects.filter(bookID=characterBook.bookID)

    relTopics=list()
    for topic in all_topics:
        relTopics.append(model_to_dict(topic))


    return JsonResponse(res2, safe=False)




def character(request,id):
    sent2chars= sent2char.objects.all()
    sentences=Sentence.objects.all()
    topics=Topic.objects.all()


    sent2chars_=list()
    for s2c in sent2chars:
        sent2chars_.append(model_to_dict(s2c))


    sentences_=list()
    for sent in sentences:
        sentences_.append(model_to_dict(sent))

    topics_ = list()
    for top in topics:
        topics_.append(model_to_dict(top))

    print(topics_)
    
    # CreateDistr
    list_of_Sent=list(filter(lambda x: x['charID']==id, sent2chars_))

    for sent in list_of_Sent:
        toSearch=sent['sentID']
        sentences=list(filter(lambda x: x['id']==toSearch,sentences_))

    bookid=Character.objects.get(pk=id).bookID.pk
    print(bookid)
    allTopics=list(filter(lambda x: x['bookID']==bookid, topics_))
        
    print(allTopics)


    distr_=dict()
    for topic in allTopics:
        print(topic)
        distr_[topic['TopicID']]= {'TopicName:':topic['TopicName'], 'Count':0}
    for sent in sentences:
        print(sent)
        distr_[sent['topicID']]['Count']+=1

    return JsonResponse(distr_)


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
