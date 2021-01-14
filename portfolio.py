from strategy import Strategy

class Portfolio:
    def __init__(self, initial_value,):
        self.initial_value = initial_value
        self.strategy_groups = dict()
        self.asset_list = []
        self.current_value = 0.00
    def add_subtract_strat(self,strat,add_subtract = 'add', weight = 0.00):
        if strat in self.strategy_groups.keys() == True and add_subtract == 'subtract':
            self.strategy_groups.pop(strat)
        elif strat in self.strategy_groups.keys() == True and add_subtract == 'add':
            pass
        else:
            self.strategy_groups[strat] = Strategy(name = strat, weight = weight)
        return self.strategy_groups[strat]
    def add_asset(self, asset,):
        pass
    def authenticate(self):
        pass
    def update_quotes(self):
        pass
    def rebalance_portfolio(self,):
        pass
    def __str__(self,):
        result = str(self.asset_list)
        return result
