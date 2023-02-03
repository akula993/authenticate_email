from django.db import models


class TypesOfService(models.TextChoices):
    """ Роли пользователей """
    WITHDRAWAL = 'WITHDRAWAL', 'Снятие кассы'


class TypesService(models.Model):
    """ Вид обслуживания """
    name = models.CharField(max_length=11, verbose_name='Вид обслуживания', choices=TypesOfService.choices,
                            default=TypesOfService.WITHDRAWAL)

# class Counter(models.Model):
#     types_service = models.F