from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Class(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=50)
    mac = models.CharField(max_length=17, unique=True)
    email = models.EmailField(unique=True)
    class_name = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Record(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    present_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.student} ---> {self.present_time}'