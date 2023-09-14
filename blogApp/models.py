from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

from taggit.managers import TaggableManager
from django_jalali.db import models as jmodels
from django.urls import reverse
from django.utils.text import slugify



class Post(models.Model):
    author = models.CharField(max_length=30, default="مهدی آزادی")
    title = models.CharField(max_length=100, verbose_name="تگ عنوان اصلی") 
    title_tag = models.CharField(max_length=100, verbose_name="تگ-seo") 
    meta_desc = models.CharField(max_length=100, verbose_name="متا-تگ")   
    title_slug = models.CharField(max_length=100,blank=True , verbose_name="تگ-slug")  
    slug = models.SlugField(max_length=255,blank=True,unique=True, verbose_name="اسلاگ")   
    img_banner = models.ImageField(upload_to="images/" ,default="blog_image.jpg", verbose_name="تصویر بنر")
    img_small_one = models.ImageField(upload_to="images/")    
    title_one = models.CharField(max_length=100)   
    text_one = models.TextField()
    title_two = models.CharField(max_length=100)
    text_two = models.TextField()
    title_tree = models.CharField(max_length=100)
    text_tree = models.TextField(blank=True)
    text_four = models.TextField(blank=True)
    text_five = models.TextField(blank=True)
    text_sex = models.TextField(blank=True)
    tags = TaggableManager()    
    created_at = jmodels.jDateTimeField(auto_now_add=True)    
    views = models.IntegerField(default=0, editable=False)
   
    

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.slug])               
                              

    def update_views(self):
        self.views = models.F('views') + 1
        self.save()

    def __str__(self):
        return self.title

