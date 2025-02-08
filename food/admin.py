from django.contrib import admin
from .models import PastOrder,OrderItem,TableBooking
# Register your models here.
@admin.register(PastOrder)
class PastOrderAdmin(admin.ModelAdmin):
    list_display = ('get_username','order_id', 'order_placed_at', 'mobile_number', 'address', 'total_payment', 'payment_id')
    
    def get_username(self,obj):
        return obj.user.username
    
    get_username.short_description='Username'

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('get_username','order_id', 'item_name', 'quantity')
    
    def get_username(self,obj):
        return obj.order.user.username if obj.order else None
    
    get_username.short_description='Username'

# admin.site.register(PastOrder)
# admin.site.register(OrderItem)

@admin.register(TableBooking)
class TableBookingAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'mobile_number','booking_date','booking_time','number_of_people')

    def get_username(self,obj):
        return obj.user.username
    
    get_username.short_description='Username'
