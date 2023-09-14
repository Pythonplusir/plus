from django.urls import path
from .import views

app_name = "course"

urlpatterns = [
    path("", views.courselist, name="list_course"),
    path('tag/<slug:tag_slug>', views.courselist, name='course_list_by_tag'),   
    path('course_detail/<str:slug>', views.course_detail, name='course_detail'),
    
   
]