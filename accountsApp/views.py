from django.views import generic, View
from django.core.mail import send_mail, send_mass_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from.forms import OrderForm
from .models import Order
from .models import Invoice
from .models import Transaction
from decimal import Decimal
import zeep
from zeep import Client

from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings



from django.contrib.auth import get_user_model
User = get_user_model()



@login_required()
def myprofile(request, user_id, username):
    
    # Render profile page
    user_profile = User.objects.filter(id=user_id)
    
    return render(request, "profile.html", {
        "user_profile": user_profile,
        
    })






@login_required
def order_create(request):
    if request.method== "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user     
            order.email =request.user.email       
            order.save()
            request.session['order_id'] = order.id
            
            return redirect('askes:to_bank')
    else:
        form = OrderForm()
    return render(request,
                  'order_created.html',
                  {'form': form})



def to_bank(request , order_id):
    order_id = request.session.get("order_id")
    order = get_object_or_404(Order, id=order_id)
    amount  =200000       
   
    client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
    callbackUrl = 'http://127.0.0.1:80000/callback/'
    mobile = order.phone # mobile
    user = order.customer.email    # email
    email = user
    description = 'Test'
    merchant = '***********************'
    result = client.service.PaymentRequest(merchant, amount, description, email, mobile, callbackUrl)

    if result.Status == 100 and len(result.Authority) == 36:
        Invoice.objects.crate(order = order ,
                                     authority = result.Authority)
        return redirect('https://www.zarinpal.com/pg/StartPay/' + result.Authority)
    else :
        return HttpResponse('Error Code' + str(result.Status))


def callback(request):
    if request.GET.get('Status') == 'OK':
        authority = request.GET.get('Authority')
        invoice = get_object_or_404(Invoice, authority=authority)
        amount = 20000
        
        order_invoice = invoice.order              
        result = Client.service.PaymentVerification(merchant, authority, amount)
        order_id = request.session.get('order_id')
        order = get_object_or_404(Order, id = order_id)
        email = order.email
        #user = order.customer.COURSE_TYPE == "FREE"

        if result.Status == 100:
            order.paid = True                     
            order.customer.course_type== "FREE"
            order.save()
            subject = "hello, " + (email)
            message = 'Please, find attached the invoice for your recent purchase.'
            email = EmailMessage(subject,
                                 message,
                                 'admin@myshop.com',
                                 [order.email])
            email.send()
       
            return render(request, 'callback.html', {'invoice': invoice})
        else:
            return HttpResponse('error ' + str(result.Status))
    else:
        return HttpResponse('error')