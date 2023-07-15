from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import login

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')  # Replace 'order_list' with the name of your order list view
    else:
        form = OrderForm()

    return render(request, 'create_order.html', {'form': form})

def home(request):
    return render(request ,'home.html')

def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  # Use auth_login instead of login
                return redirect('home')  # Replace 'home' with the URL name of your home page
            else:
                # Handle invalid credentials
                return render(request, 'login.html', {'form': AuthenticationForm(), 'invalid': True})
    else:
        form = AuthenticationForm()

        return render(request, 'login.html', {'form': form})


def contact(request):
    return render(request ,'contact.html')
def shop(request):
    return render(request ,'shop.html')
def why(request):
    return render(request ,'why.html')
def testmon(request):
    return render(request ,'testimonial.html')