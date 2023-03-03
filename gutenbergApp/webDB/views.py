from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
# from .forms import ModelFormWithFileField
from .models import Book, Character, Sentence, Topic, Character2Sentence

def api_home(request,*args, **kwargs):
    return JsonResponse({"message":"Hello From the API!!!"})


def collection(request,*args, **kwargs):
    response = Book.objects.all()
    return JsonResponse(response)


def book(request,*args, **kwargs):
    book = Book.objects.get(id=id)
    response = book.characters.all()
    return JsonResponse(response)


def character(request,*args, **kwargs):
    character = Character.objects.get(id=id)
    sentence = character.sentences.all()
    response = sentence.topics.all()
    return JsonResponse(response)


# def upload_file(request):
#     if request.method == 'POST':
#         form = ModelFormWithFileField(request.POST, request.FILES)
#         if form.is_valid():
#             # file is saved
#             form.save()
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = ModelFormWithFileField()
#     return render(request, 'upload.html', {'form': form})

# def handle_uploaded_file(f):
#     with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)