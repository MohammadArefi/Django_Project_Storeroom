from django.db import models
from .validators import *


class Project(models.Model):
    project_id = models.BigIntegerField(primary_key=True, unique=True)
    project_name = models.CharField(max_length=50, validators=[persian_valid])

    def __str__(self):
        return "{} - {}".format(self.project_id, self.project_name)


class Product(models.Model):
    pid = models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    category = models.CharField(max_length=100)
    device_type = models.CharField(max_length=50)
    device_status = models.CharField(max_length=50)
    device_brand = models.CharField(max_length=50)
    device_mileage = models.CharField(max_length=50)
    description = models.TextField()
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    image_3 = models.ImageField()
    image_4 = models.ImageField()
    image_5 = models.ImageField()
    image_6 = models.ImageField()

    def __str__(self):
        return "{} - {} - {}".format(self.pid, self.name, self.project.project_name)


class Status(models.Model):
    sid = models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    pid = models.ForeignKey(Product, on_delete=models.PROTECT)
    ST = [(1, 'entry'),
          (2, 'Temporary exit'),
          (3, 'permanent exit'),
          ]
    status = models.CharField(max_length=1, choices=ST, default=1)
    time = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return f"{self.status}"

