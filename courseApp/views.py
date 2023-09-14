from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import *
from taggit.models import Tag
from django.db.models import Count



from django.contrib.contenttypes.models import ContentType



def courselist(request, tag_slug=None):
    #course = Course.objects.all() 
    course = Course.objects.filter(id__in=[1, 2, 3]) 
    free_course = Course.objects.filter(course_type="FREE")
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        course = course.filter(tags__in=[tag])      
             
    context = {             
              "course": course,
              'free':free_course,                          
              'tag': tag,
             
            }
    return render (request, 'mycourse/course_list.html',context) 




def course_detail(request, slug):           
    course = Course.objects.filter(course_slug=slug).first()
    section = Section.objects.filter(course=course)
    lecture = Lecture.objects.filter(course=course)

    course_tags_ids =course.tags.values_list('id', flat=True)
    similar_course = Course.objects.filter(tags__in=course_tags_ids).exclude(id=course.id)
    similar_course = similar_course.annotate(same_tags=Count('tags')).order_by('-same_tags')[:4]
       
    
    context ={
       
        "course":course,
        "section":section,
        "lecture":lecture,     
        'similar_course':similar_course,     

    }
    
    return render(request, 'mycourse/course_detail.html', context)