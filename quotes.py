from auth import c
from tda.client import Client
from input import futures_month
import time
import TypeError

def get_price_data(symbol):
    r = c.get_price_history(symbol,
            period_type=client.Client.PriceHistory.PeriodType.YEAR,
            period=client.Client.PriceHistory.Period.TWENTY_YEARS,
            frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
            frequency=client.Client.PriceHistory.Frequency.DAILY)
    assert r.status_code == 200, r.raise_for_status()
    print(json.dumps(r.json(), indent=4))
    return r.json()

def get_quote(symbol, asset_type = 'None', time_input = time.localtime()):
    if asset_type == 'Futures':
        for i in futures_months:
            try:
                current_year = time.strftime('%y', time_input)
                full_quote = symbol+i+current_year
                r = c.get_quotes(full_quote)
                assert r.status_code == 200, r.raise_for_status()
                json.dump(r.json(), fp = '/dumps/'+full_quote)
                print(json.dumps(r.json(), indent=4))
                output = r.json()
            except TypeError:
                pass
    else:
            pass
    return output


def get_bid_ask_last_mark(symbol):
    bid, ask, last, mark = 0.00, 0.00, 0.00, 0.00
    return bid, ask, last, mark


def get_option_quote(symbol, strike, expiration, put_call, in_session = True):
    """
    expirations: Valid ISO-8601 formats are:
    yyyy-MM-dd and yyyy-MM-dd'T'HH:mm:ssz.'
    """
    chain = c.get_option_chain(symbol = symbol, contract_type = put_call, strike = strike, strike_from_date = expiration, strike_to_date = expiration)
    dict = json.loads(chain)
    if in_session == True:
        quote = chain['mark']
    else:
        quote = chain['last']
    return quote
