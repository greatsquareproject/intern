from django import forms
from .models import products


class ProductForm(forms.ModelForm):#ModelForm-It creates model as form
    class Meta:
        model = products
        fields = "__all__"	#collecting all data from models
