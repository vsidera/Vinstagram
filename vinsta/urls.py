from django.urls import path
from .views import ImageListView, ImageCreateView, CommentListView
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ImageListView.as_view(), name='vinsta-home'),
    path('comment/<int:id>', CommentListView.as_view(), name='vinsta-comment'),
    path('post/new/', ImageCreateView.as_view(), name='image-create'),
    url(r'^user/(\d+)/$', views.user, name='users'),
    url(r'comments/(\d+)/', CommentListView.as_view(), name='vinsta-comment'),
]