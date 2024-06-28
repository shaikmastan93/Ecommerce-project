from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models.product import *
from .models.category import *
from .models.customer import *
from django.contrib import messages

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
    if request.method == 'GET':
        return render(request, 'signup.html')
    
    else:
        postData = request.POST
        name = postData.get("name") 
        phone = postData.get("phone")
        
        error_message = None
        
        customer = Customer(name=name,phone=phone)
        if(not name):
            error_message = "Name is required"
        elif not phone:
            error_message = "Phone num is required"
            
        elif len(phone) < 10:
            error_message = "Phone number is not valid"
        if not error_message:
            messages.success(request,"Register Successfully")
            
            customer.register()
            return redirect('signup')
        else:
            return render(request,"signup.html",{'error':error_message})

    