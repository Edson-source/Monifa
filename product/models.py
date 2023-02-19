from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Product (models.Model):
    title = models.CharField(max_length=50)
    image = RichTextUploadingField()
    price = models.FloatField()

    def __str__(self):
        return self.title