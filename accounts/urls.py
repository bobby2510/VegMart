from django.urls import path
from .views import register,login,logout,customer_profile_update_view
app_name='accounts'
urlpatterns=[
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('update_profile/',customer_profile_update_view,name='update-customer-profile')
]