from django.db import models
from django.utils import timezone
class user_data(models.Model):
    task_name=models.CharField(max_length=200)
    start_date=models.DateTimeField()
    finish_date=models.DateTimeField()

# Create your models here