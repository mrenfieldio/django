from django.db import models

# Create your models here.
class teacher(models.Model):
    name=models.CharField(max_length=25)
    age=models.CharField(max_length=2)
    dept=models.CharField(max_length=25)
    def __str__(self):
        return self.dept

class batch(models.Model):
    name=models.CharField(max_length=25)
    year=models.CharField(max_length=25)
    def __str__(self):
        return self.year

class student(models.Model):
    name=models.CharField(max_length=25)
    dept=models.ForeignKey(teacher,on_delete=models.CASCADE) 
    year=models.ForeignKey(batch,on_delete=models.CASCADE) 
    age=models.CharField(max_length=2)   
    phone=models.CharField(max_length=10) 
    def __str__(self):
        return self.name