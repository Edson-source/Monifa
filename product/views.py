from django.shortcuts import render

from .models import Product

# Create your views here.
def product(request):
    products = {}
    products['db'] = Product.objects.all()
    return render(request, 'product.html', products)

def detail(request, pk):
    products = {}
    products['db'] = Product.objects.get(pk=pk)
    return render(request, 'detail.html', products)