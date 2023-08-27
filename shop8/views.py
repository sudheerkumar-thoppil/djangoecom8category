from django.shortcuts import render , HttpResponse
from .models import Product, Category

def index(request):
# Create your views here.
    # category = Category.objects.get(pk=id)
    category = Category.objects.all()
    products=Product.objects.all()
    data={'category':category,
    'products':products}
    
    return render(request,'index.html',{'data':data},)

def category(request,id):
    return render(request,'base.html')