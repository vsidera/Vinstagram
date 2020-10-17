from django.urls import path
from .views import ImageListView
from . import views

urlpatterns = [
    path('', ImageListView.as_view(), name='vinsta-home'),
]