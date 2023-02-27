from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from product.serializer import ProductSerializer, CustomerSerializer, ListaCustomerProductSerializer
from .models import Product, Customer, Purchase

# Create your views here.
def product(request):
    products = {}
    products['db'] = Product.objects.all()
    return render(request, 'product.html', products)

def detail(request, pk):
    products = {}
    products['db'] = Product.objects.get(pk=pk)
    return render(request, 'detail.html', products)

class ProductViewSet(viewsets.ModelViewSet):
    """EXIBINDO TODOS OS PRODUTOS"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CustomerViewSet(viewsets.ModelViewSet):
    """EXIBINDO TODOS OS PRODUTOS"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class PurchaseViewSet(viewsets.ModelViewSet):
    """EXIBINDO AS MATRICULAS DE ALUNO"""
    queryset = Purchase.objects.all()
    serializer_class = ListaCustomerProductSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaCustomerProduct(generics.ListAPIView):
    """EXIBINDO AS MATRICULAS DE ALUNO"""
    def get_queryset(self):
        queryset = Purchase.objects.filter(product_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaCustomerProductSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]