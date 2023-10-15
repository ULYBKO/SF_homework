from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Post, PostCategory
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.db.models.signals import post_save, m2m_changed

def send_notifications(preview, pk, title, subscribers):
    html_content = render_to_string(
        'flatpages/post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/post_list/{pk}'
        }
    )


    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )


    msg.attach_alternative(html_content, 'text/html')
    msg.send()



@receiver(m2m_changed, sender=PostCategory)
def new_post(sender, instance, **kwargs): 

    if kwargs['action']=='post_add':
        categories = instance.postCategory.all()
        subscribers: list[str]=[]
        for category in categories:
            subscribers+= category.subscribers.all()

        subscribers = [s.email for s in subscribers ]
    
        send_notifications(instance.preview(), instance.pk, instance.title, subscribers)