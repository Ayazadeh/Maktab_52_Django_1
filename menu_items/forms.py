from django import forms
from django.core.exceptions import ValidationError

from menu_items.models import *





# class CreateMenuItem(forms.Form):
#     name = forms.CharField(max_length=30, validators=[menu_item_validator])
#     price = forms.ModelChoiceField(validators=[price_positive], queryset=Price.objects.all())
#     discount = forms.ModelChoiceField(queryset=Discount.objects.all())
#     image = forms.FileField()
#     category = forms.ModelChoiceField(queryset=Categories.objects.all())

class CreateMenuItem(forms.ModelForm):
    class Meta:
        model = MenuItems
        fields = "__all__"
