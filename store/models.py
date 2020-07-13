from django.db import models
from django.shortcuts import reverse
from django.core.validators import RegexValidator
from accounts.models import User
from django.db.models import Q
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    
    @property
    def get_absolute_orders_url(self):
        return reverse('store:customer-orders',kwargs={
            'customer':self.user.username,
        })
    @property
    def get_cart_count(self):
        qs=self.order.filter(is_completed=False)
        if qs.exists() and qs.count()==1:
            return qs.first().order_item.count()
        else:
            return 0
    @property
    def get_live_order_products(self):
        print('hi hello')
        order_qs=Order.objects.filter(customer=self,is_completed=False)
        if order_qs.exists() and order_qs.count() == 1:
            order=order_qs.first()
            result=[]
            for order_item in order.order_item.all():
                result.append(order_item.product)
            print(result)
            return result
        return []
    @property
    def have_atleast_one_address(self):
        if self.address.count() == 0:
            return False
        return True
    @property
    def get_address_list(self):
        return self.address.all()

class Staff(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    staff_id=models.AutoField(primary_key=True)
    address=models.OneToOneField('BaseAddress',on_delete=models.SET_NULL,null=True,blank=True,unique=True)
    def __str__(self):
        return self.user.username
            
class ShopOwner(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    shop=models.OneToOneField('Shop',on_delete=models.CASCADE)
    address=models.OneToOneField('BaseAddress',on_delete=models.SET_NULL,null=True,blank=True,unique=True)
    
    def __str__(self):
        return self.user.username

    @property
    def get_previous_order_url(self):
        return reverse('business:shop-previous-order',kwargs={'id':self.shop.id,})
    @property
    def get_my_products_url(self):
        return reverse('business:shop-products',kwargs={'id':self.shop.id})
    @property
    def get_discount_url(self):
        return reverse('business:change-discount',kwargs={'id':self.shop.id,})


class DelivaryBoy(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    is_available=models.BooleanField(default=True)
    address=models.OneToOneField('BaseAddress',on_delete=models.SET_NULL,null=True,blank=True,unique=True)
    image=models.ImageField(upload_to='delivaryboy_images')

    def __str__(self):
        return self.user.username
    
    @property
    def get_active_orders(self):
        return self.shipped_order.filter(is_delivered=False).count()
    @property
    def get_profile_url(self):
        return reverse('business:delivery-boy-profile',kwargs={'id':self.id,})

    @property
    def get_delivered_orders(self):
        return self.shipped_order.filter(is_delivered=True).count()
    @property
    def get_previous_order_url(self):
        return reverse('business:previous-order',kwargs={'id':self.id,})

    @property
    def get_total_orders(self):
        return self.shipped_order.all().count()
    
    @property
    def get_not_available_url(self):
        return reverse('business:delivery-boy-not-available',kwargs={'id':self.id,})
    @property
    def get_available_url(self):
        return reverse('business:delivery-boy-available',kwargs={'id':self.id,})
    @property
    def is_active(self):
        return self.is_available

class Shop(models.Model):
    name=models.CharField(max_length=100,unique=True)
    image=models.ImageField(upload_to='shop_images')
    address=models.OneToOneField('BaseAddress',on_delete=models.SET_NULL,null=True,blank=True,unique=True)
    slug_store=models.SlugField(default='empty')
    sponsored=models.BooleanField(default=False)
    description=models.CharField(max_length=1024,null=True,blank=True)
    minimum_amount=models.IntegerField(default=0)
    limit_of_discount=models.IntegerField(default=0)
    discount=models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        temp_name_list=list(self.name.split(' '))
        self.slug_store='-'.join(temp_name_list)
        super(Shop,self).save(*args,**kwargs)
    @property
    def shop_rating_count(self):
        return self.rating.count()
    @property
    def shop_rating(self):
        rate=0
        qs=self.rating.all()
        for obj in qs:
            rate+=obj.rate
        if self.shop_rating_count ==0:
            return 0
        return rate/self.shop_rating_count
    @property
    def get_absolute_url(self,*args,**kwargs):
        return reverse('store:shop-detail',kwargs={'slug_store':self.slug_store})
    
    @property
    def get_products(self):
        return self.product.all()
    
    @property
    def get_products_count(self):
        return self.product.count()
    
    @property
    def get_active_orders(self):
        return OrderShipping.objects.filter(Q(order__shop=self) & 
        Q(is_delivered=False)).count()
    
    @property
    def get_delivered_orders(self):
        return OrderShipping.objects.filter(Q(order__shop=self) &
        Q(is_delivered=True)).count()
    @property
    def get_total_orders(self):
        return OrderShipping.objects.filter(order__shop=self).count()


class Product(models.Model):
    shop=models.ForeignKey(Shop,on_delete=models.CASCADE,related_name='product')
    name=models.CharField(max_length=110)
    price=models.IntegerField(default=0)
    slug_product=models.SlugField(default='empty')
    category=models.ForeignKey('Category', null=True,on_delete=models.SET_NULL)
    image=models.ImageField(upload_to='product_images',null=True)
    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        slug_string=self.shop.name+' '+self.name
        self.slug_product='-'.join(list(slug_string.split(' ')))
        super(Product,self).save(*args,**kwargs)
    @property
    def get_absolute_url(self,*args,**kwargs):
        return reverse('store:add-to-cart',kwargs={'slug_store':self.shop.slug_store,'slug_product':self.slug_product,})
    @property
    def get_absolute_remove_from_cart_url(self,*args,**kwargs):
        return reverse('store:remove-from-cart',kwargs={'slug_store':self.shop.slug_store,'slug_product':self.slug_product,})
    @property
    def get_absolute_fresh_cart_url(self,*args,**kwargs):
        return reverse('store:fresh-cart',kwargs={'slug_store':self.shop.slug_store,'slug_product':self.slug_product,})
    @property
    def get_absolute_decreament_order_item_url(self,*args,**kwargs):
        return reverse('store:decrease',kwargs={'slug_store':self.shop.slug_store,'slug_product':self.slug_product,})
    @property
    def get_absolute_increase_order_item_url(self,*args,**kwargs):
        return reverse('store:increase',kwargs={'slug_store':self.shop.slug_store,'slug_product':self.slug_product,})
    @property
    def get_product_edit_url(self):
        return reverse('business:shop-product-detail',kwargs={'id':self.id,}) 

class Order(models.Model):
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL,related_name='order')
    shop=models.ForeignKey(Shop,null=True,blank=True,on_delete=models.SET_NULL,related_name='order')
    is_completed=models.BooleanField(default=False)
    date_added=models.DateTimeField(auto_now_add=True)
    shop_discount=models.IntegerField(default=0)
    shop_limit_of_discount=models.IntegerField(default=0)
    shop_minimum_amount=models.IntegerField(default=0)

    def __str__(self):
        return self.customer.user.username+', date: '+str(self.date_added.day)+'-'+str(self.date_added.month)+'-'+str(self.date_added.year)
    
    def save(self,*args,**kwargs):
        self.shop_discount=self.shop.discount
        self.shop_limit_of_discount=self.shop.limit_of_discount
        self.shop_minimum_amount=self.shop.minimum_amount
        return super(Order,self).save(*args,**kwargs)


    @property
    def get_order_actual_amount(self):
        sum=0
        for order_item in self.order_item.all():
            sum+=order_item.get_order_item_amount
        return sum

    @property
    def get_discounted_amount(self):
        if self.order_item.count()>0:
            shop=self.order_item.first().product.shop
            amount=self.get_order_actual_amount
            discount_amount=(amount*self.shop_discount)/100
            if amount<self.shop_minimum_amount:
                return 0
            if discount_amount>self.shop_limit_of_discount:
                return self.shop_limit_of_discount
            return discount_amount
        else:
            return 0
    
    @property
    def get_final_amount(self):
        return self.get_order_actual_amount-self.get_discounted_amount+10

class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_item')
    quantity=models.IntegerField(default=1)
    product_price=models.IntegerField(default=0)

    def save(self,*args,**kwargs):
        self.product_price=self.product.price
        return super(OrderItem,self).save(*args,**kwargs)


    def __str__(self):
        return self.product.name+' - '+str(self.quantity)
    
    @property
    def get_order_item_amount(self):
        return self.product_price*self.quantity

class Category(models.Model):
    name=models.CharField(max_length=110,unique=True)
    def __str__(self):
        return self.name

class Rating(models.Model):
    shop=models.ForeignKey(Shop,on_delete=models.CASCADE,related_name='rating')
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='rating')
    rate=models.IntegerField(default=0)

    def __str__(self):
        return self.customer.user.username+' on '+self.shop.name

COUNTRY_CHOICES=(('IND','India'),)
STATE_CHOICES=(('AP','Andhra Predesh'),
            ('TS','Telangana'),
)

class BaseAddress(models.Model):
    country=models.CharField(max_length=4,choices=COUNTRY_CHOICES)
    state=models.CharField(max_length=4,choices=STATE_CHOICES)
    address_line=models.TextField(unique=True)
    city=models.CharField(max_length=30)
    landmark=models.CharField(max_length=30)

    def __str__(self):
        return self.address_line
    @property
    def get_address(self):
        return f'{self.address_line},{self.landmark},{self.city},{self.get_state_display()},{self.get_country_display()}.'
class Customer_Address(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='address')
    country=models.CharField(max_length=4,choices=COUNTRY_CHOICES)
    state=models.CharField(max_length=4,choices=STATE_CHOICES)
    address_line=models.TextField(unique=True)
    city=models.CharField(max_length=30)
    landmark=models.CharField(max_length=30)
    zipcode=models.CharField(max_length=10)

    def __str__(self):
        return self.customer.user.username+' - '+str(self.id)
    @property
    def get_address(self):
        return f'{self.address_line},{self.landmark},{self.city},zipcode : {self.zipcode},{self.get_state_display()},{self.get_country_display()}.'
        
class OrderShipping(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='shipped_order')
    order=models.OneToOneField(Order,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=30)
    phone_number=models.CharField(max_length=10)
    delivery_boy=models.ForeignKey(DelivaryBoy,on_delete=models.SET_NULL,null=True,blank=True,related_name='shipped_order')
    address=models.ForeignKey(Customer_Address,on_delete=models.SET_NULL,null=True,blank=True,related_name='shipped_order')
    date_shipped=models.DateTimeField(auto_now_add=True)
    is_delivered=models.BooleanField(default=False)
    is_canceled=models.BooleanField(default=False)

    def __str__(self):
        return self.customer.user.username+" "+self.order.shop.name

    @property
    def get_absolute_url(self,*args,**kwargs):
        return reverse('store:order-detail',kwargs={
            'customer':self.customer.user.username,
            'order_id':self.order.id,
            'id':self.id,
        })
    @property
    def get_delivered_url(self):
        return reverse('store:order-delivered',kwargs={'id':self.id,})
    