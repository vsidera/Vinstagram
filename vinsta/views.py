from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    CreateView,
)
from .models import Image , Profile, Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import uploadForm



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

# @login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user.profile
    if request.method == 'POST':
        form = uploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('vinsta-home')
    else:
        form = uploadForm()
    return render(request, 'vinsta/image_form.html', {'form':form})
        

class CommentListView(ListView):
    model = Comment
      # <app>/<model>_<viewtype>.html
    context_object_name = 'comments'            

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'vinsta/comment_list.html'
    fields = ['comment_body']
    
    
    
   