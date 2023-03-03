from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(label = 'books', max_length=100)
    file = forms.FileField()
