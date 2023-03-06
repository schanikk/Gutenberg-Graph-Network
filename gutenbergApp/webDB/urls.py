from django.urls import include, path
from rest_framework import routers
from webDB import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.api_home),
    path('collection/', views.collection),
    path('book/<int:id>', views.book),
    path('character/<int:id>', views.character),
    path('bookTopic/<int:id>', views.bookTopics)
]
