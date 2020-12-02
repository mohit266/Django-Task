from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=200)
    tags = TaggableManager()
    image = models.ImageField(upload_to='images/')
    