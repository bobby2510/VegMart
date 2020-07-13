from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator


USERNAME_RAGEX='^[a-zA-Z][a-zA-Z0-9]{3,}'
GENDER_CHOICES=(('M','Male'),
                ('F','Female'),
                ('O','Others'),
                )
PHONE_NO_REGEX='^[6-9][0-9]{9}$'

COUNTRY_CHOICES=(('IND','India'),)
STATE_CHOICES=(('AP','Andhra Predesh'),
            ('TS','Telangana'),
)

class ShopOnline(models.Model):
    username=models.CharField(  max_length=300,
                                validators=[
                                    RegexValidator(regex=USERNAME_RAGEX,
                                        message='Invalid Username!',
                                        code='Invalid Username!'
                                    ),
                                ],
                                unique=True
    )
    email=models.CharField( 
                        max_length=255,
                        unique=True,
    )
    phone_number=models.CharField(max_length=10,
                              validators=[
                                  RegexValidator(
                                      regex=PHONE_NO_REGEX,
                                      message='Invalid Phone Number!',
                                      code='Invlaid Phone Number!'
                                  ),
                              ],
                              null=True,unique=True)
    age=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,blank=True,null=True)
    first_name=models.CharField(max_length=255,null=True,blank=True)
    last_name=models.CharField(max_length=255,null=True,blank=True)
    owner_country=models.CharField(max_length=4,choices=COUNTRY_CHOICES)
    owner_state=models.CharField(max_length=4,choices=STATE_CHOICES)
    onwer_address_line=models.TextField(unique=True)
    owner_city=models.CharField(max_length=30)
    owner_landmark=models.CharField(max_length=30)
    shop_country=models.CharField(max_length=4,choices=COUNTRY_CHOICES)
    shop_state=models.CharField(max_length=4,choices=STATE_CHOICES)
    shop_address_line=models.TextField(unique=True)
    shop_city=models.CharField(max_length=30)
    shop_landmark=models.CharField(max_length=30)
    shop_name=models.CharField(max_length=100,unique=True)
    shop_image=models.ImageField(upload_to='shop_images')
    shop_zipcode=models.CharField(max_length=10,null=True,blank=True)
    owner_zipcode=models.CharField(max_length=10,null=True,blank=True)
    shop_description=models.CharField(max_length=1024,null=True,blank=True)
    is_verified=models.BooleanField(default=False)
    is_accepted=models.BooleanField(default=False)
    is_rejected=models.BooleanField(default=False)
    is_registered=models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
    @property
    def get_absolute_url(self):
        return reverse('business:shop-application-detail',kwargs={'id':self.id,})
    @property
    def get_accepted_url(self):
        return reverse('business:shop-accept',kwargs={'id':self.id})
    @property
    def get_rejected_url(self):
        return reverse('business:shop-reject',kwargs={'id':self.id})
    @property
    def get_register_url(self):
        return reverse('business:shop-register',kwargs={'id':self.id})
        

class DeliveryBoyJob(models.Model):
    username=models.CharField(  max_length=300,
                                validators=[
                                    RegexValidator(regex=USERNAME_RAGEX,
                                        message='Invalid Username!',
                                        code='Invalid Username!'
                                    ),
                                ],
                                unique=True
    )
    email=models.CharField( 
                        max_length=255,
                        unique=True,
    )
    phone_number=models.CharField(max_length=10,
                              validators=[
                                  RegexValidator(
                                      regex=PHONE_NO_REGEX,
                                      message='Invalid Phone Number!',
                                      code='Invlaid Phone Number!'
                                  ),
                              ],
                              null=True,unique=True)
    age=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,blank=True,null=True)
    first_name=models.CharField(max_length=255,null=True,blank=True)
    last_name=models.CharField(max_length=255,null=True,blank=True)
    image=models.ImageField(upload_to='deliveryboy_images')
    country=models.CharField(max_length=4,choices=COUNTRY_CHOICES)
    state=models.CharField(max_length=4,choices=STATE_CHOICES)
    address_line=models.TextField(unique=True)
    city=models.CharField(max_length=30)
    landmark=models.CharField(max_length=30)
    zipcode=models.CharField(max_length=10)
    is_verified=models.BooleanField(default=False)
    is_accepted=models.BooleanField(default=False)
    is_rejected=models.BooleanField(default=False)
    is_registered=models.BooleanField(default=False)
    def __str__(self):
        return self.username
    @property
    def get_absolute_url(self):
        return reverse('business:delivery-boy-application-detail',kwargs={'id':self.id,})
    @property
    def get_accepted_url(self):
        return reverse('business:delivery-boy-accept',kwargs={'id':self.id})
    @property
    def get_rejected_url(self):
        return reverse('business:delivery-boy-reject',kwargs={'id':self.id})
    
    @property
    def get_register_url(self):
        return reverse('business:delivery-boy-register',kwargs={'id':self.id})
        


