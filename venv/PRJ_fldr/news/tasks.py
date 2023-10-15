import datetime

from celery import shared_task
import time
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.db.models.signals import post_save, m2m_changed
from .models import Post, PostCategory, Author,Category, Subscription


@shared_task
def send_email_task(pk):
    post = Post.objects.get(pk=pk)
    categories = post.post_category.all()
    title = post.post_title
    subscribers_emails = []
    for category in categories:
        subscribers_users = category.subscribers.all()
        for sub_user in subscribers_users:
            subscribers_emails.append(sub_user.email)
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': f'{post.post_title}',
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to= subscribers_emails,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

    


@shared_task
def weekly_notifications():
    today = datetime.datetime.now()
    last_week= today - datetime.timedelta(days=7)
    posts = Post.objects.filter(dateCreation__gte=last_week)
    categories = set(posts.calues_list('postCategory__name', flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,


        }
    )
    
    
    msg = EmailMultiAlternatives(
        subject="Posts for the week",
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers
    )
    
    msg.attach_alternative(html_content, 'text/html')
    msg.send()