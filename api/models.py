from django.db import models

class students(models.Model):
    id=models.IntegerField(primary_key=True)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    nrc=models.CharField(max_length=50)
    results=models.DecimalField(max_digits=10,decimal_places=3)
