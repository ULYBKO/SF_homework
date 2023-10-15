from django.urls import path
from .views import *
from .views import CategoryListView
from .import views
from django.views.decorators.cache import cache_page

urlpatterns = [
   path ('', PostList.as_view(), name ='post_list'),
   path ('post_list/', PostList.as_view(), name ='post_list'),
   path('article/', ArticleList.as_view(), name='article_list'),
   path('news/', cache_page(60*10)(NewsList.as_view()), name='news_list'),
 

   
   path ('search/', NewSearch.as_view(), name='search'),
   path('subscriptions/', subscriptions, name='subscriptions'),
   path('categories/<int:pk>', CategoryListView.as_view(), name = 'category_list'),
   
   #Новость
   path ('<int:pk>/', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='news_create'),
   path('<int:pk>/edit/', PostEdit.as_view(), name='news_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
   #Статья
   path('article/<int:id>/', ArticleDetail.as_view(), name='article_detail'),
   path('article/create/', PostCreate.as_view(), name='article_create'),
   path('article/<int:pk>/edit/', ArticleEdit.as_view(), name='article_edit'),
   path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),

]  