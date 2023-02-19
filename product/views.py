from django.shortcuts import render

from .models import Product

# Create your views here.
def product(request):
    products = {}
    products['db'] = Product.objects.all()
    return render(request, 'product.html', products)