from django.db import models


from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from django_jalali.db import models as jmodels
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)



class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address.")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email,password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    COURSE_TYPE = [
    ("FREE","FREE"),
    ("PAID","PAID"),
    ]

    email = models.EmailField(
        verbose_name='email',
        unique=True,
        db_index=True,
    )
    full_name = models.CharField(
        max_length=191,
        blank=True,
    )
    short_name = models.CharField(
        max_length=191,
        blank=True,
    )
    photo = models.ImageField(upload_to='images/',blank=True, default="images/assets/default_image.jpg")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    django_course = models.BooleanField(default=False)
    is_student =  models.BooleanField(default=False)
    course_type = models.CharField(max_length=4,choices=COURSE_TYPE, default="PAID",blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.short_name

    def __str__(self):
        return f"{self.email} ({self.full_name})"
    
   





class Tags(models.Model): 
    tag_word = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tag_word


class Question(models.Model):
    title = models.CharField(max_length=500, unique=True, verbose_name="عنوان سوال")
    body = models.TextField(verbose_name="متن  سوال")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    tags = models.ManyToManyField(Tags, blank=True)
    views = models.IntegerField(default=0)
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    updated_at = jmodels.jDateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ['-created_at']


    def __str__(self):
        return self.title[:50]

def pre_save_receiver(sender, instance, *args, **kwargs):
   if not instance.slug:
       instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender=Question)






class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50 ,verbose_name="نام و نام خانوادگی")
    phone = models.CharField(max_length=11, verbose_name="شماره همراه")
    is_apply = models.BooleanField(default=False, blank=False, null=False)
    email = models.EmailField(blank=True)    
    order_date = jmodels.jDateTimeField(auto_now_add=True)   
    paid = models.BooleanField(default=False) 
        

    class Meta:
        ordering = ('-order_date', )

    def __str__(self):
        return f'Order {self.id}'
    
    def save(self, *args, **kwargs):       
        if self.paid == True:
            self.customer.course_type == "FREE"
        super().save(*args, **kwargs)




class Invoice(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    invoice_date =  jmodels.jDateTimeField(auto_now_add=True)  
    authority = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class Transaction(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('failed', 'Failed'),
        ('completed', 'Completed')
    )
    invoice = models.ForeignKey(Invoice, null=True, on_delete=models.SET_NULL)
    transaction_date =  jmodels.jDateTimeField(auto_now_add=True)  
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return str(self.id)
    



