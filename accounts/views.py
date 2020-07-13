from django.shortcuts import render,redirect
from django.contrib.auth import login as user_login,logout as user_logout
from .forms import UserRegistrationForm,UserLoginForm,UpdateProfileForm
from store.models import Customer
from store.decorators import check_access
from django.contrib import messages

@check_access(allowed_users=['anonymous',])
def register(request):
    if request.method =='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user_obj=form.instance
            print(user_obj)
            Customer.objects.create(user=user_obj)
            messages.success(request,'Account created successfully! please login')
            return redirect('accounts:login')
        return render(request,'accounts/register.html',{'form':form,})
    form=UserRegistrationForm()
    return render(request,'accounts/register.html',{'form':form,})

@check_access(allowed_users=['anonymous',])
def login(request):
    path=request.GET.get('next')
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            user_obj=form.cleaned_data.get('user_obj')
            user_login(request,user_obj)
            messages.success(request,'You have logged in successfully!')
            if user_obj.user_role.role == 'Customer':
                if path == None or path == '/accounts/logout/':
                    return redirect('store:home')
                return redirect(path)
            elif user_obj.user_role.role == 'ShopOwner':
                return redirect('business:shop-owner-home')
            elif user_obj.user_role.role == 'DeliveryBoy':
                return redirect('business:delivery-boy-home')
            elif user_obj.user_role.role == 'Staff':
                return redirect('business:staff-home')
            else:
                return redirect('business:admin-home')
        return render(request,'accounts/login.html',{'form':form,})
    form=UserLoginForm()
    return render(request,'accounts/login.html',{'form':form,})

@check_access(allowed_users=['Customer','ShopOwner','DeliveryBoy','Admin','Staff',])
def logout(request):
    if request.user.is_authenticated:
        user_logout(request)
    return render(request,'accounts/logout.html')

@check_access(allowed_users=['Customer',])
def customer_profile_update_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=UpdateProfileForm(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request,'Your Profile has updated successfully!')
                return redirect('accounts:update-customer-profile')
            return render(request,'accounts/update_profile.html',{'form':form,})
        form=UpdateProfileForm(instance=request.user)
        return render(request,'accounts/update_profile.html',{'form':form,})
    return render(request,'store/error.html')