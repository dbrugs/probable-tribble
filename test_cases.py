from option_class import Option
from asset import Asset
from datetime import datetime

def test_Option_class():
    option1 = Option(10,"ABC","Call",100.00,'01-02-2021')
    passing = False
    print(option1)
    return passing

def test_greeks():
    passing = False
    return passing

def test_objects():
    portfolio = Portfolio(100000)
    portfolio = portfolio.add_subtract_strat('name')
    print(portfolio)
    #print(portfolio.strategy_groups)
    strategy = Strategy('strat',0.33)
    print(strategy)

    option = Option(10,"SPY","Call",370.00,'01-04-2021')
    option.add_subtract_contracts(-8)
    print(option)
    asset = Asset("SPY", delta = 100.00)
    asset.add_subtract_delta(-50.00)
    print(asset.delta)

    strategy.add_subtract_asset(asset)
    print(strategy.asset_dict.items())
