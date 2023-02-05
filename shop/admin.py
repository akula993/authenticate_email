from django.contrib import admin
from django.template.defaultfilters import slugify

from shop.models import Product, Gallery


class GalleryInline(admin.StackedInline):
    model = Gallery
    exclude = ['slug', ]
    readonly_fields = ('slug',)
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.product.title, self.image)
    #     super(Gallery, self).save(*args, **kwargs)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (GalleryInline,)

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    exclude = ['slug', ]
    readonly_fields = ('slug',)
    # pass