from django.db import models
from django.utils.timezone import datetime

# Create your models here.
# Quando fazer uma alteração 
# python manage.py makemigrations
# python manage.py migrate
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    info = models.CharField(max_length=30)
    gender = models.CharField(max_length=50, choices =(
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ))   
    image = models.ImageField(upload_to='images/', blank = True)
    #date_added = models.DateField(auto_now_add=True) 
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']