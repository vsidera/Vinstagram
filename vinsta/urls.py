from django.urls import path
from .views import ImageListView, ImageCreateView
from . import views

urlpatterns = [
    path('', ImageListView.as_view(), name='vinsta-home'),
    path('post/new/', ImageCreateView.as_view(), name='image-create'),
]