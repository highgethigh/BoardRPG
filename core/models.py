from django.contrib.auth import get_user_model
from allauth.account.signals import user_logged_in


# Create your models here.

User = get_user_model()

def user_logged_in_receiver(request, user):
    print(request)
    print(user)

user_logged_in.connect(user_logged_in_receiver, sender=User)