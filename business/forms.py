from django import forms
from .models import ShopOnline
from store.models import Product,Category,Shop
from accounts.models import User


AGE_CHOICES=(('M','Male'),
                ('F','Female'),
                ('O','Others'),
                )

COUNTRY_CHOICES=(('IND','India'),)
STATE_CHOICES=(('AP','Andhra Predesh'),
            ('TS','Telangana'),
)

class OwnerDataForm(forms.Form):
    username=forms.CharField(label='',required=True,widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'Username'
        }
    ))
    email=forms.CharField(label='',required=True,widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'Email',
        }
    ))
    phone_number=forms.CharField(label='',required=True,widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'Phone Number'
        }
    ))
    first_name=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'First name',
        }
    ))
    last_name=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'Last name',
        }
    ))
    age=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'Age',
        }
    ))
    gender=forms.ChoiceField(label='',widget=forms.Select(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'Gender'
        }
    ),choices=AGE_CHOICES,)
    
    class Meta:
        fields=['username','email','phone_number','first_name','last_name','age','gender']
    
    def clean(self,*args,**kwargs):
        print('hi there using sai')
        temp_username=self.cleaned_data.get('username')
        print(temp_username,' it is a test')
        user_qs=User.objects.filter(username=temp_username)
        shoponline_qs=ShopOnline.objects.filter(username=temp_username)
        print(user_qs)
        print(shoponline_qs)
        if user_qs.exists() or  shoponline_qs.exists() :
            print('valid here')
            raise forms.ValidationError('username already exists try another one!')
        super(OwnerDataForm,self).clean(*args,**kwargs)


class OwnerAddressForm(forms.Form):
    owner_address_line=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'Address Line',

        }
    ))
    owner_city=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'City',
        }
    ))
    owner_country=forms.ChoiceField(label='',widget=forms.Select(
        attrs={
            'class':'form-control custom-form',
        }
    ),choices=COUNTRY_CHOICES,)
    owner_state=forms.ChoiceField(label='',widget=forms.Select(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'State',

        }
    ),choices=STATE_CHOICES,)
    owner_landmark=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'LandMark',
        }
    ))
    owner_zipcode=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'Zipcode',
        }
    ))

    class Meta:
        fields=['owner_address_line','owner_city','owner_country','owner_state','owner_landmark','owner_zipcode']

class ShopDataForm(forms.Form):
    shop_name=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'Shop Name',
        }
    ))
    shop_image=forms.ImageField(label='Shop Image - ',)
    shop_description=forms.CharField(label='',widget=forms.Textarea(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'Shop Description'
        }
    ))

    class Meta:
        fields=['shop_name','shop_image','shop_description']
class ShopAddressForm(forms.Form):
    shop_address_line=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'Address Line',

        }
    ))
    shop_city=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'City',
        }
    ))
    shop_country=forms.ChoiceField(label='',widget=forms.Select(
        attrs={
            'class':'form-control custom-form',
        }
    ),choices=COUNTRY_CHOICES,)
    shop_state=forms.ChoiceField(label='',widget=forms.Select(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'State',

        }
    ),choices=STATE_CHOICES,)
    shop_landmark=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'LandMark',
        }
    ))
    shop_zipcode=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'Zipcode',
        }
    ))

    class Meta:
        fields=['shop_address_line','shop_city','shop_country','shop_state','shop_landmark','shop_zipcode']

class DeliveryBoyPersonalDataForm(forms.Form):
    username=forms.CharField(label='',required=True,widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'Username'
        }
    ))
    email=forms.CharField(label='',required=True,widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'Email',
        }
    ))
    phone_number=forms.CharField(label='',required=True,widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'Phone Number'
        }
    ))
    first_name=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'First name',
        }
    ))
    last_name=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'Last name',
        }
    ))
    age=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'Age',
        }
    ))
    gender=forms.ChoiceField(label='',widget=forms.Select(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'Gender'
        }
    ),choices=AGE_CHOICES,)
    image=forms.ImageField(label='Delivery boy image - ')
    
    class Meta:
        fields=['username','email','phone_number','first_name','last_name','age','gender','image']

class DeliveryBoyAddressForm(forms.Form):
    address_line=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'Address Line',

        }
    ))
    city=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'City',
        }
    ))
    country=forms.ChoiceField(label='',widget=forms.Select(
        attrs={
            'class':'form-control custom-form',
        }
    ),choices=COUNTRY_CHOICES,)
    state=forms.ChoiceField(label='',widget=forms.Select(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'State',

        }
    ),choices=STATE_CHOICES,)
    landmark=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'LandMark',
        }
    ))
    zipcode=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'placeholder':'Zipcode',
        }
    ))

    class Meta:
        fields=['address_line','city','country','state','landmark','zipcode']


class ProductForm(forms.ModelForm):
    name=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'custom-form',
            'placeholder':'Name'
        }
    ))
    price=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'custom-form',
            'placeholder':'Product Price per kg'
        }
    ))
    image=forms.ImageField(required=False, error_messages = {'invalid':"Image files only"}, widget=forms.FileInput)
    category=forms.ModelChoiceField(label='',queryset=Category.objects.all(),empty_label=None)
    class Meta:
        model=Product
        fields=['name','price','category','image']

class ProductCreationForm(forms.ModelForm):
    name=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'custom-form',
            'placeholder':'Name'
        }
    ))
    price=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'custom-form',
            'placeholder':'Product Price per kg'
        }
    ))
    image=forms.ImageField(required=True, error_messages = {'invalid':"Image files only"}, widget=forms.FileInput)
    category=forms.ModelChoiceField(label='',queryset=Category.objects.all(),empty_label=None)
    class Meta:
        model=Product
        fields=['name','price','category','image']

class ChangeDiscountForm(forms.ModelForm):
    discount=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form-full',
            'placeholder':'Shop Discount',
        }
    ))
    limit_of_discount=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form-full',
            'placeholder':'Discount Limit',
        }
    ))
    minimum_amount=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form-full',
            'placeholder':'Minimum Amount',
        }
    ))

    class Meta:
        model=Shop
        fields=['discount','limit_of_discount','minimum_amount']

