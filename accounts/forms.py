from django import forms
from .models import User,UserRole
from django.db.models import Q

AGE_CHOICES=(('M','Male'),
                ('F','Female'),
                ('O','Others'),
                )


class UserRegistrationForm(forms.ModelForm):
    username=forms.CharField(label='Username',required=True,widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    ))
    email=forms.CharField(label='Email',required=True,widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    ))
    phone_number=forms.CharField(label='Phone Number',required=True,widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    ))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput( attrs={
            'class':'form-control',
        }))
    password2=forms.CharField(label='Password Confirmation',widget=forms.PasswordInput( attrs={
            'class':'form-control',
        }))
    
    class Meta:
        model=User
        fields=['username','email','phone_number','password1','password2']

    def clean(self,*args,**kwargs):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError('Passwords did not match!')
        super(UserRegistrationForm,self).clean(*args,**kwargs)
    def save(self,*args,**kwargs):
        user=super(UserRegistrationForm,self).save(*args,**kwargs)
        password2=self.cleaned_data['password2']
        customer=UserRole.objects.filter(role__iexact='Customer').first()
        user.user_role=customer
        user.set_password(password2)
        user.save()
        return user

class UserLoginForm(forms.Form):
    query=forms.CharField(label='username / email',widget=forms.TextInput(attrs={
            'class':'form-control',
        }))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
        }
    ))
    class Meta:
        fields=['query','password']

    def clean(self,*args,**kwargs):
        query=self.cleaned_data['query']
        password=self.cleaned_data['password']
        queryset=User.objects.filter(
            Q(username__iexact=query) |
            Q(email__iexact=query)
        ).distinct()
        if not queryset.exists() or queryset.count()>1:
            raise forms.ValidationError('Invalid Credentials!')
        user=queryset.first()
        if not user.check_password(password):
            raise forms.ValidationError('Invalid Credentials!')
        self.cleaned_data['user_obj']=user
        super(UserLoginForm,self).clean(*args,**kwargs)

class UpdateProfileForm(forms.ModelForm):
    username=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form-full',
            'readonly':'true',
            'placeholder':'username'
        }
    ))
    email=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form-full',
            'placeholder':'email',
            'readonly':'true',
        }
    ))
    phone_number=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form-full',
            'placeholder':'phone number',
            'readonly':'true',
        }
    ))
    first_name=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form-full',
            'placeholder':'First name',
        }
    ))
    last_name=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form-full',
            'placeholder':'Last name',
        }
    ))
    age=forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'class':'form-control custom-form-full',
            'placeholder':'Age',
        }
    ))
    gender=forms.ChoiceField(label='',widget=forms.Select(
        attrs={
            'class':'form-control custom-form-full',
            'placeholder':'Gender'
        }
    ),choices=AGE_CHOICES,)

    class Meta:
        model=User
        fields=['username','email','phone_number','first_name','last_name','age','gender']