from  django.db.models.signals import post_save
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .mails import send_mail_to_user
from .models import CustomUser

def  user_created(sender, instance, created, **kwargs):
    if created:
        user = instance
        token = user.activationtoken
        uid = urlsafe_base64_encode(smart_bytes(user.id))
        subject = 'Verification'
        message = 'Please click on the link to verify your email: http://localhost:8000/api/v1/auth/activate/' + uid + '/' + token + '/'
        send_mail_to_user (user, subject, message)

post_save.connect(user_created, sender=CustomUser)
