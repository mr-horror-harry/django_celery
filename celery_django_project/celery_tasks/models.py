from django.db import models

class Student_data(models.Model):
    regno = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    marks = models.FloatField()
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.name 