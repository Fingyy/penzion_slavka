from django import forms

from penzion.models import RoomType, Order


class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
