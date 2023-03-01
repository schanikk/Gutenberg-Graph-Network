from django.urls import include, path
from rest_framework import routers
from webDB import views

router = routers.DefaultRouter()
router.register(r'book', views.BookViewSet)
router.register(r'paragraph', views.ParagraphViewSet)
router.register(r'charakter', views.CharacterViewSet)
router.register(r'topic', views.TopicViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]