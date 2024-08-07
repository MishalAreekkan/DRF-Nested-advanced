from django.urls import path,include
from .views import SongViewSet,SingerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'singer',SingerViewSet,basename='singer')
router.register(r'song',SongViewSet,basename='song')
urlpatterns = [
    path('',include(router.urls)),
]
