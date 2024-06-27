from django.contrib import admin
from  .models import *


class AdminProduct(admin.ModelAdmin):
    list_display = ['id','name','price','category','description']

# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Category)