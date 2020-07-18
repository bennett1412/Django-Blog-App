from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here

class post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    