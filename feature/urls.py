from django.urls import path
from . import views 

urlpatterns = [
    path('feature/', views.feature),
]
