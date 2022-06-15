from ast import Or
from dataclasses import field
from turtle import width
from urllib import request

from django.http import HttpRequest
from .models import Order, Service
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['street', 'build', 'home', 'time', 'phone']
        

    