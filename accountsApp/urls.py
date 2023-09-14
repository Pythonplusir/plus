from django.urls import path
from .import views

app_name = "askes"


urlpatterns = [   
    path("order/created/", views.order_create, name="order_create"), 
    path('to-bank/', views.to_bank, name='to_bank'), 
    path('<int:user_id>/<str:username>/', views.myprofile, name="myprofile"), 
       
]