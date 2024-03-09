from django.db import models

class Student(models.Model):
    name = models.CharField(null = False,max_length = 100)
    age = models.IntegerField()
    department = models.CharField(null = False,max_length = 100)
    college = models.CharField(null = False,max_length = 100)
    address = models.CharField(null=False,max_length = 100)
    def __str__(self):
        return f"{self.name}"