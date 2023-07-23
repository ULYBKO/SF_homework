from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, PostCategory, Author


class Post(ListView):
    model= Post
    ordering= 'categoryType'
    template_name = 'news.html'
    context_object_name= 'posts'

class PostDetail(DetailView):
    model = Post
    template_name='post.html'
    context_object_name= 'post'

class AuthorList(DetailView):
    model = Author
    template_name='authors.html'
    context_object_name= 'authors'