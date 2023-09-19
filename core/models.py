from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/projects/')
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Client(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/clients/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title