from django.db import models


# Create your models here.

class travel(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class team(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name
