from django import forms
from .models import productdetails


class ProductForm(forms.ModelForm):
    class Meta:
        model = productdetails

        fields = [
            'name',
            'sku',
            'description',
            'status'
        ]

        labels = {
            'name': '',
            'sku': '',
            'description': '',
            'status': ''
        }

        widgets = {
            'name': forms.TextInput(
                attrs={'name': 'name', 'class': 'form-control', 'placeholder': 'Name', }),
            'sku': forms.TextInput(
                attrs={'name': 'sku', 'class': 'form-control', 'placeholder': 'SKU', }),
            'description': forms.TextInput(attrs={'name': 'description', 'class': 'form-control', 'placeholder': 'Description'}),
            'status': forms.Select(
                attrs={'name ': 'status ', 'class ': 'form-control ', 'placeholder ': 'Product Status'}),
        }
