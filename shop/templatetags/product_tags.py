from django import template

from shop.models import Product

register = template.Library()


@register.simple_tag
def product_tag(count=3):
    product = Product.published.order_by('-publish')[:count]
    return product


@register.inclusion_tag('shop/product/.inc/best_products.html')
def show_the_best_products(count=6):
    latest_product = Product.published.order_by('-view')[:count]
    return {'latest_product': latest_product}
@register.inclusion_tag('shop/product/.inc/new_arrivals.html')
def show_latest_product(count=14):
    latest_product = Product.published.order_by('-publish')[:count]
    return {'latest_product': latest_product}