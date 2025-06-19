from django.shortcuts import render
from . import models
from django.core.mail import send_mail
from decouple import config
from django.shortcuts import get_object_or_404

contact_email = config("CONTACT_EMAIL")

def main(request):
    context = {}
    return render(request , 'main/home.html' , context)

def about(request):
    context = {}
    return render(request , 'main/about.html' , context)

def work(request):
    categories = models.Category.objects.all()
    context = {'categories' : categories}
    return render(request , 'main/work.html' , context)

def tapes(request , category_id):
    category = get_object_or_404(models.Category , id=category_id)
    videos = category.videos.all()
    context = {'category' : category,
                'videos' : videos}
    return render(request , 'main/tapes.html' , context)

def contact(request):
    success = False
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if message and email:
            send_mail(
                    'New contact message!',
                    f'From: {email}\n\n{message}',
                    contact_email,  # Your verified sender email
                    [contact_email],
                    fail_silently=False,
                )
            success = True
    
    context = {'success' : success}
    return render(request , 'main/contact.html' , context)