from rest_framework import serializers
from .models import PastOrder, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['item_name', 'quantity']

class PastOrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True,source='orderitem_set')

    class Meta:
        model = PastOrder
        fields = ['id','order_id', 'order_placed_at', 'mobile_number', 'address', 'total_payment', 'payment_id', 'order_items']
