from celery import shared_task
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.models import User



@shared_task(bind=True)
def test_func(self):
    #operations
    for i in range(10):
        print(i)
    return "Done"

@shared_task(bind=True)
def send_email(self):
    users=User.objects.filter(is_superuser=False)
    for user in users:
        mail_subject="Email Testing"
        message="Hi,Celery Testing" 
        to_email=user.email
        print(to_email)
        send_mail=EmailMessage(subject=mail_subject,body=message,from_email=settings.EMAIL_HOST_USER,to=[to_email])
        send_mail.send()
        print('email')
        
    return "Done"
