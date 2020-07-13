from django import template
from store.models import Order,Customer,Product,Shop
register= template.Library()

@register.filter
def order_item_instance(product,user):
    order=Order.objects.filter(customer=user.customer,is_completed=False).first()
    order_item=order.order_item.filter(product=product).first()
    return [order_item,]

@register.filter
def rated(shop,user):
    customer=user.customer
    
