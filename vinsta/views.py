from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Image


def home(request):
    context = {
        'posts': Image.objects.all()
    }
    return render(request, 'vinsta/home.html', context)

class ImageListView(ListView):
    model = Image
    template_name = 'vinsta/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-created_on']    