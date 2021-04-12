from datetime import timedelta

from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.core.validators import MaxValueValidator


class Freight(models.Model):
    class Status(models.TextChoices):
        NOT_ASSIGNED = 'not_assigned', _('Not assigned')
        WAITING = 'waiting', _('Waiting')
        IN_DELIVERY_TRANSIT = 'in_delivery_transit', _('In delivery transit')
        TRANSFERING = 'transfering', _('Transfering')
        IN_RECEPTION_TRANSIT = 'in_reception_transit', _('In reception transit')
        DELIVERED = 'delivered', _('Delivered')
        RETURNED = 'returned', _('Returned')

    name = models.CharField(_('name'), max_length=150)
    status = models.CharField(_('status'), max_length=30)
    transfer = models.OneToOneField('companies.Transfer', on_delete=models.CASCADE, null=True)
    is_damaged = models.BooleanField(_('is damaged'), default=False)

    def __str__(self):
        return self.name


class Rule(models.Model):
    coefficient = models.FloatField(_('coefficient'), validators=[MaxValueValidator(1.0)])
    max_value = models.FloatField(_('max value'))
    min_value = models.FloatField(_('min value'))
    possible_deviation = models.FloatField(_('possible deviation'), default=0)
    time_interval = models.DurationField(_('time interval'), default=timedelta(hours=1))
    freight = models.ForeignKey('Freight', on_delete=models.CASCADE, related_name='rules')
    device = models.ForeignKey('devices.Device', on_delete=models.CASCADE, related_name='rules')

    def __str__(self):
        return f'{self.device}({self.freight})'


class State(models.Model):
    value = models.FloatField(_('value'))
    timestamp = models.DateTimeField(_('timestamp'), auto_now_add=True)
    rule = models.ForeignKey('Rule', on_delete=models.CASCADE, related_name='states')

    def __str__(self):
        return f'{self.rule} at {self.timestamp}'



