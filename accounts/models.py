from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.core.validators import RegexValidator

USERNAME_RAGEX='^[a-zA-Z][a-zA-Z0-9]{3,}'
GENDER_CHOICES=(('M','Male'),
                ('F','Female'),
                ('O','Others'),
                )
PHONE_NO_REGEX='^[6-9][0-9]{9}$'


class UserRole(models.Model):
    role=models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.role

class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not email:
            raise ValueError('Invalid Username')
        user=self.model(
            username=username,
            email=self.normalize_email(email)
        )
        customer=UserRole.objects.filter(role__iexact='Customer').first()
        user.user_role=customer
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username,email,password=None):
        user=self.create_user(username,email,password)
        user.is_admin=True
        user.is_staff=True
        admin=UserRole.objects.filter(role__iexact='Admin').first()
        user.user_role=admin
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
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
    user_role=models.ForeignKey('UserRole',null=True,blank=False,on_delete=models.SET_NULL)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    objects=UserManager()
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email',]

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
