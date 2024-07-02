from django.contrib import admin
from  .models import *
from .models.customer import Customer



class AdminProduct(admin.ModelAdmin):
    list_display = ['id','name','price','category','description']
    
    
class AdminCustomer(admin.ModelAdmin):
    list_display = ['id','name','phone']

class AdminCart(admin.ModelAdmin):
    list_display = ['id','phone','product','image','price']


# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Cart,AdminCart)