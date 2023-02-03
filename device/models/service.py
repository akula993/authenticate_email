from django.db import models

class Status(models.TextChoices):
    """Статусы для заявок"""
    CREATED = 'CREATED', 'Новая заявка от клиента'
    CONFIRMED = 'CONFIRMED', 'Подтверждена техником'
    READY_TO_WORK = 'READY_TO_WORK', 'Готова к работе'
    PROGRESS = 'PROGRESS', 'В работе'
    VERIFICATION = 'VERIFICATION', 'Ремонт выполнен'
    TESTS = 'TESTS', 'На тестировании'
    RE_REPAIR = 'RE_REPAIR', 'На доработку'
class Service(models.Model):
    users = models.ManyToManyField(to='users.User', related_name='service', verbose_name='Учасники заявки')
    description = models.TextField(verbose_name='Описание заявки')
    status = models.CharField(max_length=20, choices=Status.choices)
    time_to_device = models.DateTimeField(verbose_name='Время обслуживаня', null=True, blank=True)
    address_to_service = models.ForeignKey('Address', related_name='address', on_delete=models.PROTECT,
                                           verbose_name='Адрес', null=True, blank=True)
    type_of_service = models.ForeignKey('TypesService', related_name='types_service',
                                        on_delete=models.PROTECT, verbose_name='Тип обслуживания', null=True,
                                        blank=True)
