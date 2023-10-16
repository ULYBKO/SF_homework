from django.shortcuts import render
from django.db.models import Exists, OuterRef
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Author,Category, Subscription
from datetime import datetime
from .filters import PostFilter
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from .forms import PostForm
from django.core.cache import cache

class PostList(ListView):
    model= Post
    ordering= 'dateCreation'
    template_name = 'flatpages/post.html'# TODO SHUT
    context_object_name= 'posts'# FIXME ASFAS
    paginate_by = 20

    
    def get_queryset(self):
       queryset = super().get_queryset()
       self.filterset = PostFilter(self.request.GET, queryset)
       return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filterset'] = self.filterset
        context['time_now'] = datetime.utcnow()
        return context

class PostDetail(DetailView):
    model = Post
    template_name='flatpages/post_detail.html'  
    context_object_name= 'post'


    def get_object(self, *args, **kwargs): # переопределяем метод получения объекта, как ни странно
        obj = cache.get(f'product-{self.kwargs["pk"]}', None) # кэш очень похож на словарь, и метод get действует так же. Он забирает значение по ключу, если его нет, то забирает None.
 
        # если объекта нет в кэше, то получаем его и записываем в кэш
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'product-{self.kwargs["pk"]}', obj)
            
            return obj    

class AuthorList(DetailView):
    model = Author
    template_name='flatpages/authors.html'
    context_object_name= 'authors'


class NewsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news_list.html'
    context_object_name = 'Posts'
    paginate_by = 6

    def get_queryset(self):
        queryset = Post.objects.filter(categoryType = 'NW')
        return queryset
    

class NewSearch(ListView):
    model= Post
    ordering= 'dateCreation'
    template_name = 'flatpages/search.html'
    context_object_name= 'search'
    paginate_by = 6

    def get_queryset(self):
       queryset = super().get_queryset()
       self.filterset = PostFilter(self.request.GET, queryset)
       return self.filterset.qs

        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['time_now'] = datetime.utcnow()
        return context
    


class PostCreate(CreateView):
    #permission_required = 'newsapp.add_news'
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'flatpages/news_create.html'

    def form_valid(self, form):
        post=form.save(commit=False)
        if self.request.path=='/article/create/':
            post.postCategory = 'AR'
        post.save()
        return super().form_valid(form)


class PostEdit(UpdateView):
    #permission_required = ('newsapp.change_news',)
    form_class = PostForm
    model = Post
    template_name = 'flatpages/news_edit.html'
    success_url = reverse_lazy('post_list')

class PostDelete(DeleteView):
    permission_required = ('newsapp.delete_news',)
    model = Post
    template_name = 'flatpages/news_delete.html'
    success_url = reverse_lazy('post_list')
    



class ArticleList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'article_list.html'
    context_object_name = 'Posts'
    paginate_by = 10


class ArticleDetail(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'Post'
    pk_url_kwarg = 'id'




class ArticleEdit(UpdateView):
    permission_required = ('newsapp.update_article',)
    form_class = PostForm
    model = Post
    template_name = 'flatpages/article_edit.html'




class ArticleDelete(DeleteView):
    permission_required = ('newsapp.delete_article',)
    model = Post
    template_name = 'flatpages/article_delete.html'
    success_url = reverse_lazy('post_list')


@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscription.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscription.objects.filter(
                user=request.user,
                category=category,
            ).delete()

    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(
            Subscription.objects.filter(
                user=request.user,
                category=OuterRef('pk'),
            )
        )
    ).order_by('name')
    return render(
        request,
        'subscriptions.html',
        {'categories': categories_with_subscriptions},
    )


class CategoryListView(ListView):
    model = Post
    template_name = 'flatpages/category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(postCategory=self.category).order_by('-dateCreation')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context

