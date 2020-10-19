from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    CreateView,
)
from .models import Image , Profile, Comment
from django.contrib.auth.models import User


def home(request):
    context = {
        'posts': Image.objects.all()
    }
    return render(request, 'vinsta/home.html', context)

def user(request, user_id):
    users = User.objects.filter(id=user_id)
    pics = Image.objects.filter(profile=user_id).all()    
    return render(request, 'vinsta/user.html', {'pics':pics, 'users':users})    

class ImageListView(ListView):
    model = Image
    template_name = 'vinsta/homeclone.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-created_on']    

class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    fields = ['image', 'caption']

    def form_valid(self, form):
        form.instance.user.profile = self.request.user
        return super().form_valid(form)    

class CommentListView(ListView):
    model = Comment
      # <app>/<model>_<viewtype>.html
    context_object_name = 'comments'            

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'vinsta/comment_list.html'
    fields = ['comment_body']


