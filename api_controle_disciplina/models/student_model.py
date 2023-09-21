from django.db import models

# Create your models here.

class StudentEntity(models.Model):
    name  = models.CharField(blank=False, null=False, max_length=255)
    email = models.CharField(blank=False, null=False, max_length=255)

    def __str__(self) -> str:
        return self.name, self.email