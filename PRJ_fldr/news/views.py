from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, PostCategory, Author


class PostList(ListView):
    model= Post
    ordering= 'categoryType'
    template_name = 'flatpages/news.html'
    context_object_name= 'posts'

class PostDetail(DetailView):
    model = Post
    template_name='flatpages/post.html'
    context_object_name= 'postlist'

class AuthorList(DetailView):
    model = Author
    template_name='flatpages/authors.html'
    context_object_name= 'authors'