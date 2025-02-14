from django.shortcuts import render,redirect
from .models import OrderItem,PastOrder,TableBooking
from django.utils.dateparse import parse_datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json
# Create your views here.

def index(request):
    return render(request, 'index.html')


def cart_view(request):
    if request.user.is_authenticated:
        
        return render(request, 'cart.html')
    else:
        return redirect('login')

def empty(request):
    return render(request, 'empty.html')

def payment(request):
    return render(request, 'payment.html')

def thank(request):
    return render(request, 'thankyou.html')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use auth_login to avoid confusion
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')  # Redirect to 'home' on successful login
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    
def user_logout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Account has been created successfully!')
            form=UserCreationForm()
    else:
        form = UserCreationForm()
    return render(request, 'signup.html',{'form':form})

def booking(request):
    data=TableBooking.objects.filter(user=request.user)
    if request.method == 'POST':
      
        mobile_number=request.POST.get('mobile_number')
        booking_date = request.POST.get('booking_date')
        booking_time = request.POST.get('booking_time')
        number_of_people = request.POST.get('number_of_people')
        user = request.user 
        booking = TableBooking.objects.create(
            user=user,
            mobile_number=mobile_number,
            booking_date=booking_date,
            booking_time=booking_time,
            number_of_people=number_of_people
        )
        booking.save()
        

        # return redirect('book1')
    return render(request, 'tablebook.html',{'data':data})

# def book1(request):
#     return render(request, 'book.html')

def order(request):
    past_orders = PastOrder.objects.filter(user=request.user)

    for order in past_orders:
        # Retrieve related OrderItems for each PastOrder
        order.order_items = order.orderitem_set.all()
    return render(request, 'order.html', {'past_orders': past_orders})

# @api_view(['GET'])
# def order(request):
#     past_orders = PastOrder.objects.all()
#     serializer = PastOrderSerializer(past_orders, many=True)
#     return Response(serializer.data)

@csrf_exempt
@login_required
def save_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            order_time = parse_datetime(data['order_time']) 
            # print("Received data:", data)
            user = request.user
            order = PastOrder.objects.create(
                user=user,
                order_id=data['order_id'],
                order_placed_at=order_time,
                mobile_number=data['mobile_number'],
                address=data['address'],
                total_payment=data['total_payment'],
                payment_id=data['payment_id']
            )
            items_ordered = data.get('items_ordered', [])  # Retrieve items from data
            for item_data in items_ordered:
                OrderItem.objects.create(
                    order=order,
                    item_name=item_data['name'],
                    quantity=item_data['quantity']
                )
            print("Order saved successfully!")
            return JsonResponse({'message': 'Order saved successfully!'})
        except Exception as e:
            print("Error saving order:", e)
            return JsonResponse({'error': 'Internal Server Error'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    

def rate_us(request):
    return render(request, 'RateUs.html')

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import PastOrder
from .serializers import PastOrderSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_orders(request):
    orders = PastOrder.objects.filter(user=request.user)  # Fetch only user's orders
    serializer = PastOrderSerializer(orders, many=True)
    return Response(serializer.data)