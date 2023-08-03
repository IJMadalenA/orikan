# Path: BinanceAPI/admin/ticker_admin.py

import logging
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from BinanceAPI.models.ticker_model import Ticker
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash

logger = logging.getLogger(__name__)

# Crear la aplicación Dash
app = DjangoDash("TickerApp")

# Configurar el layout del gráfico de velas
app.layout = html.Div(
    children=[
        dcc.Graph(id="candlestick-graph"),
    ]
)


@app.callback(
    Output("candlestick-graph", "figure"),
    Input("url", "pathname")  # Podrías usar algún otro Input para refrescar el gráfico
)
def update_graph(pathname):
    # Aquí debes escribir el código para obtener los datos necesarios para el gráfico
    # Por ejemplo, puedes obtener los datos de Ticker usando una consulta a la base de datos.
    # Supongamos que los datos están almacenados en una lista de diccionarios llamada "data".

    # Ejemplo de código para crear un gráfico de velas utilizando Plotly:
    figure = {
        "data": [
            {
                "x": [data_point["open_time"] for data_point in data],
                "open": [data_point["open_price"] for data_point in data],
                "high": [data_point["high_price"] for data_point in data],
                "low": [data_point["low_price"] for data_point in data],
                "close": [data_point["close_price"] for data_point in data],
                "type": "candlestick",
                "name": "Velas",
            }
        ],
        "layout": {
            "title": "Gráfico de Velas",
        },
    }

    return figure


# Registramos el modelo Ticker en el admin de Django
@admin.register(Ticker)
class TickerAdmin(ModelAdmin):
    # Campos a mostrar en la lista.
    list_display = [
        "symbol",
        "price_change",
        "price_change_percent",
        "open_price",
        "close_price",
        "high_price",
        "low_price",
        "volume",
    ]
    # Campos de solo lectura.
    readonly_fields = [
        "symbol",
        "price_change",
        "price_change_percent",
        "weighted_avg_price",
        "prev_close_price",
        "last_price",
        "bid_price",
        "ask_price",
        "open_price",
        "close_price",
        "high_price",
        "low_price",
        "volume",
        "open_time",
        "close_time",
        "first_trade_id",
        "last_trade_id",
        "trade_count",
        "maker_commission",
        "taker_commission",
        "updated_at",
    ]
    # Ordenamiento.
    ordering = ["-updated_at", "-symbol"]
    # Campos de filtrado.
    list_filter = [
        "symbol",
        "created_at",
        "updated_at",
    ]
    # Campos de búsqueda.
    search_fields = [
        "symbol",
        "created_at",
        "updated_at",
    ]


# Definimos la función get_model_perms para evitar que Django genere los enlaces de cambio y eliminación
# para el modelo Ticker. Solo queremos visualizar el gráfico Dash.
def get_model_perms(self, request):
    return {}


# Asignamos la función get_model_perms al admin de Ticker
TickerAdmin.get_model_perms = get_model_perms
