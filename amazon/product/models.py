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
    
class category(models.Model):
    cname=models.CharField(max_length=20)
    def __str__(self):
        return self.cname
    
class subcat(models.Model):
    sname=models.CharField(max_length=20)
    cat=models.ForeignKey(category,on_delete=models.CASCADE)

    def __str__(self):
        return self.sname

class department(models.Model):
    dname=models.CharField(max_length=20)
    def __str__(self):
        return self.dname
    
class stud(models.Model):
    studname=models.CharField(max_length=20)
    commona=models.ForeignKey(department,on_delete=models.CASCADE)
    def __str__(self):
        return self.studname