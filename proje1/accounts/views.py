from django.shortcuts import render,redirect,get_object_or_404
from accounts.forms import regForm,PersonProfileForm
from accounts.models import PersonDetail

from products.models import Product
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import razorpay
from proje1.settings import rzp_KEY_ID,rzp_KEY_SECRET
from django.views.decorators.csrf import csrf_exempt


def register(request):
    registered=False
    if request.method=='POST':
        forms=regForm(request.POST)
        if forms.is_valid():
            user=forms.save()
            user.set_password(user.password)
            user.save()
    else:
        forms=regForm()
    return render(request,'register.html',{'forms':forms,'registered':registered})

@login_required(login_url="user_login")
def profile(request):
    user = request.user
    # Retrieve data from the session
    data = request.session.get('cleaned_data')
    return render(request, "profile.html", {'pdata': user, "data": data})

@login_required(login_url="user_login")
def add_profile(request):
    if request.method == "POST":
        form = PersonProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # If form is valid, save cleaned data in session
            data = form.cleaned_data
            request.session['cleaned_data'] = data
            # Redirect to profile page after form submission
            return redirect('profile')
    else:
        form = PersonProfileForm(instance=request.user)
        data = None
    return render(request, "add_profile.html", {"form": form, "data": data})



@login_required(login_url="user_login")
def index(request):
    products = Product.objects.all()
    return render(request,"index.html",{'products':products})

def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get('password')
        
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect("index")
        else:
            return HttpResponse("please check your cred!!!!!")

    return render(request,"user_login.html",{})
@login_required(login_url="user_login")
def user_logout(request):
    logout(request)
    return redirect("user_login")

def details(request,pk):
    products = Product.objects.get(pk=pk)
    productss = Product.objects.get(pk=pk)
    is_liked = False
    if products.likes.filter(id=request.user.id).exists():
        is_liked = True 
    prod_like = is_liked
    
    is_carted = False
    
    if productss.carts.filter(id=request.user.id).exists():
        is_carted = True
    prod_cart = is_carted
    
    return render(request,"details.html",{'products':products,'prod_like':prod_like,"productss":productss,"prod_cart":prod_cart})


def product_liked(request,pk):
    prod_id=request.POST.get('product_id')
    print(prod_id)
    product = get_object_or_404(Product,id=request.POST.get('product_id'))

    print(product)
    if product.likes.filter(id=request.user.id).exists():
        product.likes.remove(request.user)
    else:
        product.likes.add(request.user)
    return redirect('details',pk=pk)


def add_wishlist(request):
    wishlisted = Product.objects.filter(likes=request.user)
    print(wishlisted)
    return render(request,"wishlist.html",{'wishlisted':wishlisted})

def searchproducts(request):
    prod = request.POST.get('item')
    # print(searched_item)
    searched_item = ''
    if request.POST.get('item'):
        searched_item = request.POST.get('item') 
    print(searched_item)
    products = Product.objects.filter(product_name__icontains=searched_item)
    print(products)
    return render(request,"searchproduct.html",{'products':products,"searched_item":searched_item,"prod":prod})   

def add_to_cart(request,pk):
    prod_id = request.POST.get('prod_id')
    print(prod_id)
    product = get_object_or_404(Product,id=request.POST.get('prod_id'))
    print(product)
    if product.carts.filter(id=request.user.id).exists():
        product.carts.remove(request.user)
    else:
        product.carts.add(request.user)
    return redirect('details',pk=pk)

def card(request):
    abc= Product.objects.filter(carts=request.user)
    print(abc)
    d=0
    c=0
    sgst=0
    cgst=0
    total=0
    delivery=0
    for i in abc:
        
        if i.price:
            d+=i.price
            c+=1
    sgst=(d*4)/100
    cgst=(d*4)/100
    total=d+sgst+cgst
    if total<1:
        total=0
    elif total < 500:
        delivery=50
        total+=50
    elif 500<total<1000:
        delivery=30
        total+=30
    elif total>1000:
        delivery=0
        total+=0
    client = razorpay.Client(
            auth=(rzp_KEY_ID,rzp_KEY_SECRET))

    totals=round((total * 100),2)  
    if totals<=0:
        totals=0
    else:
        payment = client.order.create({'amount': totals, 'currency': 'INR','payment_capture': '1'})
    return render(request,'addcart.html',{"abc":abc,"d":d,"c":c,"sgst":sgst,"cgst":cgst,"total":total,"delivery":delivery,'totals':totals})


def remove_cart(request):
    product = get_object_or_404(Product,id=request.POST.get('pro_id'))

    if product.carts.filter(id=request.user.id).exists():
        product.carts.remove(request.user)
    return redirect('cards')

@csrf_exempt
def success(request):
    return render(request,"success.html")


