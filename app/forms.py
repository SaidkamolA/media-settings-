from django import forms
from .models import Product, Review

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'slug', 'description', 'price', 'picture']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'content', 'rating']
