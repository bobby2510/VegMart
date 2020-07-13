from django.urls import path
from .views import (business_home,online_shop_portal,new_delivery_boy,staff_home,new_online_shop_applications,shop_application_detail,new_delivery_boy_applications,delivery_boy_application_detail,
                shop_verified_applications,delivery_boy_verified_applications,shop_accept_view,shop_reject_view,
                delivery_boy_accept_view,delivery_boy_reject_view,verify_shop_application,verify_delivery_boy_application,
                register_shop,register_delivery_boy,shop_onwer_home,delivery_boy_home,admin_home,delivery_boy_available,delivery_boy_not_available,
                delivery_boy_previous_order,delivery_boy_profile,shop_previous_order,shop_products,shop_product_view,product_creation_view,change_discount_view

)
app_name='business'

urlpatterns=[
    path('home/',business_home,name='business-home'),
    path('shop_onwer/',shop_onwer_home,name='shop-owner-home'),
    path('shop/<id>/change_discount/',change_discount_view,name='change-discount'),
    path('delivery_boy',delivery_boy_home,name='delivery-boy-home'),
    path('shop_product/<id>/detail/',shop_product_view,name='shop-product-detail'),
    path('delivery_boy/<id>/previous_orders/',delivery_boy_previous_order,name='previous-order'),
    path('new_product/',product_creation_view,name='new-product'),
    path('shop/<id>/previous_orders/',shop_previous_order,name='shop-previous-order'),
    path('delivery_boy/<id>/available/',delivery_boy_available,name='delivery-boy-available'),
    path('shop/<id>/products/',shop_products,name='shop-products'),
    path('delivery_boy/<id>/not_available/',delivery_boy_not_available,name='delivery-boy-not-available'),
    path('admin',admin_home,name='admin-home'),
    path('delivery_boy/<id>/profile/',delivery_boy_profile,name='delivery-boy-profile'),
    path('new_online_shop_applications/',new_online_shop_applications,name='new-shop-applications'),
    path('verify_shop_application/',verify_shop_application,name='verify-shop'),
    path('new_shop/<id>/register/',register_shop,name='shop-register'),
    path('new_delivery_boy/<id>/register/',register_delivery_boy,name='delivery-boy-register'),
    path('verify_delivery_job_application/',verify_delivery_boy_application,name='verify-delivery-boy'),
    path('new_delivery_boy_applications/',new_delivery_boy_applications,name='new-delivery-boy-applications'),
    path('shop_verified_applications/',shop_verified_applications,name='shop-verified-applications'),
    path('delivery_boy_verified_applications/',delivery_boy_verified_applications,name='delivery-boy-verified-applications'),
    path('shop/<id>/accept/',shop_accept_view,name='shop-accept'),
    path('delivery_boy/<id>/reject/',delivery_boy_reject_view,name='delivery-boy-reject'),
    path('delivery_boy/<id>/accept/',delivery_boy_accept_view,name='delivery-boy-accept'),
    path('shop/<id>/reject/',shop_reject_view,name='shop-reject'),
    path('new_online_shop/',online_shop_portal,name='new-online-shop'),
    path('new_delivery_boy/',new_delivery_boy,name='new-delivery-boy'),
    path('staff/',staff_home,name='staff-home'),
    path('shop_application/<id>/',shop_application_detail,name='shop-application-detail'),
    path('delivery_boy_application/<id>/',delivery_boy_application_detail,name='delivery-boy-application-detail'),
]