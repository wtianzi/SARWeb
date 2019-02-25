from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    def __str__(self):
        return self.first_name

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    taskpolygon = models.CharField(max_length=10000)
    notes = models.CharField(max_length=30)
    def __str__(self):
        return self.notes
