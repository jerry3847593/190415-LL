from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
# Create your views here.

def page(request):
    posts = Post.objects
    return render (request, 'introduce/page.html', {'posts':posts})

def particular(request):
    return render(request, 'introduce/particular.html')