from django.urls import path, include
from . import views 

from product.views import ProductViewSet, CustomerViewSet, PurchaseViewSet, ListaCustomerProduct
from rest_framework import routers


router = routers.DefaultRouter()
router.register('produtos', ProductViewSet, basename='produtos')
router.register('customers', CustomerViewSet, basename='customers')
router.register('purchase', PurchaseViewSet, basename='purchase')

urlpatterns = [
    path('', include(router.urls)),
    path('product/', views.product),
    path('detail/<int:pk>/', views.detail),
    path('tag_hunting/', views.tag_hunting),
    path('purchase/<int:pk>/', ListaCustomerProduct.as_view()),
]
