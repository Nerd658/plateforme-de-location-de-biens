from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    ville = models.CharField(max_length=100, blank=True, null=True) 
    telephone = models.CharField(max_length=15, blank=True, null=True)  

    def __str__(self):
        return self.user.username

