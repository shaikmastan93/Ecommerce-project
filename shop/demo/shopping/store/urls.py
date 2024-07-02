from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('', views.home,name='homepage'),
    path('signup',views.Signup.as_view(),name='signup'),
    path('login',views.Login.as_view(),name='login'),
    path('product-detail/<int:pk>',views.productdetail,name='product-detail'),
    path('logout',views.Logout,name='logout'),
    path('add_to_cart',views.add_to_cart,name='cart_to_cart'),
    path('show_cart',views.show_cart,name='show_cart'),
]