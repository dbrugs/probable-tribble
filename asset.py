from option_class import Option
from auth import c


class Asset:
    def __init__(self,ticker, delta = 0.00, assettype = None):
        self.ticker = ticker
        self.delta = delta
        #Option dictionary Option:contracts
        self.option_dict = {
        }
        self.price = c.get_quote(ticker)
        self.beta = 0.00
        self.delta_target = 0.00
        self.description = None
    def add_option(self, option, contracts):
        if option in self.option_dict.keys:
            self.option_dict[str(option)] += contracts
        else:
            self.option_dict[str(option)] = contracts
        option.contracts+=contracts
        return self.option_dict, option
    def add_subtract_delta(self, delta):
        self.delta += delta
        return self.delta
    def recalc_values(self):
        '''Returns new snapshot of values including assetprice
        option_book price, and cumulative greeks'''
        pass
    def calc_beta(self, beta_symbol = 'SPX'):
        beta_quote = 0.00
        return self.price
    def __str__(self):
        result = str(self.ticker)
        return result
#invisible subclass
class Security(Asset):
    def __init__(self, ):
        Asset.__init__(self, ticker, delta = 0.00, assettype = None)

##asset subclasses
class Future(Asset):
    def __init__(self, month, year, sector = None ):
        Asset.__init__(self, ticker, delta = 0.00, assettype = 'future',)
        months = {'Jan':'F','Feb':'G', 'Mar':'H', 'Apr':'J','May':'K','Jun':'M',
        'Jul':'N','Aug':'Q','Sep':'U','Oct':'V','Nov':'X', 'Dec':'Z'}
        sectors = ['equities', 'metals', 'interest rates', 'energies','ags', 'grains', 'softs','currencies']
        if month in months.keys:
            self.month = months[month_code].values
        else:
            print('Not a valid month code')
            month = str(input())
            self.month = months[month].values
        if sector in sectors:
            self.sector = sectors[sector]
        else:
            print('Not a sector, please add. Setting to "None"')
            self.sector = None
        self.year = str(year)
        def calc_backwardation_contango(self, spot):
            self.versus_spot = self.mark - spot
            if spot > self.mark:
                self.contango = False
            return self.versus_spot, self.contango


class Bond(Asset):
    def __init__(self, coupon, duration, issuer, rating, payments_per_year = 12):
        Asset.__init__(self, ticker, delta = 0.00, assettype = 'bond')
        self.issuer = issuer
        self.coupon = coupon
        self.payments_per_year = payments_per_year
class Equity(Asset):
    def __init__(self, sector = None, shares_outstanding = 0, dividend = 0.00):
        Asset.__init__(self, ticker, delta = 0.00, assettype = 'equity')
class Currency(Asset):
    def __init__(self, country, projected_interest = 0.00,):
        Asset.__init__(self, ticker, delta = 0.00, assettype = 'currency')
