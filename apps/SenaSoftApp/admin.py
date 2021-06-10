# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from apps.SenaSoftApp.models import Ciudad
from apps.SenaSoftApp.models import Cliente
from apps.SenaSoftApp.models import Cuenta
from apps.SenaSoftApp.models import Movimiento

admin.site.register(Ciudad)
admin.site.register(Cliente)
admin.site.register(Cuenta)
admin.site.register(Movimiento)
