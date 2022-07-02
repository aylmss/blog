from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView


from .models import Post
# Create your views here.

class blogListView(ListView):
    model = Post
    template_name = 'home.html'

class blogDetailView(DetailView):
    model=Post
    template_name = 'post_detail.html'

class blogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class blogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

