from django.shortcuts import render
from django.http import HttpResponse
from .models.product import *
from .models.category import *

# Create your views here.
def home(request):
    products =None
    category = Category.get_all_categories()

    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_product_by_category_id(categoryID)

    else:
        products = Product.get_all_products()


    data = {}
    data['product'] = products
    data['category'] = category
    return render(request,'home.html',data)

def signup(request):
    return render(request, 'signup.html')
