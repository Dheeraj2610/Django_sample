
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class usermodel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    experience = models.BooleanField(default=False)
