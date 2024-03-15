from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    operating_hours = models.CharField(max_length=255)

    def __str__(self):
        return self.name
