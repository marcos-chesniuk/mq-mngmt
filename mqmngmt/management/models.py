from django.db import models

# Create your models here.
class Consultant(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mail = models.EmailField()


class Query(models.Model):
    text = models.TextField()
    date = models.DateField(auto_now_add=True)


class Response(models.Model):
    text = models.TextField()
    date = models.DateField(auto_now_add=True)


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mail = models.EmailField()


class Course(models.Model):
    name = models.CharField(max_length=200)


class Bill(models.Model):
    ammount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    dues_qt = models.IntegerField(default=1)
    dues_amm = models.DecimalField(max_digits=10, decimal_places=2)