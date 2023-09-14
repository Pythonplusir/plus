from django.urls import path

from.views import LandView

app_name= "land"
urlpatterns = [
    path("", LandView.as_view(), name="landing"),
    
       
]

