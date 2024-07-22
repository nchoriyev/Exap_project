from django import forms

from products.models import Product


class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=100, required=False)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'image', 'description', 'value', 'price', 'rating', 'count', 'country_of_origin', 'Quality', 'Check', 'Min_weight', 'Featured_products']


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'image', 'description', 'value', 'price', 'rating', 'count', 'country_of_origin', 'Quality', 'Check', 'Min_weight', 'Featured_products']