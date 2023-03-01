from django.contrib.auth.models import Book, Paragraph, Charakter, Topic
from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','name', 'publication', 'author']

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['id', 'para_number', 'parent_document', 'raw_text']

class CharakterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charakter
        fields = ['id', 'Name', 'Vorname', 'Nachname', 'parent_document']

    
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'topic_name', 'keywords']

