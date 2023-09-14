from django.contrib import admin

# Register your models here.
from django.contrib import admin


from.models import User
from.models import Order
from.models import Invoice
from.models import Transaction



from .import models
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id' , 'customer' , 'order_date',)



class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id' , 'invoice' , 'amount' , 'transaction_date' , 'status',)

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id' , 'order',) 


admin.site.register(models.Order , OrderAdmin)
admin.site.register(models.Invoice , InvoiceAdmin)
admin.site.register(models.Transaction , TransactionAdmin)









from django.contrib.auth import get_user_model
from django.http import HttpResponse
import csv, datetime

User = get_user_model()

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;' 'filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)

    return response

export_to_csv.short_description = 'Export to CSV'  #short description

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    '''
    Registers the action in your model admin
    '''
    actions = [export_to_csv] 



"""
>>> from django.contrib.auth.models import User
>>> with open('myfile.csv', 'w') as csv:
...     for user in User.objects.all():
...         d = '%s, %s, %s,\n' % (user.username, user.last_name, user.first_name)
...         csv.write(d)
"""