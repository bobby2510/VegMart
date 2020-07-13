from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Staff)
admin.site.register(ShopOwner)
admin.site.register(DelivaryBoy)
admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(BaseAddress)
admin.site.register(Customer_Address)
admin.site.register(OrderShipping)