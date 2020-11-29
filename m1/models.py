from django.db import models
from datetime import datetime

# Create your models here.

class model_1(models.Model):

    name=models.CharField(max_length=50,default="")
    x=models.DecimalField(max_digits=100,decimal_places=2,default=40.99)
    t=models.FileField(upload_to='covers/',default="")
    img=models.ImageField(upload_to='covers/',default="")
    def __str__(self):
        return "{},{},{}".format(self.name,self.x,self.t)
