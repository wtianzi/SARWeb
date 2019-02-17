from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    def __str__(self):
        return self.first_name+" "+self.last_name

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    leader=models.CharField(max_length=30)
    member1=models.CharField(max_length=30)
    member2=models.CharField(max_length=30)
    member3=models.CharField(max_length=30)
    member4=models.CharField(max_length=30)
    member5=models.CharField(max_length=30)
    member6=models.CharField(max_length=30)
    member7=models.CharField(max_length=30)
    member8=models.CharField(max_length=30)
    member9=models.CharField(max_length=30)
    member10=models.CharField(max_length=30)
    member11=models.CharField(max_length=30)
    member12=models.CharField(max_length=30)
    member13=models.CharField(max_length=30)
    member14=models.CharField(max_length=30)
    member15=models.CharField(max_length=30)
    member16=models.CharField(max_length=30)
    member17=models.CharField(max_length=30)
    member18=models.CharField(max_length=30)
    member19=models.CharField(max_length=30)
    member20=models.CharField(max_length=30)
    other_members=models.CharField(max_length=30)
    def __str__(self):
        return self.leader
