from django.db import models


class store_data(models.Model):
    topic=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    content=models.CharField(max_length=500)
    imageurl=models.ImageField(blank=True,null=True)


    def __str__(self):
        return self.name
# Create your models here.
