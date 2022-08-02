from django.db import models

# 建立資料表
class Shelter(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    def ___str__(self):
        return self.name
