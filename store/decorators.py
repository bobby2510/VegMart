from store.models import Customer,DelivaryBoy,Staff,ShopOwner
from accounts.models import User,UserRole
from django.http import HttpResponse
from django.shortcuts import redirect


def check_access(allowed_users=[]):
    def decorator(view_func):
        def wraper(request,*args,**kwargs):
            if not request.user.is_authenticated:
                if 'anonymous' in allowed_users:
                    return view_func(request,*args,**kwargs)
                else:
                    return HttpResponse('you are not authorized to view this page!')
            else:
                if request.user.user_role.role in allowed_users:
                    return view_func(request,*args,**kwargs)
                else:
                    return HttpResponse('you are not authorized to view this page!')
        return wraper
    return decorator