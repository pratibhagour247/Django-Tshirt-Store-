
from django.contrib import admin
from django.urls import path
from store.views import home,cart,login,oders,signup,logout,show_product

urlpatterns = [
    path('', home, name="homepage"),
    path('cart/',cart),
    path('login/',login),
    path('oders/',oders),
    path('signup/',signup),
    path("logout/",logout),
    path("product/<int:id>", show_product)
      

    
]
