from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    CreateView,
)
from .models import Image


def home(request):
    context = {
        'posts': Image.objects.all()
    }
    return render(request, 'vinsta/home.html', context)

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

