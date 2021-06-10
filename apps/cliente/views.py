# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.base import View
from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from apps.SenaSoftApp.models import Cliente
from apps.SenaSoftApp.models import Cuenta
from apps.SenaSoftApp.models import Movimiento
from apps.SenaSoftApp.forms import ClienteForm
from apps.administrador.views import ListadoClientes
from apps.SenaSoftApp.forms import CuentaForm
from apps.SenaSoftApp.forms import MovimientoForm

# Create your views here.

class PerfilCliente(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'cliente/perfil_cliente.html'
    form_class = ClienteForm

    def get(self, request):
        try:
            datos_usuario = Cliente.objects.get(usuid=request.user.pk)
            form = self.form_class(instance=datos_usuario)
            return render(request, self.template_name, {'form': form})

        except Cliente.DoesNotExist:
            return render(request, "pages-404.html")

    def post(self, request):
        try:
            datos_usuario = Cliente.objects.get(usuid=request.user.pk)
            form = self.form_class(request.POST, instance=datos_usuario)

            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'El Perfil se modificó correctamente')
            else:
                messages.add_message(request, messages.ERROR, 'El Perfil no se pudo modificar')

            return self.get(request)

        except Cliente.DoesNotExist:
            return render(request, "pages-404.html")

class ListadoCuentas(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'cliente/listar_cuentas.html'
    form_class = CuentaForm

    def get(self, request):
        datos_usuario = Cliente.objects.get(usuid=request.user.pk)
        lista_cuentas = Cuenta.objects.filter(cliente=datos_usuario.pk)
        return render(request, self.template_name, {'cuentas': lista_cuentas})

class ListadoCuentasReporte(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'cliente/listar_cuentas_reporte.html'
    form_class = CuentaForm

    def get(self, request):
        datos_usuario = Cliente.objects.get(usuid=request.user.pk)
        lista_cuentas = Cuenta.objects.filter(cliente=datos_usuario.pk)
        return render(request, self.template_name, {'cuentas': lista_cuentas})

class ListadoMovimientos(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'cliente/listar_movimientos.html'
    form_class = MovimientoForm

    def get(self, request):
        datos_usuario = Cliente.objects.get(usuid=request.user.pk)
        lista_movimientos = Movimiento.objects.filter(cliente=datos_usuario.pk)
        return render(request, self.template_name, {'movimientos': lista_movimientos, 'user': datos_usuario})

class ListadoMovimientosReporte(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'cliente/listar_movimientos_reporte.html'
    form_class = MovimientoForm

    def get(self, request):
        datos_usuario = Cliente.objects.get(usuid=request.user.pk)
        lista_movimientos = Movimiento.objects.filter(cliente=datos_usuario.pk)
        return render(request, self.template_name, {'movimientos': lista_movimientos})

class VisualizarCuenta(LoginRequiredMixin, View):
    login_url = '/'
    form_class = CuentaForm
    template_name = 'cliente/visualizar_cuenta.html'

    def get(self, request, id_codigo_cuenta):
        codigo = Cuenta.objects.get(codigo_cuenta=id_codigo_cuenta)
        form = self.form_class(instance=codigo)
        return render(request, self.template_name, {'form': form})

class VisualizarMovimiento(LoginRequiredMixin, View):
    login_url = '/'
    form_class = MovimientoForm
    template_name = 'cliente/visualizar_movimientos.html'

    def get(self, request, id_movimiento):
        codigo = Movimiento.objects.get(id_movimiento=id_movimiento)
        form = self.form_class(instance=codigo)
        return render(request, self.template_name, {'form': form})

class Retiro(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'cliente/realizar_retiro.html'

    def get(self, request, id_cuenta):
        cuenta = Cuenta.objects.get(codigo_cuenta=id_cuenta)
        return render(request, 'cliente/realizar_retiro.html')

    def post(self, request, id_cuenta):
        try:
            cliente = Cliente.objects.get(usuid=request.user.pk)
            cuenta = Cuenta.objects.get(codigo_cuenta=id_cuenta)
            fecha = datetime.now()
            fecha_formato = "%s-%s-%s" % (fecha.year, fecha.month, fecha.day)
            saldo_retiro = cuenta.saldo - int(request.POST.get('retiro_saldo', 0))
            if saldo_retiro > 15000:
                cuenta.saldo = saldo_retiro
                cuenta.save()
                retiro = Movimiento(
                    cliente=cliente,
                    codigo_cuenta=cuenta,
                    fecha=fecha_formato,
                    tipo="RET",
                    saldo=saldo_retiro
                )
                retiro.save()
                messages.add_message(request, messages.INFO, "La transacion ha sido exitosa(Retiro)")
                lista = ListadoMovimientos()
                return lista.get(request)

            else:
                messages.add_message(request, messages.ERROR, 'El saldo minimo que debe de tener en la cuenta es de $15000')
        except Cuenta.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'La cuenta no existe')

        except Cliente.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'El cliente no existe')

class Deposito(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'cliente/realizar_deposito.html'

    def get(self, request, id_cuenta):
        cuenta = Cuenta.objects.get(codigo_cuenta=id_cuenta)
        return render(request, 'cliente/realizar_deposito.html')

    def post(self, request, id_cuenta):
        try:
            cliente = Cliente.objects.get(usuid=request.user.pk)
            cuenta = Cuenta.objects.get(codigo_cuenta=id_cuenta)
            fecha = datetime.now()
            fecha_formato = "%s-%s-%s" % (fecha.year, fecha.month, fecha.day)
            saldo_deposito = cuenta.saldo + int(request.POST.get('deposito_saldo', 0))

            cuenta.saldo = saldo_deposito
            cuenta.save()

            deposito = Movimiento(
                cliente=cliente,
                codigo_cuenta=cuenta,
                fecha=fecha_formato,
                saldo=saldo_deposito,
                tipo="DEP"
            )

            deposito.save()
            messages.add_message(request, messages.INFO, 'La trasacion ha sido exitosa(Deposito)')
            lista = ListadoMovimientos()
            return lista.get(request)

        except Cuenta.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'La cuenta no existe')

        except Cliente.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'El cliente no existe')

class ListadoMovimientosReporteByDate(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'cliente/listar_movimientos_by_fecha.html'

    def get(self, request, id_usr):
        return render(request, self.template_name)

    def post(self, request, id_usr):
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        s = Cliente.objects.get(usuid=id_usr)
        lista_movimientos = Movimiento.objects.filter(cliente=s, fecha__gte=fecha_inicio, fecha__lte=fecha_fin)
        classmuestradatos = ListadoMovimientosReporteByFecha()
        return classmuestradatos.get(request, lista_movimientos, id_usr)

class ListadoMovimientosReporteByFecha(LoginRequiredMixin, View):
    template_name = 'cliente/listar_movimientos_por_fecha.html'
    def get(self, request, lista_movimientos, id_usr):
        s = Cliente.objects.get(usuid=id_usr)
        return render(request, self.template_name, {'movimientos': lista_movimientos, 'user': s})
