from django import forms

from.models import Order

from crispy_forms.helper import FormHelper





class OrderForm(forms.ModelForm):
    is_apply = forms.BooleanField()

    class Meta:
        model = Order
        fields = ['user_name', 'phone', 'is_apply']
        exclude = ('customer',)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['is_apply'].help_text = "من قوانین سایت را قبول دارم"
        self.fields['is_apply'].label = ''
      
       # self.fields['is_apply'].widget.attrs['checked'] = True

    



    

       