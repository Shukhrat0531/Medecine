from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['phone_number', 'delivery_address']
        labels = {
            'phone_number': 'Номер телефона',
            'delivery_address': 'Адрес доставки',
        }