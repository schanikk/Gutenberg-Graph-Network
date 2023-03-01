from .models import Book, Paragraph, Character, Topic
from rest_framework import serializers



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','name', 'publication', 'author']

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['id', 'para_number', 'parent_document', 'raw_text']

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'Name', 'Vorname', 'Nachname', 'parent_document']

    
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'topic_name', 'keywords']

