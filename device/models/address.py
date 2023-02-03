from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Address(models.Model):
    """Адресса в которых стоят аппараты"""
    name = models.CharField(max_length=250, verbose_name='Адресс')
    slug = models.SlugField(max_length=200, blank=True, null=True, )

    created_at = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    to_rent = models.DecimalField('Аренда', max_digits=10, decimal_places=2, blank=True, null=True,)

    @classmethod
    def get_default_pk(cls):
        obj, created = cls.objects.get_or_create(name='Без адреса', slug='no_address', to_rent='0')
        return obj.pk

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Address, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('address_detail', kwargs={'address': self.slug})

