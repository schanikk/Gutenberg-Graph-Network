from django.urls import include, path
from rest_framework import routers
from webDB import views

router = routers.DefaultRouter()
router.register(r'Book', views.BookViewSet)
router.register(r'Paragraph', views.ParagraphViewSet)
router.register(r'Charakter', views.CharacterViewSet)
router.register(r'Topic', views.TopicViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]