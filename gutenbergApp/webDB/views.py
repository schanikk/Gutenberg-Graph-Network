from .models import Book, Paragraph, Character, Topic
from rest_framework import viewsets
from rest_framework import permissions
from .Serializers import BookSerializer, CharacterSerializer, ParagraphSerializer, TopicSerializer



class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all() # .order_by('-date_joined')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class ParagraphViewSet(viewsets.ModelViewSet):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer
    permission_classes = [permissions.IsAuthenticated]


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticated]


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticated]
    
