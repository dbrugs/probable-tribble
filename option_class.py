from datetime import datetime
from option_math_brugs.d1_d2 import calc_d1, calc_d2
import option_math_brugs.greeks
#from tdameritrade.grab_data import get_price_data
from option_math_brugs.BS import Calculate_IV_Call_Put
from tdameritrade.quotes import get_option_quote, get_bid_ask_last_mark
import json
from tda.client import Client

class Option:
    def __init__(self, contracts, underlying_ticker, call_put, strike, expiration,):
        self.contracts = contracts
        self.expiration = datetime.strptime(expiration, '%m-%d-%Y')
        #bid/ask/mark/last
        self.price = get_option_quote(underlying_ticker,strike, self.expiration, call_put)
        self.quote = get_bid_ask_last_mark(underlying_ticker)
        self.price_elements = {'bid': self.quote[0], 'ask': self.quote[1],
        'mark': 0.00, 'quoted mark': self.quote[3], 'last': self.quote[2], 'ba_last_avg':0.00}
        #optioninfo
        self.underlying = str(underlying_ticker.upper())
        self.underlying_price = 100.00
        self.call_put = Client.Options.ContractType(call_put.upper())
        self.strike = float(strike)
        self.dte = datetime.today() - self.expiration
        self.seconds_to_exp = (self.dte).total_seconds()
        seconds_per_year = {252 : 20865600,
        270: 22356000, 300: 24840000,360: 29808000,}
        self.time_percentage = {252: self.seconds_to_exp/seconds_per_year[252],
        270: self.seconds_to_exp, 300: self.seconds_to_exp/seconds_per_year[300], 360: self.seconds_to_exp/seconds_per_year[360]}
            ##call_put and moneyness
        if call_put == 'CALL':
            self.BS_IV = Calculate_IV_Call_Put(self.underlying_price, self.strike, r = 0.0001, T = self.time_percentage, Option_Price = self.price, Put_or_Call = "Call")
            if self.underlying_price > self.strike:
                self.itm = True
                self.intrinsic = self.underlying_price - self.strike
                self.extrinsic = self.price - self.intrinsic
            else:
                self.itm = False
                self.intrinsic = 0.00
                self.extrinsic = self.price
        else:
            self.BS_IV = Calculate_IV_Call_Put(self.underlying_price, self.strike, r = 0.0001, T = self.time_percentage, Option_Price = self.price, Put_or_Call = "Put")
            if self.underlying_price < self.strike:
                self.itm = True
                self.intrinsic = self.strike - self.underlying_price
                self.extrinsic = self.price - self.intrinsic
            else:
                self.intrinsic = 0.00
                self.extrinsic = self.price
        #expiration and dte values
        if self.seconds_to_exp == 0.00:
            self.expired = True
            self.price = self.intrinsic
        #https://www.programiz.com/python-programming/datetime/strftime#format-code
        #greeks should be functions imported from a greeks module
        #self.d1_d2 = {'d1':calc_d1(strike),'d2':calc_d2()}
        self.greeks = {'Delta': 'delta',
            'Gamma':'gamma',
            'Vega':'vega',
            'Theta':'theta',
            'Rho':'rho'}
    def add_subtract_contracts(self, x):
        self.contracts += x
        return self.contracts
    def grab_json(self,):
        r = json.dumps(c.get_option_chain(symbol = underlying_ticker,
        contract_type = self.call_put, strike = strike, strike_from_date = start, strike_to_date = end).json())
        return r
    def recalc_values(self,):
        return self.price, self.greeks
    def __str__(self,):
        result = str(self.underlying)+" " + str(self.strike) +" "+str(self.expiration)+" "+str(self.call_put)
        return result
