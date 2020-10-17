from django.shortcuts import render
from .models import Image


def home(request):
    context = {
        'posts': Image.objects.all()
    }
    return render(request, 'vinsta/home.html', context)