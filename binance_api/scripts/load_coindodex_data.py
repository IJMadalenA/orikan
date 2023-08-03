import os
from _decimal import Decimal

import django
from django.utils import timezone
from csv import DictReader
from datetime import datetime

# Establece la variable de entorno para la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orikan.settings')
django.setup()

from BinanceAPI.models.symbol_model import Symbol
from BinanceAPI.models.ticker_model import Ticker


def load_candlestick_data_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as csvfile:
        reader = DictReader(csvfile)
        for row in reader:

            # Obtén o crea el objeto Symbol asociado al par de trading
            symbol_name = 'BTCUSDT'  # Reemplaza con el nombre del símbolo correspondiente
            symbol = Symbol.objects.get(symbol=symbol_name)

            # Crea una nueva instancia de Candlestick con los valores obtenidos
            ticker = Ticker(
                symbol=symbol,
                time_frame='1d',
                open_time=timezone.make_aware(datetime.strptime(row['Start'], '%Y-%m-%d')),
                close_time=timezone.make_aware(datetime.strptime(row['End'], '%Y-%m-%d')),
                open_price=row['Open'],
                high_price=row['High'],
                low_price=row['Low'],
                close_price=row['Close'],
                volume=row['Volume'],
                market_cap=row['Market Cap'],
            )

            try:
                ticker.full_clean()  # Valida los campos del modelo
                ticker.save()  # Guarda la instancia en la base de datos
            except Exception as e:
                print(f"Error al guardar Ticker: {e}")

# Llama a la función para cargar los datos desde el archivo CSV
file_path = './BinanceAPI/data_set/CoinCodex_BTC-USD_DAILY_2010-07-18_2023-07-05.csv'

load_candlestick_data_from_csv(file_path)
