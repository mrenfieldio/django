from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=25)
    age=models.CharField(max_length=25)
    dept=models.CharField(max_length=25)
    program=models.CharField(max_length=25)
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=25)


    def __str__(self):
        return self.name
