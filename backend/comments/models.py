from django.db import models;
from authentication.models import User;

# Create your models here.
class Comment(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    breed= models.CharField(max_length=255)
    dog_name= models.CharField(max_length=255)
    comment= models.CharField(max_length=255)