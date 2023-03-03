from django.db import models

# Create your models here.
class Book(models.Model):
    bookID = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.TextField()
    class Meta:
        ordering = ['created']



class Character(models.Model):
    characterID = models.CharField(max_length=100,blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    bookID = models.TextField(max_length=100,blank=True,default='')
    class Meta:
        ordering = ['created']

class Sentence(models.Model):
    sentenceText = models.CharField(max_length=1000,blank=True, default='')
    bookID = models.CharField(max_length=100,blank=True,default='')


class Topic(models.Model):
    topicID = models.CharField(max_length=100, blank=True, default='')
    topicName = models.CharField(max_length=100, blank=True, default='')
    class Meta:
        ordering = ['created']



class Character2Sentence(models.Model):
    characterID = models.CharField(mx_length=100, blank=True, default='')
    sentenceID = models.CharField(max_length=100, blank=True, default='')
    class Meta:
        ordering = ['created']



