from django.db import models

# Create your models here.
class SampleSchool(models.Model):
    school_name = models.CharField(max_length=20)
    school_population = models.IntegerField()

    def __str__(self):
        return f'{self.school_name}- {self.school_population}'