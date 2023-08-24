from django.db import models

# Create your models here.
# Creating tables as classes

class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    course = models.CharField(max_length=100)
    age = models.TextField()
    
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    salary = models.TextField()
