from django.db import models

# Create your models here.


class my_work(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    description = models.TextField()