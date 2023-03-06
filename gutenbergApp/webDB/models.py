from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Book(models.Model):
    bookID =  models.CharField(max_length=1000, blank=True, default='')
    bookName = models.CharField(max_length=5000, blank=True, default='')
    bookauthor = models.CharField(max_length=5000, blank=True, default='')
    bookAuthorYearOfBirth=models.CharField(max_length=50, blank=True,default='')
    bookAuthorYearOfDeath=models.CharField(max_length=50, blank=True,default='')
    bookLanguage=models.CharField(max_length=5000, blank=True,default='')
    bookSubjects=models.CharField(max_length=5000, blank=True,default='')
    # class Meta:
    #     ordering = ['created']

class Topic(models.Model):
    TopicID = models.IntegerField(default=0)
    TopicName = models.CharField(max_length=1000, blank=True, default='')

    default_=list
    Top_n_words = ArrayField(
            models.CharField(max_length=200, blank=True),
            size=15,
            default=default_
        )
    bookID = models.ForeignKey(Book, on_delete=models.CASCADE, default=0)
    # class Meta:
    #     ordering = ['created']


class Character(models.Model):
    Name = models.CharField(max_length=1000, blank=True, default='')
    ## bookID = models.TextField(max_length=100,blank=True,default='')
    bookID = models.ForeignKey(Book, on_delete=models.CASCADE, default=0)
    # class Meta:
    #     ordering = ['created']

class Sentence(models.Model):
    bookID = models.ForeignKey(Book, on_delete=models.CASCADE, default=0)
    sentenceText = models.TextField(default='')
    sentIDBook=models.IntegerField(default=0)
    topicID=models.ForeignKey(Topic,on_delete=models.CASCADE, default=0)


class sent2char(models.Model):
    sentID = models.ForeignKey(Sentence, on_delete=models.CASCADE, default=0)
    charID = models.ForeignKey(Character, on_delete=models.CASCADE, default=0)
