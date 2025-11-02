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
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Karel',
                'required': 'required',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Novák',
                'required': 'required',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Hlavní 1',
                'required': 'required',
            }),
            'postal_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '53843',
                'required': 'required',
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Třemošnice',
                'required': 'required',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'karel.novak@email.com',
                'required': 'required',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '731488405',
                'pattern': '[0-9]{9}$',
                'maxlength': '9',
                'inputmode': 'numeric',
                'required': 'required',
            }),
            'arrive_date': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': 'required',
            }),
            'departure_date': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': 'required',
            }),
            'no_of_nights': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'step': '1',
                'placeholder': '0',
                'required': 'required',
            }),
            'no_of_adults': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'step': '1',
                'placeholder': '0',
                'required': 'required',
            }),
            'no_of_kids': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'step': '1',
                'placeholder': '0',
            }),
            'no_of_rooms': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'step': '1',
                'placeholder': '0',
                'required': 'required',
            }),
            'room_type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'vyberte typ pokoje',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
            }),
        }
