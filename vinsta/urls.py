from django.urls import path
from .views import CommentListView
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='vinsta-home'),
    path('comment/<int:id>', CommentListView.as_view(), name='vinsta-comment'),
    url(r'^user/(\d+)/$', views.user, name='users'),
    url(r'comments/(\d+)/', CommentListView.as_view(), name='vinsta-comment'),
    url(r'new/image$', views.new_image, name='new_image'),
]