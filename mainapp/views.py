from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import OrderForm,InvitaitonForm
from xhtml2pdf import pisa
# Create your views here.
from .models import Product,Order,Category,Carousel,HomeCategories,Invitations,Gifts,Tresures,Personalized
from .cart import Cart
import string
import random
import uuid
from django.contrib.postgres.search import SearchQuery,SearchVector,SearchRank
from django.core.cache import cache
 

def generate_unique_code():
    #length = 6

    while True:
        code = str(uuid.uuid1())
        code=code[:7]
        if Order.objects.filter(code=code).count() == 0:
            break

    return code
def refresh_cart(request):
    '''print("this from the function",request.session.get('cart'))
    if request.session.get('cart'):
        print(request.session.get('cart'))
        x=list(request.session.get('cart').keys())
        y=list(request.session.get('cart').values())
        print("Y:",y)
        print(x)
        for i in range(len(x)):
            print("i:",i)
            try:
                p=Product.objects.get(id=int(x[i]))
            except:
                del request.session.get('cart')[x[i]]
                print("the item is deleted:",request.session.get('cart'))]]]'''
    
    c=Cart(request)
    c.refreshcart()
    print(request.session.get('cart'))
    
    return redirect('cart_detail')

def home(request,done=None):
    cat=HomeCategories.objects.all()
    gift=Gifts.objects.all()
    coursel=Carousel.objects.get(id_image=1)
    coursel_2=Carousel.objects.get(id_image=2)
    coursel_3=Carousel.objects.get(id_image=3)
    coursel_4=Carousel.objects.get(id_image=4)
    tresures=Tresures.objects.all()
    personals=Personalized.objects.all()
    invite=InvitaitonForm()
    if request.method=='POST':
        name=request.POST.get('name')
        number=request.POST.get('number')
        email=request.POST.get('email')
        if len(number)<=10:
            invitation=Invitations(Name=name,Number=number,Email=email)
            invitation.save()
            return render(request,'index.html',context={'coursel':coursel,'coursel_2':coursel_2,'coursel_3':coursel_3,'coursel_4':coursel_4,'cat':cat,'invite':invite,'gift':gift,'invalid_credentials':"Your invitation has been recieved! You will soon be contacted by our sales executives...Have a nice day..",'personalized':personals,"tresures":tresures})

        else:
            return render(request,'index.html',context={'coursel':coursel,'coursel_2':coursel_2,'coursel_3':coursel_3,'coursel_4':coursel_4,'cat':cat,'invite':invite,'gift':gift,'invalid_credentials':"Invalid credentials try again!",'personalized':personals,"tresures":tresures})
    
    return render(request,'index.html',context={'coursel':coursel,'coursel_2':coursel_2,'coursel_3':coursel_3,'coursel_4':coursel_4,'cat':cat,'invite':invite,'gift':gift,'personalized':personals,"tresures":tresures})

def _404_page(request,exception):
    return render(request,'page_404.html')

def _500_page(request):
    return render(request,template_name='page_500.html')


def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")



def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")



def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")



def item_decrement(request, id):
    if request.is_ajax():
        cart = Cart(request)
        product = Product.objects.get(id=id)
        cart.decrement(product=product)
        return redirect("cart_detail")



def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


def cart_detail(request,message=None):
    '''print(request.POST)
    print(request.session.get('cart'))'''
    print(request.session.get('cart'))
    c=Cart(request)
    c.refreshcart()
    if request.method=='POST':
        if request.session.get('cart'):
            x=list(request.session.get('cart').keys())
            y=list(request.session.get('cart').values())
            print("Y:",y)
            print(x)
            if len(request.POST['number'])==10:
                for i in range(len(x)):
                    print("i:",i)
                    p=Product.objects.get(id=int(x[i]))
                    quantity=y[i]
                    o=Order(code=generate_unique_code(),product=p,product_quantity=quantity['quantity'],customer_name=request.POST['firstname'],customer_email=request.POST['email'],customer_number=request.POST['number'],customer_address=request.POST['address'],order_completed=False)
                    o.save()
                cart=Cart(request)
                cart.clear()
                return render(request,'cart.html',context={"success":'Congradulations..!your order has been placed.....'})
            else:
                return render(request, 'cart.html',context={'invalid_credentials':'OOps!..invalid credentials..Try again...'})
    return render(request, 'cart.html')
    



def addtobase(request):
    c=Cart(request) 
    c.refreshcart()
    if request.method=='POST':
        if request.session.get('cart'):
            x=list(request.session.get('cart').keys())
            y=list(request.session.get('cart').values())
            print("Y:",y)
            print(x)
            if len(request.POST['number'])==10:
                for i in range(len(x)):
                    print("i:",i)
                    p=Product.objects.get(id=int(x[i]))
                    quantity=y[i]
                    o=Order(code=generate_unique_code(),product=p,product_quantity=quantity['quantity'],customer_name=request.POST['firstname'],customer_email=request.POST['email'],customer_number=request.POST['number'],customer_address=request.POST['address'],order_completed=False)
                    o.save()
                return cart_clear(request)
            else:
                return render



def detail(request,id):
    product=Product.objects.get(id=id)
    print(product.product_customization)
    return render(request,'detail.html',context={'product':product})


def product_page(request,category):
    try:
        items=Product.objects.filter(product_category=Category.objects.get(category_name=category))
    except:
        items=Product.objects.filter(product_sub_category__contains=category)
    return render(request,'products.html',{'items':items})
    

def search(request):
    if request.method=='GET':
        keyword=request.GET['search']
        categories=Category.objects.annotate(search=SearchVector('category_name'),).filter(search=SearchQuery(keyword))
        print(categories)
        if len(categories)<1:
            items=Product.objects.annotate(search=SearchVector('product_code','product_name','product_description','product_sub_category'),).filter(search=SearchQuery(keyword))
            if len(items)>0:
                print(items)
                return render(request,'products.html',{'items':items})
            else:
                items=Product.objects.all()
                return render(request,'products.html',{'items':items,'notfound':'Oops! We couldn\'t process your request.  See our other products!'})
        else:
            
            for i in categories:
                items=Product.objects.filter(product_category=i)
            return render(request,'products.html',{'items':items})

def handle_invitaion(request):
    if request.method=='POST':  
        name=request.POST.get('name')
        number=request.POST.get('number')
        email=request.POST.get('email')
        invitation=Invitations(Name=name,Number=number,Email=email)
        invitation.save()
        return home(request)


        

