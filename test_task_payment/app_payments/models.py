# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class PaymentsFromJson(models.Model):
    class Meta:
        managed = False
        verbose_name = 'Платежи'
        verbose_name_plural = 'Платежи'