"""
URL configuration for FoodDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from food import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/empty/', views.empty, name='empty'),
    path('cart/payment', views.payment, name='payment'),
    path('cart/thankyou', views.thank, name='thankyou'),
    path('save_order/', views.save_order, name='save_order'),
    path('order/',views.order,name='order'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('booking/',views.booking,name='booking'),
    # path('book1/',views.book1,name='book1')
    path('rateus/',views.rate_us)
]
