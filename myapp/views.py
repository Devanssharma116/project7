from django.shortcuts import render

# Create your views here.
from .models import Product
def product_list(request):
    products=Product.objects.all()
    return render(request,'product_list.html',{'products':products})

def product_detail(request,product_id):
    product=Product.objects.get(pk=product_id)
    return render(request,'product_detail.html',{'product':product})