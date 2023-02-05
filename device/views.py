from django.shortcuts import render
from django.views.generic import ListView

from device.models import Address


class HomeListView(ListView):
    model = Address
    template_name = 'device/home.html'
    context_object_name = 'address'
