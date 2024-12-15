from django.db import models


class Student(models.Model):
    student_name = models.CharField(max_length=120)
    nationality = models.CharField(max_length=120)
    city = models.CharField(max_length=120, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    student_age = models.IntegerField(null=True, blank=True)
    cgp = models.DecimalField(max_digits=3, decimal_places=1)
    
    def __str__(self):
        return f'{self.student_name} from {self.nationality}'
