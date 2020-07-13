from django.shortcuts import render,redirect
from .forms import OwnerDataForm,OwnerAddressForm,ShopDataForm,ShopAddressForm,DeliveryBoyPersonalDataForm,DeliveryBoyAddressForm,ProductForm,ProductCreationForm,ChangeDiscountForm
from .models import ShopOnline,DeliveryBoyJob
from store.models import ShopOwner,DelivaryBoy,BaseAddress,Shop,OrderShipping,Product
from accounts.models import User,UserRole
from django.db.models import Q
from store.decorators import check_access
from django.contrib import messages
import re
@check_access(allowed_users=['anonymous',])
def business_home(request):
    return render(request,'business/business_home.html',{'business_flag':True,})

def create_shoponline_obj(form1,form2,form3,form4):
    username=form1.cleaned_data.get('username')
    email=form1.cleaned_data.get('email')
    phone_number=form1.cleaned_data.get('phone_number')
    first_name=form1.cleaned_data.get('first_name')
    last_name=form1.cleaned_data.get('last_name')
    age=form1.cleaned_data.get('age')
    gender=form1.cleaned_data.get('gender')
    owner_address_line=form2.cleaned_data.get('owner_address_line')
    owner_city=form2.cleaned_data.get('owner_city')
    owner_country=form2.cleaned_data.get('owner_country')
    owner_state=form2.cleaned_data.get('owner_state')
    owner_landmark=form2.cleaned_data.get('owner_landmark')
    owner_zipcode=form2.cleaned_data.get('owner_zipcode')
    shop_name=form3.cleaned_data.get('shop_name')
    shop_image=form3.cleaned_data.get('shop_image')
    shop_description=form3.cleaned_data.get('shop_description')
    shop_address_line=form4.cleaned_data.get('shop_address_line')
    shop_city=form4.cleaned_data.get('shop_city')
    shop_country=form4.cleaned_data.get('shop_country')
    shop_state=form4.cleaned_data.get('shop_state')
    shop_landmark=form4.cleaned_data.get('shop_landmark')
    shop_zipcode=form4.cleaned_data.get('shop_zipcode')
    return ShopOnline(username=username,email=email,phone_number=phone_number,age=age,gender=gender,first_name=first_name,last_name=last_name,owner_country=owner_country,owner_state=owner_state,onwer_address_line=owner_address_line,owner_city=owner_city,owner_landmark=owner_landmark,shop_country=shop_country,shop_state=shop_state,shop_address_line=shop_address_line,shop_city=shop_city,shop_landmark=shop_landmark,shop_name=shop_name,shop_image=shop_image,shop_description=shop_description,owner_zipcode=owner_zipcode,shop_zipcode=shop_zipcode)

@check_access(allowed_users=['anonymous',])
def online_shop_portal(request):
    if request.method == 'POST':
        form1=OwnerDataForm(request.POST)
        form2=OwnerAddressForm(request.POST)
        form3=ShopDataForm(request.POST,request.FILES)
        form4=ShopAddressForm(request.POST)
        context={
            'form1':form1,
            'form2':form2,
            'form3':form3,
            'form4':form4,
        }
        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            shop_online_obj=create_shoponline_obj(form1,form2,form3,form4)
            shop_online_obj.save()
            messages.success(request,'Your data is successfully submitted!')
            return redirect('business:business-home')
        return render(request,'business/business_new_store.html',context)
    else:
        form1=OwnerDataForm()
        form2=OwnerAddressForm()
        form3=ShopDataForm()
        form4=ShopAddressForm()
        context={
            'form1':form1,
            'form2':form2,
            'form3':form3,
            'form4':form4,
        }
        return render(request,'business/business_new_store.html',context)

def create_delivery_boy_obj(form1,form2):
    username=form1.cleaned_data.get('username')
    email=form1.cleaned_data.get('email')
    phone_number=form1.cleaned_data.get('phone_number')
    first_name=form1.cleaned_data.get('first_name')
    last_name=form1.cleaned_data.get('last_name')
    age=form1.cleaned_data.get('age')
    gender=form1.cleaned_data.get('gender')
    image=form1.cleaned_data.get('image')
    address_line=form2.cleaned_data.get('address_line')
    city=form2.cleaned_data.get('city')
    country=form2.cleaned_data.get('country')
    state=form2.cleaned_data.get('state')
    landmark=form2.cleaned_data.get('landmark')
    zipcode=form2.cleaned_data.get('zipcode')
    return DeliveryBoyJob(username=username,email=email,phone_number=phone_number,age=age,gender=gender,image=image,first_name=first_name,last_name=last_name,address_line=address_line,zipcode=zipcode,landmark=landmark,country=country,state=state,city=city)

@check_access(allowed_users=['anonymous',])
def new_delivery_boy(request):
    if request.method == 'POST':
        form1=DeliveryBoyPersonalDataForm(request.POST,request.FILES)
        form2=DeliveryBoyAddressForm(request.POST)
        context={
            'form1':form1,
            'form2':form2,
        }
        if form1.is_valid() and form2.is_valid():
            delivery_boy_obj=create_delivery_boy_obj(form1,form2)
            delivery_boy_obj.save()
            messages.success(request,'Your data is successfully submitted!')
            return redirect('business:business-home')
        return render(request,'business/business_delivery_boy.html',context)
    else:
        form1=DeliveryBoyPersonalDataForm()
        form2=DeliveryBoyAddressForm()
        context={
            'form1':form1,
            'form2':form2,
        }
        return render(request,'business/business_delivery_boy.html',context)


#staff home panel
@check_access(allowed_users=['Staff',])
def staff_home(request):
    qs_shop=ShopOnline.objects.all()
    qs_delivery_boy=DeliveryBoyJob.objects.all()
    shop_total_number_of_applications=qs_shop.count()
    delivery_boy_total_number_of_applications=qs_delivery_boy.count()
    shop_verified_applications=qs_shop.filter(is_verified=True).count()
    delivery_boy_verified_applications=qs_delivery_boy.filter(is_verified=True).count()
    shop_accepted_applications=qs_shop.filter(is_verified=True,is_accepted=True).count()
    delivery_boy_accepted_applications=qs_delivery_boy.filter(is_verified=True,is_accepted=True).count()
    shop_rejected_applications=qs_shop.filter(is_verified=True,is_rejected=True).count()
    delivery_boy_rejected_applications=qs_delivery_boy.filter(is_verified=True,is_rejected=True).count()

    context={
        'shop_total_number_of_applications':shop_total_number_of_applications,
        'delivery_boy_total_number_of_applications': delivery_boy_total_number_of_applications,
        'shop_verified_applications':shop_verified_applications,
        'delivery_boy_verified_applications':delivery_boy_verified_applications,
        'shop_accepted_applications':shop_accepted_applications,
        'delivery_boy_accepted_applications':delivery_boy_accepted_applications,
        'shop_rejected_applications':shop_rejected_applications,
        'delivery_boy_rejected_applications':delivery_boy_rejected_applications,

    }
    return render(request,'business/staff_home.html',context)

#delivery_boy home
@check_access(allowed_users=['DeliveryBoy',])
def delivery_boy_home(request):
    delivery_boy=request.user.delivaryboy
    active_orders=delivery_boy.shipped_order.filter(is_delivered=False)
    active=active_orders.exists()
    context={
        'active_orders':active_orders,
        'active':active_orders,
    }
    return render(request,'business/delivery_boy_home.html',context)

#ShopOnwer home
@check_access(allowed_users=['ShopOwner',])
def shop_onwer_home(request):
    shop_owner=request.user.shopowner
    qs=OrderShipping.objects.filter(Q(order__shop=shop_owner.shop) & Q(is_delivered=False)).distinct()
    context={
        'active':qs.exists(),
        'orders':qs,
    }
    return render(request,'business/shop_owner_home.html',context)
#admin home
@check_access(allowed_users=['Admin',])
def admin_home(request):
    return render(request,'business/admin_home.html')

#new online shop applications
@check_access(allowed_users=['Staff',])
def new_online_shop_applications(request):
    qs=ShopOnline.objects.filter(is_verified=False)
    new_shop_applications=qs.exists()
    print(new_shop_applications)
    context={
        'new_shop_applications':qs,
        'applications':new_shop_applications,
    }
    return render(request,'business/new_online_shop.html',context)

#shop application detail
@check_access(allowed_users=['Staff',])
def shop_application_detail(request,id):
    try:
        obj=ShopOnline.objects.get(id=id)
        return render(request,'business/shop_application_detail.html',{'application':obj,})
    except:
        return render(request,'store/error.html')

#new delivery boy job applications
@check_access(allowed_users=['Staff',])
def new_delivery_boy_applications(request):
    qs=DeliveryBoyJob.objects.filter(is_verified=False).order_by('id')
    new_delivery_boy_applications=qs.exists()
    context={
        'new_delivery_boy_applications':qs,
        'applications':new_delivery_boy_applications,
    }
    return render(request,'business/new_delivery_boy.html',context)

#delivery boy application detail
@check_access(allowed_users=['Staff',])
def delivery_boy_application_detail(request,id):
    try:
        obj=DeliveryBoyJob.objects.get(id=id)
        return render(request,'business/delivery_boy_application_detail.html',{'application':obj,})
    except:
        return render(request,'store/error.html')

#shop verified applications 
@check_access(allowed_users=['Staff',])
def shop_verified_applications(request):
    status=request.GET.get('status')
    if status == None:
        status=1
    else:
        status=int(status)
    qs=ShopOnline.objects.filter(is_verified=True)
    applications=None
    if status ==1:
        applications=qs.order_by('id')
    elif status ==2:
        applications=qs.filter(is_accepted=True).order_by('id')
    else:
        applications=qs.filter(is_rejected=True).order_by('id')
    is_applications_exist=applications.exists()
    context={
        'applications':applications,
        'status':status,
        'is_applications_exist':is_applications_exist,
    }
    return render(request,'business/shop_verified_applications.html',context)

#delivery boy verified applications 
@check_access(allowed_users=['Staff',])
def delivery_boy_verified_applications(request):
    status=request.GET.get('status')
    if status == None:
        status=1
    else:
        status=int(status)
    qs=DeliveryBoyJob.objects.filter(is_verified=True)
    applications=None
    if status ==1:
        applications=qs.order_by('id')
    elif status ==2:
        applications=qs.filter(is_accepted=True).order_by('id')
    else:
        applications=qs.filter(is_rejected=True).order_by('id')
    is_applications_exist=applications.exists()
    context={
        'applications':applications,
        'status':status,
        'is_applications_exist':is_applications_exist,
    }
    return render(request,'business/delivery_boy_verified_applications.html',context)

@check_access(allowed_users=['Staff',])
def shop_accept_view(request,id):
    if request.method=='POST':
        try:
            obj=ShopOnline.objects.get(id=id)
            obj.is_accepted=True
            obj.is_verified=True
            obj.save()
            return redirect(obj.get_absolute_url)
        except:
            return render(request,'store/error.html')
    else:
        return render(request,'store/error.html')

@check_access(allowed_users=['Staff',])
def shop_reject_view(request,id):
    if request.method=='POST':
        try:
            obj=ShopOnline.objects.get(id=id)
            obj.is_rejected=True
            obj.is_verified=True
            obj.save()
            return redirect(obj.get_absolute_url)
        except:
            return render(request,'store/error.html')
    else:
        return render(request,'store/error.html')

@check_access(allowed_users=['Staff',])
def delivery_boy_accept_view(request,id):
    if request.method == 'POST':
        try:
            obj=DeliveryBoyJob.objects.get(id=id)
            obj.is_accepted=True
            obj.is_verified=True
            obj.save()
            return redirect(obj.get_absolute_url)
        except:
            return render(request,'store/error.html')
    else:
        return render(request,'store/error.html')

@check_access(allowed_users=['Staff',])
def delivery_boy_reject_view(request,id):
    if request.method == 'POST':
        try:
            obj=DeliveryBoyJob.objects.get(id=id)
            obj.is_rejected=True
            obj.is_verified=True
            obj.save()
            return redirect(obj.get_absolute_url)
        except:
            return render(request,'store/error.html')
    else:
        return render(request,'store/error.html')
        
#verifying shop onilne appications
@check_access(allowed_users=['anonymous',])
def verify_shop_application(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        phone_number=request.POST.get('phone_number')
        try:
            obj=ShopOnline.objects.get(username=username,phone_number=phone_number)
            if obj.is_registered:
                messages.info(request,'Application is already registered, kindly login!')
                return redirect('business:new-online-shop')
            if not obj.is_verified:
                messages.info(request,'Application is not yet verified, we will mail you when it is done!')
                return redirect('business:new-online-shop')
            if obj.is_verified and obj.is_rejected:
                messages.warning(request,'Sorry! Your Application is Rejected.')
                return redirect('business:new-online-shop')
            messages.success(request,'Congratulations! Your Application is Accepted! kindly register Here')
            return render(request,'business/register_shop.html',{'obj':obj})    
        except:
            messages.warning(request,'Invalid username or phone number, kindly check again!')
            return redirect('business:new-online-shop')
    else:
        return render(request,'store/error.html')

        
#verifying devivery boy appications
@check_access(allowed_users=['anonymous',])
def verify_delivery_boy_application(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        phone_number=request.POST.get('phone_number')
        try:
            obj=DeliveryBoyJob.objects.get(username=username,phone_number=phone_number)
            if obj.is_registered:
                messages.info(request,'Application is already registered, kindly login!')
                return redirect('business:new-delivery-boy')
            if not obj.is_verified:
                messages.info(request,'Application is not yet verified, we will mail you when it is done!')
                return redirect('business:new-delivery-boy')
            if obj.is_verified and obj.is_rejected:
                messages.warning(request,'Sorry! Your Application is Rejected.')
                return redirect('business:new-delivery-boy')
            messages.success(request,'Congratulations! Your Application is Accepted! kindly register Here')
            return render(request,'business/register_delivery_boy.html',{'obj':obj,})    
        except:
            messages.warning(request,'Invalid username or phone number, kindly check again!')
            return redirect('business:new-delivery-boy')
    else:
        return render(request,'store/error.html')

def remove_media(image_url):
    return re.sub('media/','',image_url)

#register shop 
@check_access(allowed_users=['anonymous',])
def register_shop(request,id):
    if request.method == 'POST':
        try:
            temp_shop=ShopOnline.objects.get(id=id)
            password1=request.POST.get('password1')
            shop_owner=UserRole.objects.filter(role__iexact='ShopOwner').first()
            user=User(
                username=temp_shop.username,
                email=temp_shop.email,
                age=temp_shop.age,
                gender=temp_shop.gender,
                phone_number=temp_shop.phone_number,
                first_name=temp_shop.first_name,
                last_name=temp_shop.last_name,
                user_role=shop_owner
            )
            user.set_password(password1)
            user.save()
            owner_address=BaseAddress(
                country=temp_shop.owner_country,
                state=temp_shop.owner_state,
                address_line=temp_shop.onwer_address_line,
                city=temp_shop.owner_city,
                landmark=temp_shop.owner_landmark,
            )
            owner_address.save()
            shop_address=BaseAddress(
                country=temp_shop.shop_country,
                state=temp_shop.shop_state,
                address_line=temp_shop.shop_address_line,
                city=temp_shop.shop_city,
                landmark=temp_shop.shop_landmark,
            )
            shop_address.save()
            shop=Shop(
                name=temp_shop.shop_name,
                image=remove_media(temp_shop.shop_image.url),
                address=shop_address,
                description=temp_shop.shop_description
            )
            shop.save()
            shop_owner_obj=ShopOwner(
                user=user,
                address=owner_address,
                shop=shop,
            )
            shop_owner_obj.save()
            temp_shop.is_registered=True
            temp_shop.save()
            messages.success(request,'Congratulations! Your account is Created Successfully!')
            return redirect('accounts:login')
        except:
            return render(request,'store/error.html')
    else:
        return render(request,'store/error.html')
        

#register delivery boy
@check_access(allowed_users=['anonymous',])
def register_delivery_boy(request,id):
    if request.method == 'POST':
        try:
            temp_shop=DeliveryBoyJob.objects.get(id=id)
            password1=request.POST.get('password1')
            delivery_boy=UserRole.objects.filter(role__iexact='DeliveryBoy').first()
            user=User(
                username=temp_shop.username,
                email=temp_shop.email,
                age=temp_shop.age,
                gender=temp_shop.gender,
                phone_number=temp_shop.phone_number,
                first_name=temp_shop.first_name,
                last_name=temp_shop.last_name,
                user_role=delivery_boy
            )
            user.set_password(password1)
            user.save()
            address=BaseAddress(
                country=temp_shop.country,
                state=temp_shop.state,
                address_line=temp_shop.address_line,
                city=temp_shop.city,
                landmark=temp_shop.landmark,
            )
            address.save()
            delivery_boy_obj=DelivaryBoy(
                user=user,
                address=address,
                image=remove_media(temp_shop.image.url),
            )
            delivery_boy_obj.save()
            temp_shop.is_registered=True
            temp_shop.save()
            messages.success(request,'Congratulations! Your account is Created Successfully!')
            return redirect('accounts:login')
        except:
            return render(request,'store/error.html')
    else:
        return render(request,'store/error.html')

@check_access(allowed_users=['DeliveryBoy',])
def delivery_boy_available(request,id):
    if request.method == 'POST':
        try:
            delivery_boy=DelivaryBoy.objects.get(id=id)
            delivery_boy.is_available=True
            delivery_boy.save()
            return redirect('business:delivery-boy-home')
        except:
            return render(request,'store/error.html')
    else:
        return render(request,'store/error.html')

@check_access(allowed_users=['DeliveryBoy',])
def delivery_boy_not_available(request,id):
    if request.method == 'POST':
        try:
            delivery_boy=DelivaryBoy.objects.get(id=id)
            delivery_boy.is_available=False
            delivery_boy.save()
            return redirect('business:delivery-boy-home')
        except:
            return render(request,'store/error.html')
    else:
        return render(request,'store/error.html')

#delivery boy previous orders
@check_access(allowed_users=['DeliveryBoy',])
def delivery_boy_previous_order(request,id):
    try:
        delivery_boy=DelivaryBoy.objects.get(id=id)
        previous_orders=delivery_boy.shipped_order.filter(is_delivered=True)
        active=previous_orders.exists()
        context={
            'previous_orders':previous_orders,
            'previous':active,
        }
        return render(request,'business/delivery_boy_previous_orders.html',context)
    except:
        return render(request,'store/error.html')

@check_access(allowed_users=['DeliveryBoy',])
def delivery_boy_profile(request,id):
    try:
        delivery_boy=DelivaryBoy.objects.get(id=id)
        context={
            'obj':delivery_boy,
        }
        return render(request,'business/delivery_boy_profie.html',context)
    except:
        return render(request,'store/error.html')

#delivery boy previous orders
@check_access(allowed_users=['ShopOwner',])
def shop_previous_order(request,id):
    try:
        shop_owner=ShopOwner.objects.get(id=id)
        previous_orders=OrderShipping.objects.filter(Q(order__shop=shop_owner.shop) & 
        Q(is_delivered=True))
        active=previous_orders.exists()
        context={
            'previous_orders':previous_orders,
            'previous':active,
        }
        return render(request,'business/delivery_boy_previous_orders.html',context)
    except:
        return render(request,'store/error.html')

#shop owner products 
@check_access(allowed_users=['ShopOwner',])
def shop_products(request,id):
    try:
        shop=Shop.objects.get(id=id)
        products=shop.product.all()
        present=products.exists()
        context={
            'present':present,
            'products':products,
        }
        return render(request,'business/shop_products.html',context)
    except:
        return render(request,'store/error.html')

#shop owner product edit view
@check_access(allowed_users=['ShopOwner',])
def shop_product_view(request,id):
    try:
        product=Product.objects.get(id=id)
        if request.method == 'POST':
            form=ProductForm(request.POST,request.FILES,instance=product)
            if form.is_valid():
                form.save()
                return redirect( product.get_product_edit_url )
            return render(request,'business/shop_product_detail.html',{'form':form,'product':product,})
        else:
            form=ProductForm(instance=product)
            return render(request,'business/shop_product_detail.html',{'form':form,'product':product,})
    except:
        return render(request,'store/error.html')

@check_access(allowed_users=['ShopOwner',])
def product_creation_view(request):
    if request.method == 'POST':
        form=ProductCreationForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.instance
            obj.shop=request.user.shopowner.shop
            obj.save()
            return redirect( obj.get_product_edit_url )
        return render(request,'business/product_creation.html',{'form':form,})
    else:
        form=ProductForm()
        return render(request,'business/product_creation.html',{'form':form,})
        
@check_access(allowed_users=['ShopOwner',])
def change_discount_view(request,id):
    try:
        shop=Shop.objects.get(id=id)
        if request.method == 'POST':
            form=ChangeDiscountForm(request.POST,instance=shop)
            if form.is_valid():
                form.save()
                return redirect( request.user.shopowner.get_discount_url )
            return render(request,'business/shop_discount_edit.html',{'form':form,'shop':shop,})
        else:
            form=ChangeDiscountForm(instance=shop)
            return render(request,'business/shop_discount_edit.html',{'form':form,'shop':shop,})
    except:
        return render(request,'store/error.html')
        
        