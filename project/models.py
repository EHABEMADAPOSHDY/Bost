from django.db import models

# Create your models here.
class Blog(models.Model):
   titel = models.CharField(max_length=50)
   article = models.CharField(max_length=200)
   image = models.ImageField(upload_to= 'photos' , null=True , blank=True)
   def __str__(self):
      return self.titel