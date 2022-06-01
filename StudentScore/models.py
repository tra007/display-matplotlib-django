from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    score = models.PositiveIntegerField(validators=[MaxValueValidator(20), MinValueValidator(0)])

    def __str__(self) -> str:
        return self.name
