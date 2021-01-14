"""Get Price and Time Series from various sources
@@@brugs_bunny"""

import requests
from pandas import DataFrame
from tdameritrade.quotes import get_price_data

def create_time_series(symbol):
    raw = get_price_data(symbol)

    df = DataFrame(raw)
    return df
