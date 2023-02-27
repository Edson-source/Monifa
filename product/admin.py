from django.contrib import admin
from product.models import Product, Customer, Purchase

# Register your models here.
admin.site.register(Product)

class Customers(admin.ModelAdmin):
    list_display = ('id', 'username', 'age', 'gender', 'email', 'password')
    list_display_links = ('id',)

admin.site.register (Customer, Customers)

class Purchases(admin.ModelAdmin):
    list_display = ('id', 'product', 'customer')
    list_display_links = ('id',)

admin.site.register(Purchase, Purchases)