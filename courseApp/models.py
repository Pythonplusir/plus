from django.db import models


from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from django_jalali.db import models as jmodels
import string, random
from taggit.managers import TaggableManager




def get_random_string(lenght):
    letter = string.ascii_letters
    return ''.join(random.choice(letter) for i in range(lenght))



COURSE_TYPE = [
    ("FREE","FREE"),
    ("PAID","PAID"),
]

class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="تگ عنوان اصلی") 
    title_tag = models.CharField(max_length=100, verbose_name="تگ-seo") 
    meta_desc = models.CharField(max_length=100, verbose_name="متا-تگ")    
    title_slug = models.CharField(max_length=100,blank=True , verbose_name="تگ-slug")
    gif = models.FileField(upload_to="course_video/", blank=True)    
    desc_one = models.TextField(blank=True)
    desc_two = models.TextField(blank=True)       
    banner_image = models.ImageField(upload_to="course_image/", default="course/default.jpg")
    image = models.ImageField(upload_to="course_image/", blank=True)
    course_type = models.CharField(max_length=4,choices=COURSE_TYPE, default="PAID",blank=True)
    course_length = models.CharField(max_length=20)
    course_slug = models.SlugField(default="-")    
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True)
    tags = TaggableManager()

    class Mata:
        ordering = ['title']
        verbose_name = "دوره"

    def get_absolute_url(self):
        return reverse('course:course_detail',args=[self.course_slug])  

    def __str__(self):
        return f"{self.course_type} - {self.title}."

    def save(self, *args, **kwargs):
        self.course_slug = slugify(self.title_slug)
        self.course_slug += f"-{get_random_string(10)}"
       
        super().save(*args, **kwargs)

    

     

class Section(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    
    def __str__(self):
        return f"{self.title} - {self.course}"


class Lecture(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.FileField(upload_to="course_video/", blank=True)
    video = models.FileField(upload_to="course_video/")
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True)
    lecture_slug = models.SlugField(default="-")
    

           
    
    def save(self, *args, **kwargs):
        self.course = self.section.course
        self.lecture_slug = slugify(self.title)
        self.lecture_slug += f"-{get_random_string(10)}"
        super().save(*args, **kwargs)
       

    def __str__(self):
        return f"{self.id} - {self.title} - {self.section}"

