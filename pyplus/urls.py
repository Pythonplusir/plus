from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
  
  path('accounts/', include('allauth.urls')), 
  path('account/', include('accountsApp.urls', namespace="askes")),
#   path('', include('courseApp.urls', namespace="course")),
#   path('specializations/django/', include('landApp.urls', namespace="land")), 
  
#   path('article/', include('blogApp.urls', namespace="blog")),   
#   path('admin/', admin.site.urls),
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)