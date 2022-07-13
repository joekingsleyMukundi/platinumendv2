from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .models import CustomUser
from .errors import ValidationError

def user_not_active(func):
  def wrapper (request, *args, **kwargs):
    uid = kwargs['uid']
    id = smart_bytes(urlsafe_base64_decode(uid))
    user = CustomUser.objects.get(id=id)
    if user.is_active:
      raise ValidationError('user is already active')
    return func(request, *args, **kwargs)
  return wrapper