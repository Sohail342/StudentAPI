from django.db import models

# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length=120)
    nationality = models.CharField(max_length=120)
    city = models.CharField(max_length=120, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    student_age = models.CharField(max_length=10, null=True, blank=True)
    cgp = models.DecimalField(max_digits=1, decimal_places=3)
