from django.contrib import admin
from .models import Course, Lecture, Section





class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','course_type', 'price')
    search_fields = ('title',)
    list_filter = ('title',)
    list_per_page = 10
    ordering = ['title']
   
    
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'course',)
    list_per_page = 20
    search_fields = ('title',)
    list_filter = ('course',)
    
class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'section',)      
    search_fields = ('title','section',)
  
    

admin.site.register(Course, CourseAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Lecture, LectureAdmin)
