def get_historical_data(self, symbol, start_time, end_time):
    """
    Obtiene datos históricos del símbolo especificado en el rango de tiempo dado.
    Retorna los datos históricos en formato JSON.
    """
    endpoint = '/klines'
    params = {
        'symbol': symbol,
        'interval': '1d',
        'startTime': start_time,
        'endTime': end_time
    }

    response = self._request('GET', endpoint, params)
    return response
