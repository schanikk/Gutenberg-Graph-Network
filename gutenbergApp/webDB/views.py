from django.contrib.auth.models import Book, Paragraph, Charakter, Topic
from rest_framework import viewsets
from rest_framework import permissions
from gutenbergApp.webDB.Serializers import BookSerializer, CharakterSerializer, ParagraphSerializer, TopicSerializer
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all().order_by('-date_joined')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class ParagraphViewSet(viewsets.ModelViewSet):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer
    permission_classes = [permissions.IsAuthenticated]


class CharakterSet(viewsets.ModelViewSet):
    queryset = Charakter.objects.all()
    serializer_class = CharakterSerializer
    permission_classes = [permissions.IsAuthenticated]


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticated]