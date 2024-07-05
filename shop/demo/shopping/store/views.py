from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import Product, Category, Customer,Cart
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.

def home(request):
    products =None
    totalitem = 0
    if request.session.has_key("phone"):
        phone = request.session['phone']
        category = Category.get_all_categories()
        customer = Customer.objects.filter(phone=phone)
        totalitem=len(Cart.objects.filter(phone=phone))
        for c in customer:
            name = c.name
            categoryID = request.GET.get('category')
            if categoryID:
              products = Product.get_all_product_by_category_id(categoryID)
        

            else:
                products = Product.get_all_products()
               
    


                data = {}
                data ['name'] = name
                data['product'] = products
                data['category'] = category
                data['totalitem'] = totalitem
                print('You are',request.session.get('phone'))
                return render(request,'home.html',data)
    else:
        return redirect('login')


        
class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        phone = request.POST.get('phone')
        error_message = None
        value = {'phone': phone}
        
        customer = Customer.objects.filter(phone=phone).first()

        if customer:
            request.session['phone']=phone
            return redirect('homepage')
        else:
            error_message = "Mobile number is invalid"
            data = {'error': error_message, 'value': value}
        
        return render(request, 'login.html', data)
    
class Signup(View):
    def get(self,request):
        return render(request, 'signup.html')
    
    def post(self,request):
        postData = request.POST
        name = postData.get("name")
        phone = postData.get("phone")
        
        error_message = None
        value = {'phone': phone, 'name': name}
        
        customer = Customer(name=name, phone=phone)
        if not name:
            error_message = "Name is required"
        elif not phone:
            error_message = "Mobile number is required"
        elif len(phone) < 10:
            error_message = "Mobile number is not valid"
        elif customer.isExists():
            error_message = "Mobile number already exists"
        
        if not error_message:
            messages.success(request, "Registered successfully")
            customer.register()
            return redirect('signup')
        else:
            data = {'error': error_message, 'value': value}
            return render(request, "signup.html", data)
        
        
def productdetail(request,pk):
    totalitem = 0
    product = Product.objects.get(pk=pk)
    item_already_in_cart = False
    if request.session.has_key('phone'):
        phone = request.session['phone']
        totalitem=len(Cart.objects.filter(phone=phone))
        item_already_in_cart =Cart.objects.filter(Q(product=product.id) & Q(phone=phone)).exists()
        customer = Customer.objects.filter(phone=phone)
        for c in customer:
            name = c.name
        data = {'product':product,'item_already_in_cart': item_already_in_cart,'name':name,'totalitem':totalitem}
        return render(request,'productdetail.html',data)

def Logout(request):
    if 'phone' in request.session:
        del request.session['phone']
    return redirect('login')


def add_to_cart(request):
    phone = request.session['phone']
    product_id = request.GET.get('prod_id')
    product_name = Product.objects.get(id=product_id)
    product = Product.objects.filter(id=product_id)
    for p in product:
        image=p.image
        price=p.price
        Cart(phone=phone,product=product_name,image=image,price=price).save()
        return redirect(f"/product-detail/{product_id}")
    



def show_cart(request):
    totalitem=0
    if request.session.has_key('phone'):
        phone = request.session["phone"]
        totalitem = len(Cart.objects.filter(phone=phone))
        customer = Customer.objects.filter(phone=phone)
        for c in customer:
            name = c.name
            cart=Cart.objects.filter(phone=phone)
            data = {'name':name,'totalitem':totalitem,'cart':cart}
            if cart:
                return render(request,'show_cart.html',data)
            else:
                pass

def plus_cart(request):
    if request.session.has_key('phone'):
        phone = request.session["phone"]
        product_id = request.GET['prod_id']
        cart = Cart.objects.get(Q(product=product_id) & Q(phone=phone))
        cart.quantity += 1
        cart.save()
        data = {'quantity': cart.quantity}  # Corrected reference to cart.quantity
        return JsonResponse(data)
    
def minus_cart(request):
    if request.session.has_key('phone'):
        phone = request.session["phone"]
        product_id = request.GET['prod_id']
        cart = Cart.objects.get(Q(product=product_id) & Q(phone=phone))
        cart.quantity -= 1
        cart.save()
        data = {'quantity': cart.quantity}  # Corrected reference to cart.quantity
        return JsonResponse(data)
    
def remove_cart(request):
    if request.session.has_key('phone'):
        phone = request.session["phone"]
        product_id = request.GET['prod_id']
        cart = Cart.objects.get(Q(product=product_id) & Q(phone=phone))
       
        cart.delete()
        
        return JsonResponse()




   
   
   
    

        