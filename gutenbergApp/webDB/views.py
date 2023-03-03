from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ModelFormWithFileField

def api_home(request,*args, **kwargs):
    return JsonResponse({"message":"Hello From the API!!!"})


def collection(request,*args, **kwargs):
    response = {
            "data": [
                {"id":1, "name":"Book1", "author":"Author1"},
                {"id":2, "name":"Book2", "author":"Author2"},
                {"id":3, "name":"Book3", "author":"Author3"},
                {"id":4, "name":"Book4", "author":"Author4"},
                ]
            }
    return JsonResponse(response)


def book(request,*args, **kwargs):
    response = {
            "data": [
                {"id":1, "name":"Character1", "parent":1},
                {"id":2, "name":"Character2", "parent":1},
                {"id":3, "name":"Character3", "parent":1},
                {"id":4, "name":"Character4", "parent":1},
                ]
            }
    return JsonResponse(response)


def character(request,*args, **kwargs):
    response = {
            "data": [
                {"id":1, "name":"Topic1", "count":25},
                {"id":2, "name":"Topic2", "count":5},
                {"id":3, "name":"Topic3", "count":55},
                {"id":4, "name":"Topic4", "count":12},
                ]
            }
    return JsonResponse(response)


def upload_file(request):
    if request.method == 'POST':
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = ModelFormWithFileField()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)