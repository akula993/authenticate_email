from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from geopy import Nominatim

geolocator = Nominatim(user_agent="VEND")

class Address(models.Model):
    """Адресса в которых стоят аппараты"""
    region = models.CharField(max_length=100, verbose_name='Регион', default='')
    city =models.CharField(max_length=100, verbose_name='город', default='')
    street = models.CharField(max_length=100, verbose_name='улица', default='')
    house = models.CharField(max_length=100, verbose_name='дом', default='')
    organization = models.CharField(max_length=100, verbose_name='организация', blank=True, null=True,)
    created_at = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    to_rent = models.DecimalField('Аренда', max_digits=10, decimal_places=2, blank=True, null=True,)
    slug = models.SlugField(max_length=200, blank=True, null=True, )

    def __str__(self):
        return f'{self.region}, {self.city}, {self.street}, {self.house}, {self.organization}'
    def geo(self):
        location = geolocator.geocode(f'{self.region},{self.city},{self.street}, {self.house}')
        return f'{location.longitude},' + f'{location.latitude}'
    def geo_navi(self):
        location = geolocator.geocode(f'{self.region},{self.city},{self.street}, {self.house}')
        return f'lat_to={location.latitude}' + f'&lon_to={location.longitude}'
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


    def get_absolute_url(self):
        return reverse('address_detail', kwargs={'address': self.slug})

