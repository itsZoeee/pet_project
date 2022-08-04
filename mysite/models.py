from django.db import models

# 建立資料表

class Adopt(models.Model):
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    ligation = models.CharField(max_length=50)
    vaccine  = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    pic = models.CharField(max_length=250)
    def ___str__(self):
        return self.breed

class Lost(models.Model):
    name = models.CharField(max_length=50)
    variety = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    body = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    lostdate  = models.DateField()
    area = models.CharField(max_length=50)
    pet_jpg = models.CharField(max_length=250)
    def ___str__(self):
        return self.breed