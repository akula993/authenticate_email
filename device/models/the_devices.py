from django.db import models

from device.models.address import Address


class Status(models.TextChoices):
    """Статусы для заявок"""
    CREATED = 'CREATED', 'Новая заявка от директора'
    CONFIRMED = 'CONFIRMED', 'Подтверждена менеджером'
    PROGRESS = 'PROGRESS', 'В работе'
    COMPLETED = 'VERIFICATION', 'Выполнена техником'
    TESTS = 'TESTS', 'Оплата'


class Service(models.Model):
    """ Обслуживание """
    users = models.ManyToManyField(to='users.User', related_name='service', verbose_name='Учасники заявки')
    description = models.TextField(verbose_name='Описание заявки', blank=True, null=True)
    status = models.CharField(max_length=20, choices=Status.choices)
    time_to_device = models.DateTimeField(verbose_name='Время обслуживанья', null=True, blank=True)
    address_to_service = models.ForeignKey('Address', on_delete=models.SET_DEFAULT, related_name='device',
                                           default=Address.get_default_pk, verbose_name='Адрес', null=True, blank=True)
    type_of_service = models.ForeignKey('TypesService', related_name='types_service',
                                        on_delete=models.PROTECT, verbose_name='Тип обслуживания', null=True,
                                        blank=True)
