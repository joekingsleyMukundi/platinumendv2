from django.core.mail import  send_mail, BadHeaderError

def send_mail_to_user(user, subject, message):
    from_email = 'ehoomes@novaluxicawriters.com'
    try:
        send_mail(subject, message, from_email, [user.email]);
        print('sent')
    except BadHeaderError:
       raise BadHeaderError("Invalid header found")