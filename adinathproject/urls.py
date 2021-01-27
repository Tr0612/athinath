"""adinathproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404,handler500
from  django.conf.urls.static import static
from django.conf import settings
from mainapp.views import home,addtobase,detail,product_page
from mainapp import views

urlpatterns = [
    path('adminforadinathenterprise/', admin.site.urls),
    path('',home,name='home'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('addtodatabase/',addtobase,name="addtodatabase"),
    path('detail/<int:id>',detail,name="detail"),
    path('product/<str:category>/',product_page,name='products'),
    path('search/',views.search,name='search'),
    path('invite',views.handle_invitaion,name='invite'),
    path('re/',views.refresh_cart,name='refresh')
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler404='mainapp.views._404_page'
handler500='mainapp.views._500_page'