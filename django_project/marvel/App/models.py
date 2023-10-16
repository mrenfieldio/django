from django.db import models

# Create your models here.
class bas_db(models.Model):
    name=models.CharField(max_length=20)
    age=models.CharField(max_length=2)
    phone=models.CharField(max_length=20)
    address=models.CharField(max_length=50)