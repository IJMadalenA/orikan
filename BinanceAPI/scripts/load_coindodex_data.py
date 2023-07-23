import os
import django

# Establece la variable de entorno para la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orikan.settings')
django.setup()

from csv import DictReader
from datetime import datetime
from BinanceAPI.models.symbol_model import Symbol
from BinanceAPI.models.candlestick_model import Candlestick


def load_candlestick_data_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as csvfile:
        reader = DictReader(csvfile)
        for row in reader:
            print("Row:")
            print(row, "\n")
            # Obtén los valores de cada fila en el archivo CSV
            date_start = datetime.strptime(row['Start'], '%Y-%m-%d')
            date_end = datetime.strptime(row['End'], '%Y-%m-%d')
            open_price = float(row['Open'])
            high_price = float(row['High'])
            low_price = float(row['Low'])
            close_price = float(row['Close'])
            volume = float(row['Volume']) * 1000000000
            market_cap = float(row['Market Cap']) * 1000000000

            # Obtén o crea el objeto Symbol asociado al par de trading
            symbol_name = 'BTCUSD'  # Reemplaza con el nombre del símbolo correspondiente
            symbol, _ = Symbol.objects.get_or_create(symbol=symbol_name)

            # Crea una nueva instancia de Candlestick con los valores obtenidos
            candlestick = Candlestick(
                symbol=symbol,
                time_frame='1d',
                open_time=date_start,
                close_time=date_end,
                open_price=open_price,
                high_price=high_price,
                low_price=low_price,
                close_price=close_price,
                volume=volume,
                market_cap=market_cap
            )

            try:
                candlestick.full_clean()  # Valida los campos del modelo
                candlestick.save()  # Guarda la instancia en la base de datos
            except Exception as e:
                print(f"Error al guardar Candlestick: {e}")

# Llama a la función para cargar los datos desde el archivo CSV
file_path = './BinanceAPI/data_set/CoinCodex_BTC-ETH_DAILY_2010-07-18_2023-07-05.csv'

load_candlestick_data_from_csv(file_path)
