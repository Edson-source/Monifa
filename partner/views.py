from django.shortcuts import render

# Create your views here.
def partner(request):
    return render(request, "partner.html")