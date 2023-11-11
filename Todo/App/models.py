from django.db import models

# Create your models here.
class TASK(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    completed=models.BooleanField()
    created_at=models.DateTimeField()
