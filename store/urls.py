from django.urls import path
from store import views
app_name='store'
urlpatterns=[
    path('',views.home,name='home'),
    path('cart/',views.CartView,name='cart'),
    path('about/',views.about,name='about'),
    path('contact_us/',views.contact_us,name='contact-us'),
    path('checkout/',views.checkout,name='checkout'),
    path('order_shipping/<id>/delivered/',views.order_delivered_view,name='order-delivered'),
    path('store/customer_orders/<customer>/',views.customer_orders_view,name='customer-orders'),
    path('store/order_detail/<customer>/order/<order_id>/order_invoice/<id>/',views.order_detail_view,name='order-detail'),
    path('store/<slug_store>/rating/',views.RatingView,name='rating'),
    path('store/<slug_store>/',views.ShopDetail,name='shop-detail'),
    path('store/<slug_store>/<slug_product>/add_to_cart/',views.add_to_cart,name='add-to-cart'),
    path('store/<slug_store>/<slug_product>/remove_from_cart/',views.remove_from_cart,name='remove-from-cart'),
    path('store/<slug_store>/<slug_product>/fresh-cart/',views.fresh_cart,name='fresh-cart'),
    path('store/<slug_store>/<slug_product>/decrease-order-item/',views.decrease_order_item_quantity,name='decrease'),
    path('store/<slug_store>/<slug_product>/increase-order-item/',views.increase_order_item_quantity,name='increase'),
    path('search/',views.search,name='search'),
]