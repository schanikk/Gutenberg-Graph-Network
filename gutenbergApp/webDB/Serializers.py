from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = 
        fields = ['id','name', 'publication', 'author']

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = 
        fields = ['id', 'para_number', 'parent_document', 'raw_text']

class CharakterSerializer(serializers.ModelSerializer):
    class Meta:
        model = 
        fields = ['id', 'Name', 'Vorname', 'Nachname', 'parent_document']

    
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = 
        fields = ['id', 'topic_name', 'keywords']

