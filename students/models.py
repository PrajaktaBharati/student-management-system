from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)

    roll_number = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.name
