from django.db import models

# Create your models here.

class pro(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField() 

    def __str__(self):
        return self.name
    
class user(models.Model):
    name=models.CharField(max_length=15)
    email=models.CharField(max_length=25)

    def __str__(self):
        return self.name

class prodetails(models.Model):
    img=models.ImageField(upload_to='mypic/')
    name=models.CharField(max_length=20)
    price=models.IntegerField()

    def __str__(self):
        return self.name