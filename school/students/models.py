from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField(blank=False)

    def __str__(self):
        return self.name

class Teacher(models.Model):
        name = models.CharField(max_length=20, blank=False)
        phone = models.IntegerField()
        email = models.EmailField(blank=False)
        age = models.IntegerField()

        def __str__(self):
            return self.name
class School(models.Model):
        name = models.CharField(max_length=20, blank=False)
        phone = models.IntegerField()
        email = models.EmailField(blank=False)
        Location = models.CharField(max_length=20, blank=False)

        def __str__(self):
            return self.name
