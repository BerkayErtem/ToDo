from django.db import models

# Create your models here.

class Todo(models.Model):
    title=models.CharField(max_length=50, blank=False)
    description=models.CharField(max_length=50, blank=True)
    created_at=models.DateField(auto_now=True)
    is_active=models.BooleanField(null=True)