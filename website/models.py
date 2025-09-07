from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Newsletter(models.Model):
    email = models.EmailField(max_length=100)


    def __str__(self):
        return self.email