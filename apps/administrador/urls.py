from django.conf.urls import url
from apps.administrador.views import ListadoClientes
from apps.administrador.views import ListadoClientesReporte
from apps.administrador.views import AdicionarCliente
from apps.administrador.views import AdicionarCuenta
from apps.administrador.views import VisualizarCliente
from apps.administrador.views import ModificarCliente
from apps.administrador.views import BorrarCliente
from apps.administrador.views import VisualizarCuenta
from apps.administrador.views import ModificarCuenta
from apps.administrador.views import BorrarCuenta
from apps.administrador.views import PerfilAdministrador
from apps.administrador.views import ListadoCuentas
from apps.administrador.views import ListadoCuentasReporte
from apps.administrador.views import ListadoMovimientosReporteByDate
from apps.administrador.views import ListadoMovimientosReporteByFecha
from apps.administrador.views import ListadoMovimientos
from apps.administrador.views import ListadoMovimientosGeneral
from apps.administrador.views import ListadoMovimientosReporte
from apps.administrador.views import ListadoCuentasReporteCliente
from apps.administrador.views import VisualizarClienteHipervinculo
from apps.administrador.views import VisualizarClienteCuentaHipervinculo
from apps.administrador.views import VisualizarMovimiento

app_name = 'administrador'

urlpatterns = [
    url(r'^listar-clientes/', ListadoClientes.as_view(), name='listar_clientes'),
    url(r'^listar-clientes-reporte/', ListadoClientesReporte.as_view(), name='listar_clientes_reporte'),
    url(r'^adicionar-cliente/', AdicionarCliente.as_view(), name='adicionar_cliente'),
    url(r'^visualizar-cliente/(?P<id_cliente>\w+)', VisualizarCliente.as_view(), name='visualizar_cliente'),
    url(r'^modificar-cliente/(?P<id_cliente>\w+)', ModificarCliente.as_view(), name='modificar_cliente'),
    url(r'^borrar-cliente/(?P<id_cliente>\w+)', BorrarCliente.as_view(), name='borrar_cliente'),
    url(r'^lista-cuentas/', ListadoCuentas.as_view(), name='listar_cuentas'),
    url(r'^lista-cuentas-reporte/', ListadoCuentasReporte.as_view(), name='listar_cuentas_reporte'),
    url(r'^adicionar-cuenta/', AdicionarCuenta.as_view(), name='adicionar_cuenta'),
    url(r'^visualizar-cuenta/(?P<id_codigo_cuenta>\w+)', VisualizarCuenta.as_view(), name='visualizar_cuenta'),
    url(r'^visualizar-movimiento/(?P<id_movimiento_visualizar>\w+)', VisualizarMovimiento.as_view(), name='visualizar_movimientos'),
    url(r'^modificar-cuenta/(?P<id_codigo_cuenta>\w+)', ModificarCuenta.as_view(), name='modificar_cuenta'),
    url(r'^borrar-cuenta/(?P<id_codigo_cuenta>\w+)', BorrarCuenta.as_view(), name='borrar_cuenta'),
    url(r'^perfil-administrador/', PerfilAdministrador.as_view(), name='perfil_administrador'),

    url(r'^listar-movimientos-by-fecha/(?P<id_cuen>\w+)', ListadoMovimientosReporteByDate.as_view(), name='listar_movimientos_by_fecha'),
    url(r'^listar-movimientos-por-fecha/', ListadoMovimientosReporteByFecha.as_view(), name='listar_movimientos_por_fecha'),
    url(r'^listar-movimientos/', ListadoMovimientos.as_view(), name='listar_movimientos'),
    url(r'^listar-movimientos-general/', ListadoMovimientosGeneral.as_view(), name='listar_movimientos_general'),
    url(r'^listar-movimientos-reporte/', ListadoMovimientosReporte.as_view(), name='listar_movimientos_reporte'),
    url(r'^listar-cuentas-por-cliente/(?P<id_c>\w+)', ListadoCuentasReporteCliente.as_view(), name='listar_cuentas_reporte_cliente'),

    url(r'^visualizar-cliente-hipervinculo/(?P<id_cliente>\w+)', VisualizarClienteHipervinculo.as_view(), name='visualizar_cliente_hipervinculo'),
    url(r'^visualizar-cuenta-cliente-hipervinculo/(?P<id_cliente>\w+)', VisualizarClienteCuentaHipervinculo.as_view(), name='visualizar_cuenta_cliente_hipervinculo'),
]
