from django.db import models

class ProfileInfo(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    picture = models.CharField(max_length = 50)
    description = models.CharField(max_length = 500)
    github = models.CharField(max_length=250)
    linkedin = models.CharField(max_length=250)

    def __str__(self):
        return self.first_name + ' ' + self.last_name 