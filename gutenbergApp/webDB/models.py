from django.db import models

# Create your models here.
class Book(models.Model):
    bookID =  models.CharField(max_length=100, blank=True, default='')
    bookName = models.CharField(max_length=100, blank=True, default='')
    bookauthor = models.TextField()
    # class Meta:
    #     ordering = ['created']

class Topic(models.Model):
    topicID = models.CharField(max_length=100, blank=True, default='')
    topicName = models.CharField(max_length=100, blank=True, default='')
    # class Meta:
    #     ordering = ['created']


class Character(models.Model):
    characterID = models.CharField(max_length=100,blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    ## bookID = models.TextField(max_length=100,blank=True,default='')
    bookID = models.ForeignKey(Book, on_delete=models.CASCADE)
    # class Meta:
    #     ordering = ['created']

class Sentence(models.Model):
    sentenceText = models.CharField(max_length=1000,blank=True, default='')
    ## bookID = models.CharField(max_length=100,blank=True,default='')
    bookID = models.ForeignKey(Book, on_delete=models.CASCADE)
    sentenceIndex = models.IntegerField(blank=True, default=0)
    # topicID = models.ForeignKey(Topic, on_delete=models.CASCADE)


# class Character2Sentence(models.Model):
#     ## characterID = models.CharField(mx_length=100, blank=True, default='')#
#     characterID = models.ForeignKey(Character, on_delete=models.CASCADE)
#     ## sentenceID = models.CharField(max_length=100, blank=True, default='')
#     sentenceID = models.ForeignKey(Sentence, on_delete=models.CASCADE)
#     # class Meta:
#     #     ordering = ['created']



