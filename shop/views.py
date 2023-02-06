from django.shortcuts import render
from django.views.generic import ListView, DetailView

from shop.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'shop/product/home.html'
    context_object_name = 'product'
    # ordering = ('-publish',)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'article_detail.html'