from django.db import models

# Create your models here.

class Bank(models.Model):
    NAME=models.CharField(max_length=100)

    def __str__(self):
        return self.NAME
    
class Branch(models.Model):
    NAME=models.ForeignKey(Bank,on_delete=models.CASCADE)
    IFSC=models.CharField(max_length=100)
    BRANCH=models.CharField(max_length=100)
    ADDRESS=models.TextField()
    CONTACT=models.IntegerField()
    CITY=models.CharField(max_length=100)
    DISTRICT=models.CharField(max_length=100)
    STATE=models.CharField(max_length=100)
  
    def __str__(self):
        return self.BRANCH
