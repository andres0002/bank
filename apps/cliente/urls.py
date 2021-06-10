from django.conf.urls import url
from apps.cliente.views import PerfilCliente
from apps.cliente.views import ListadoMovimientos
from apps.cliente.views import ListadoCuentas
from apps.cliente.views import ListadoCuentasReporte
from apps.cliente.views import ListadoMovimientosReporte
from apps.cliente.views import ListadoMovimientosReporteByDate
from apps.cliente.views import ListadoMovimientosReporteByFecha
from apps.cliente.views import VisualizarCuenta
from apps.cliente.views import VisualizarMovimiento
from apps.cliente.views import Deposito
from apps.cliente.views import Retiro

app_name = 'cliente'

urlpatterns = [
    url(r'^perfil-cliente/', PerfilCliente.as_view(), name='perfil_cliente'),
    url(r'^listar-movimientos/', ListadoMovimientos.as_view(), name='listar_movimientos'),
    url(r'^listar-cuentas/', ListadoCuentas.as_view(), name='listar_cuentas'),

    url(r'^listar-movimientos-reporte/', ListadoMovimientosReporte.as_view(), name='listar_movimientos_reporte'),
    url(r'^listar-cuentas-reporte/', ListadoCuentasReporte.as_view(), name='listar_cuentas_reporte'),
    url(r'^listar-movimientos-by-fecha/(?P<id_usr>\w+)', ListadoMovimientosReporteByDate.as_view(), name='listar_movimientos_by_fecha'),
    url(r'^listar-movimientos-por-fecha/', ListadoMovimientosReporteByFecha.as_view(), name='listar_movimientos_por_fecha'),

    url(r'^visualizar-cuentas/(?P<id_codigo_cuenta>\w+)', VisualizarCuenta.as_view(), name='visualizar_cuenta'),
    url(r'^visualizar-movimientos/(?P<id_movimiento>\w+)', VisualizarMovimiento.as_view(), name='visualizar_movimientos'),
    url(r'^realizar-deposito/(?P<id_cuenta>\w+)', Deposito.as_view(), name='realizar_deposito'),
    url(r'^realizar-retiro/(?P<id_cuenta>\w+)', Retiro.as_view(), name='realizar_retiro'),

]
