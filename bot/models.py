from django.db import models


class Block(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя блока', unique=True)


class ObjectPart(models.Model):
    class Type(models.IntegerChoices):
        TEXT = 1
        IMAGE = 2
        VIDEO = 3
        PAUSE = 4
        BUTTON = 5
        FORMTEXT = 6
        FORMORDER = 7

    name = models.CharField(max_length=100, verbose_name='название')
    height = models.IntegerField(verbose_name='высота')
    width = models.IntegerField(verbose_name='ширина')
    owner = models.ForeignKey(to=Block, on_delete=models.CASCADE)
    order_number = models.IntegerField(verbose_name='порядковый номер')
    data = models.TextField(verbose_name='данные', blank=True)
    type = models.SmallIntegerField(choices=Type.choices, verbose_name='тип', blank=True)
