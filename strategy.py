from asset import Asset

class Strategy:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
        self.asset_dict = {
        }
    def add_subtract_asset(self,asset):
        if asset in self.asset_dict:
            print("Already in dictionary")
        else:
            self.asset_dict[str(asset)] = asset
        return self.asset_dict[str(asset)]
    def rebalance(self):
        pass
    def __str__(self):
        result = str(self.name)
        return result


##strategysubclasses
class DragStrat(Strategy):
    pass
class CarryStrat(Strategy):
    pass
class Six_Sigma(Strategy):
    pass
