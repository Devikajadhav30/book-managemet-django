from .views import AuthorViewSet,CategoryViewSet,BookViewSet
from rest_framework.routers import SimpleRouter
from django.urls import path,include

router = SimpleRouter()

router.register('author',AuthorViewSet)
router.register('book',BookViewSet)
router.register('category',CategoryViewSet)


urlpatterns = [
    path('',include(router.urls)),
]
