# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext as _

class RegistroAccion(models.Model):

    # Atributos
    ip = models.TextField(default='')
    accion = models.TextField(default='')
    usuario = models.TextField(default='')
    url = models.TextField(default='')
    fecha = models.DateTimeField(auto_now_add=True)
    tz = models.TextField(default='')
    datos = models.TextField(default='')
    modelo = models.TextField(default='')

    def __str__(self):
        return self.accion

    class Meta:
        verbose_name = _('Registro Accion')
        verbose_name_plural = _('Registro de Acciones')
        app_label = "core"
        ordering = ['fecha']