from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Product (models.Model):
    title = models.CharField(max_length=50)
    image = RichTextUploadingField()
    pic = RichTextUploadingField()
    description = models.CharField(max_length=50, null=True)
    price = models.FloatField()

    def __str__(self):
        return self.title
    
class Customer (models.Model):
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    username = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=SEXO, blank=False, null=False)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username
    
class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)