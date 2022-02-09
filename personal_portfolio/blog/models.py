from pickle import FALSE
from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    date=models.DateField(null=FALSE)


    def __str__(self):
        return self.title