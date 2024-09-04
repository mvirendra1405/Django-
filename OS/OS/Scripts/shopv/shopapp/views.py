from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from .models import Product,Cart
from django.contrib.auth.models import User
from django.views.generic import DeleteView
from django.shortcuts import get_object_or_404



# Create your views here.

def home(request):
    return render(request,'home.html')

def add_user(request):
    if request.method=='POST':
        f=UserCreationForm(request.POST)
        f.save()
        return redirect('/')

    else:
        f=UserCreationForm
        context={'form':f}
        return render(request,'adduser.html',context)
    

def login_view(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        passw=request.POST.get('password')
        user=authenticate(request,username=uname,password=passw)

        if user is not None:
            request.session['uid']=user.id
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
    

def logout_view(request):
    logout(request)
    return redirect('/')

def product_list(request):
    pl=Product.objects.all()
    context={'pl':pl}
    return render(request,'productlist.html',context)

# def cart_list(request):
#     uid=request.session.get('uid')
#     cl=Cart.objects.filter(user_id=uid)
#     context={'cl':cl}
#     return render(request,'cartlist.html',context)

def cart_list(request):
    uid = request.session.get('uid')
    if uid is None:
        return redirect('login')  # Replace with your actual login view name
    cl = Cart.objects.filter(user_id=uid)
    context = {'cl': cl}
    return render(request, 'cartlist.html', context)

# def add_to_cart(request,pid):
#     product_id=Product.objects.get(id=pid)
#     uid=request.session.get('uid')
#     user_id=User.objects.get(id=uid)
#     c=Cart()
#     c.product=product_id
#     c.user=user_id
#     c.save()
#     return redirect('/productlist')

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # Logic to add product to the cart
    cart_item, created = Cart.objects.get_or_create(product=product, user=request.user)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('shopapp:cart_list')

def search(request):
    srch=request.POST.get('srch')
    pl=Product.objects.filter(p_name__contains=srch)
    context={'pl':pl} 
    return render(request,"productlist.html",context)

class delete_cart(DeleteView):
    template_name='delete.html'
    model=Cart
    success_url=('/cartlist')

def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_bill = 0
    
    for item in cart_items:
        item.sub_total = item.product.p_price * item.quantity  # Corrected attribute access
        total_bill += item.sub_total
    
    context = {
        'cl': cart_items,
        'total_bill': total_bill,
    }
    return render(request, 'cart.html', context)


def update_cart(request, item_id, action):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    
    if action == 'increase':
        cart_item.quantity += 1
        cart_item.save()
    elif action == 'decrease':
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    
    return redirect('/cartlist')

def footer(request):
    return render(request,'footer.html')


