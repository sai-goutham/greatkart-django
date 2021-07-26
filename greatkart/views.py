from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.template import RequestContext
def home(request):
    products=Product.objects.all().filter(is_available=True)
    context={'products':products}
    return render(request,'home.html',context)
