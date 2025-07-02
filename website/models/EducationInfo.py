from django.db import models


class Education(models.Model):
    degree = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    start_date = models.DateField(max_length=50)
    end_date = models.DateField(max_length=50)
    university = models.CharField(max_length=250)

    def __str__(self):
        return self.degree + ' ' + self.university
