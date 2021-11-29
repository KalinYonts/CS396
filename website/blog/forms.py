from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, Product, Sale, Health
from django.forms import widgets, ModelForm, DateInput
from phone_field import PhoneField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class AddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['received_quantity']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ["quantity", "amount_received", "issued_to"]

class AddHealthForm(forms.ModelForm):
    class Meta:
        model = Health
        fields = ('doctor_name', 'phone', 'email', 'prescriptions', 'dose', 'dosetime')


