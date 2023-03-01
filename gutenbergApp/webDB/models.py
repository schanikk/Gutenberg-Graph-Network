from django.db import models

# Create your models here.

class Book (models.Model):
    id = models.int()
    Name = models.CharField(max_length=50)
    publication = models.DateTimeField('date published')
    author = models.CharField(max_length=50)

class Paragraph (models.Model):
    id = models.int()
    para_number = models.IntField()
    parent_document = models.Charfield(Max_length=50)
    raw_text = models.Charfield(max_length = 10000)

class Character (models.Model):
    id = models.int()
    Name = models.CharField(max_length=50)
    Vorname = models.CharField(max_length=50)
    Nachname = models.CharField(max_length=50)
    parent_document = models.Charfield(Max_length=50)

class Topic (models.model):
    id = models.int()
    topic_name = models.CharField(max_length=50)
    keywords = models.CharField(max_length = 50)
