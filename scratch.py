from portfolio import Portfolio
from strategy import Strategy
from option_class import Option
from asset import Asset
from tdameritrade.auth import c
from datetime import datetime
from tda.client import Client
from data_cleanup.input import data_dict
from pandas import DataFrame
from tdameritrade.quotes import get_quote

start = datetime.strptime('01-01-2021', '%m-%d-%Y')
end = datetime.strptime('01-05-2021', '%m-%d-%Y')
strike = 3700
put_call = Client.Options.ContractType("PUT")
#object = json.dumps(c.get_option_chain('SPY',strike = 350, include_quotes = True,
#    strike_from_date = start, strike_to_date = end).json(), indent=2)
#print(object)
object = c.get_option_chain('$SPX.X',contract_type = put_call, strike = strike, strike_from_date = start, strike_to_date = end).json()

quote = get_quote('/CL',type = 'Futures', time_input = '21')
print(object)
print(type(object))
print(data_dict['Futures']['Bonds'])
