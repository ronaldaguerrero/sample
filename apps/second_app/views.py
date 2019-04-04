### second app, def functions here ###
from django.shortcuts import render, HttpResponse, redirect
from .models import * 
import bcrypt
from django.contrib import messages

def index(request):
    return render(request, 'second_app/index.html')

def cart(request):
    return render(request, 'second_app/checkout.html')

def shop(request):
    return render(request, 'second_app/shop.html')

def single_product(request):
    return render(request, 'second_app/single-product-details.html')

def contact(request):
    return render(request, 'second_app/contact.html')

def blog(request):
    return render(request, 'second_app/blog.html')

def add(request, my_val):
    size_from_form = (request.POST["size"])
    print("updating size of product...")
    my_size = Product.objects.get(id=my_val).size = 'size_from_form'
    product = Product.objects.get(id=my_val)
    print('size: ' + my_size)
    print('Order is being created...')
    my_order = Order.objects.create()
    new_order = Order.objects.last()
    new_order.products.add(product)
    print('Product was added to order...')
    order = Order.objects.last()
    print('last order:' + str(order))
    order_products = order.products.all()
    print(order_products)
    context = {
    	'all_p': order_products,
    }
    return render(request, 'second_app/checkout.html', context)

def login(request):
    return render(request, 'second_app/login_reg.html')

def register_user(request):
    errors = User.objects.validate_user(request.POST)
    if len(errors) != 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect ('/login') #need to redirect here. it will still keep your error messages information
    else:
        hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        new_user = User.objects.create(first_name=request.POST['fname'], last_name = request.POST['lname'], email=request.POST['email'], password = hash1)
        request.session['user_id']=new_user.id
    print(new_user)
    print(hash1)
    print("="*80)
    return redirect('/address')

def login_user(request):
    print("=+"*80)
    errors = User.objects.validate_login(request.POST)
    users_with_email = User.objects.filter(email=request.POST['email'])
    if len(errors) != 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect ('/login')
    else:
        found_user = users_with_email[0]
        request.session['user_id'] =found_user.id
        return redirect('/address')

def address(request):
    return render(request, 'second_app/address.html')

def success(request):
    current_user = User.objects.get(id=request.session['user_id'])
    context = {
        "curr_user": current_user
    }
    return render(request, 'second_app/address.html', context)

def clear(request):
    request.session.clear()
    return redirect ('/login')