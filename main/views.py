from django.shortcuts import render
from . import models
from django.core.mail import send_mail
from decouple import config

contact_email = config("CONTACT_EMAIL")

def main(request):
    # profile = models.Image.objects.filter(is_theOne=True).first()
    context = {}
    return render(request , 'main/home.html' , context)

def about(request):
    context = {}
    return render(request , 'main/about.html' , context)

def skills_and_projects(request):
    # skills = models.Skill.objects.all()
    projects = models.Project.objects.all()
    
    context = {
               'projects' : projects,
               }
    
    return render(request , 'main/skills&projects.html' , context)

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