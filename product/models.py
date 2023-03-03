from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from sign_up.models import Customer

# Create your models here.
class Product (models.Model):
    title = models.CharField(max_length=50)
    image = RichTextUploadingField()
    pic = RichTextUploadingField()
    description = models.CharField(max_length=50, null=True)
    price = models.FloatField()

    def __str__(self):
        return self.title
    
class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)