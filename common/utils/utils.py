# -*- coding: utf-8 -*-
import datetime
import random
import re
import uuid
from config.settings import PAGINATION_PAGE_SIZE

from rest_framework import exceptions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Permission
from django.core.exceptions import MultipleObjectsReturned
from django.http import Http404
from django.contrib.auth.models import Group


MAX_SIZE_IMAGE = 10 * 1024 * 1024
MAX_SIZE_DOC = 50 * 1024 * 1024

G_ADMINISTRADOR = "Administrators"

ALLOWED_TYPE_IMAGE = [
    "image/png",
    "image/jpeg"
]

ALLOWED_TYPE_DOC = [
    "text/plain",
    "application/pdf",
    "application/msword",
    "application/vnd.oasis.opendocument.text"
]

CARACTERES_EXTRANOS = "!#$%^&*()[]{};:,./<>?\|`~-=_+"


def get_uuid(length: int = 30):
    uid = str(uuid.uuid4().hex)
    if length <= 0:
        token = uid
    else:
        token = uid[:length]
    return token


def get_random_token():
    token = random.randint(100000, 999999)
    return str(token)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = PAGINATION_PAGE_SIZE
    page_size_query_param = 'page_size'


    def get_paginated_response(self, data):
        if not self.page.has_next():
            next = None
        else:
            next = self.page.next_page_number()

        if not self.page.has_previous():
            previous = None
        else:
            previous = self.page.previous_page_number()

        return Response({
            'count': self.page.paginator.count,
            'next': next,
            'previous': previous,
            'results': data
        })


def get_page_page_size(page, page_size):
    if page is not None:
        page = int(page)
    else:
        page = 0

    if page_size is not None:
        page_size = int(page_size)
    else:
        page_size = PAGINATION_PAGE_SIZE

    return page, page_size


def get_inicio(page, page_size):
    if page == 0:
        inicio = 0
    else:
        inicio = (page - 1) * page_size
    return inicio


# funcion que devuelve el siguiente para el paginado
def get_proximo(page, page_size, cantidad):
    page, page_size = get_page_page_size(page, page_size)
    inicio = get_inicio(page, page_size)

    proximo_inicio = inicio + page_size

    if proximo_inicio >= cantidad:
        # proximo = 'null'
        proximo = None
    else:
        proximo = page + 1
    return proximo


# funcion que devuelve el anterior para el paginado
def get_anterior(page, page_size):
    page, page_size = get_page_page_size(page, page_size)
    inicio = get_inicio(page, page_size)

    anterior_inicio = inicio - page_size

    if anterior_inicio < 0:
        # anterior = 'null'
        anterior = None
    else:
        anterior = page - 1
    return anterior


def devolver_lista_permisos(lista, llave, con_es):
    lista_permisos = []

    for item in lista:
        perm = {}

        if con_es:
            perm = item[llave]
        else:
            # perm = item.name
            perm['id'] = item.id
            perm['name'] = item.name
            perm['codename'] = item.codename
        lista_permisos.append(perm)
    return lista_permisos


def convertir_bool(key, valor):
    if valor is not None:
        if valor == 'True' or valor == 'true':
            valor = True
        elif valor == 'False' or valor == 'false':
            valor = False
        elif not valor is True or not valor is False:
            raise exceptions.ValidationError(detail='Formato de parámetro ' + key + ' incorrecto')
    return valor


def paginar(page, page_size, count, lista_datos):
    resultado = {}

    page, page_size = get_page_page_size(page, page_size)
    inicio = get_inicio(page, page_size)

    # if count == 0:
    #     return resultado
    if inicio >= count and count != 0:
        resultado['detail'] = "Invalid page."
    else:
        resultado['results'] = lista_datos
        resultado['count'] = count

        proximo = get_proximo(page, page_size, count)
        resultado['next'] = proximo

        anterior = get_anterior(page, page_size)
        resultado['previous'] = anterior
    return resultado


def validar_fecha(key, value, formato):
    # formato_fecha = "%Y-%m-%d %H:%M:%S.%f"
    try:
        value = datetime.datetime.strptime(value, formato)
    except ValueError as e:
        raise exceptions.ValidationError(detail="Formato de parámetro '" + key + "' incorrecto")
    return value


def validar_rango_fecha(fecha, fecha_inicio, fecha_fin):
    formato_fecha = "%Y-%m-%d"

    if fecha is not None:
        fecha = validar_fecha('fecha', fecha, formato_fecha)
    elif fecha_inicio is not None and fecha_fin is not None:
        fecha_inicio = validar_fecha('fecha_inicio', fecha_inicio, formato_fecha)
        fecha_fin = validar_fecha('fecha_fin', fecha_fin, formato_fecha)

        if fecha_inicio == fecha_fin:
            raise exceptions.ValidationError(detail="La fecha inicio y la fecha fin no pueden ser iguales")
        elif fecha_inicio > fecha_fin:
            raise exceptions.ValidationError(detail="La fecha inicio debe ser menor que la fecha fin")
    elif fecha_inicio is not None:
        fecha_inicio = validar_fecha('fecha_inicio', fecha_inicio, formato_fecha)
    elif fecha_fin is not None:
        fecha_fin = validar_fecha('fecha_fin', fecha_fin, formato_fecha)


def has_permission(request, view, model_name=None):
    usuario = request.user
    action = view.action

    if not model_name:
        try:
            model_name = view.queryset.model._meta.model_name
        except Exception:
            try:
                model_name = view.document.Django.model._meta.model_name
            except Exception:
                model_name = view.basename

    if action == "create":
        action = "add"
    elif action == "update" or action == "partial_update":
        action = "change"
    elif action == "destroy":
        action = "delete"
    elif action == "list":
        action = "view"

    if action is None:
        method = request._request.method
        if method == "GET":
            action = "list"
        elif method == "POST":
            action = "add"
        elif method == "PATCH" or method == "PUT":
            action = "change"
        elif method == "DELETE":
            action = "delete"

    code_name = action + "_" + model_name

    try:
        permission = get_object_or_404(Permission, codename=code_name)
    except MultipleObjectsReturned:
        raise exceptions.APIException(detail='Existen varios permisos con el mismo code_name')
    except Http404:
        raise exceptions.NotAuthenticated(detail='Usted no tiene permiso para realizar esta acción.')
    except Exception as ex:
        raise exceptions.NotAuthenticated(detail='Error en permisos: {}'.format(ex))

    for grupo in usuario.groups.all():
        permisos = grupo.permissions.all()
        if permission in permisos:
            return True
    return False

def pertenece_grupo(usuario, nombre_grupo):
    if nombre_grupo is None or usuario is None or usuario.is_anonymous:
        return False
    else:

        try:
            grupo = Group.objects.get(name=nombre_grupo)
        except Exception:
            return False

        if grupo in usuario.groups.all():
            return True
        else:
            return False


def check_perm_set_action(self, request, instance, action):
    action_old = self.action
    self.action = action
    self.check_object_permissions(request, instance)
    self.action = action_old
    return self


def validate_phone(phone):
    rexp = '^\+[\d]{10,11}$'
    if not re.search(rexp, phone):
        raise exceptions.ValidationError(detail={"error": ['Número de teléfono inválido.']})


def generar_slug(string: str, fecha: str):
    if fecha == '' or fecha is None:
        fecha = datetime.datetime.now()
    fecha = fecha.strftime("%Y-%m-%d %H-%M-%S-%f")
    return string.nombre + ' ' + fecha

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    else:
        return request.META.get('REMOTE_ADDR')
