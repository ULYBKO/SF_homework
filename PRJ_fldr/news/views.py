from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, PostCategory, Author
from datetime import datetime


class PostList(ListView):
    model= Post
    ordering= 'categoryType'
    template_name = 'flatpages/post.html'
    context_object_name= 'posts'

class PostDetail(DetailView):
    model = Post
    template_name='flatpages/post.html'  
    context_object_name= 'post'

    def get_context_data(self, kwargs):
        context = super().get_context_data(kwargs)
        context['time_now'] = datetime.utcnow()
        return context

class AuthorList(DetailView):
    model = Author
    template_name='flatpages/authors.html'
    context_object_name= 'authors'

