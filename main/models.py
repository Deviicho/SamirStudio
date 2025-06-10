from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='skills/')
    
class Project(models.Model):
    name = models.CharField(max_length=150)
    thumbnail = models.ImageField(upload_to='projects/')
    link = models.CharField(max_length=300 , null=True)
    
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    is_theOne = models.BooleanField(default=False)