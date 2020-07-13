from django import forms 
from .models import *

COUNTRY_CHOICES=(('IND','India'),)
STATE_CHOICES=(('AP','Andhra Predesh'),
            ('TS','Telangana'),
)
class CustomerAddressForm(forms.ModelForm):
    address_line=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'value':'Address Line',
            'id':'js_form',
            'placeholder':'Address Line',

        }
    ))
    city=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'value':'City',
            'id':'js_form',
            'placeholder':'City',
        }
    ))
    country=forms.ChoiceField(label='',widget=forms.Select(
        attrs={
            'class':'form-control custom-form',
            'value':'India',
        }
    ),choices=COUNTRY_CHOICES,)
    state=forms.ChoiceField(label='',widget=forms.Select(
        attrs={
            'class':'form-control custom-form',
            'value':'Andhra Pradesh',
            'placeholder':'State',

        }
    ),choices=STATE_CHOICES,)
    landmark=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'value':'LandMark',
            'placeholder':'LandMark',
            'id':'js_form'
        }
    ))
    zipcode=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form',
            'value':'Zipcode',
            'placeholder':'Zipcode',
            'id':'js_form'
        }
    ))

    class Meta:
        model=Customer_Address
        fields=['address_line','landmark','city','zipcode','state','country']
