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
    list_display = ('title', 'slug', 'author', 'price', 'status', 'view')
    list_display_links = ('title', 'slug',)
    list_filter = ('publish', 'status')
    list_editable = ('status',)
    search_fields = ('title', 'author',)
    search_help_text = 'Поиск по названию и авторами'
    date_hierarchy = None
    save_as = True
    save_as_continue = True
    save_on_top = True
    exclude = ['slug', 'view']
    readonly_fields = ('slug', 'view')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    exclude = ['slug', ]
    readonly_fields = ('slug',)
    # pass
