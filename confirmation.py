"""Volume related confirmation indicators
@@brugs_bunny"""

def calc_OBV(open,close, volume):
    """On Balance volume
    def OBV(volume,index_value, open, close):
    pg 210"""
    if open > close:
        obv = index_value - volume
    elif close > open:
        obv = index_value + volume
    else:
        obv = index_value
    return obv

def price_volume_trend(close, yesterday_close, volume):
    """pg. 211
    """
    percent_change = (close - yesterday_close)/yesterday_close
    return percent_change*volume

def williams_variable_accum_dist(close, open, high, low, volume):
    """WVAD
    open and close prices are most important prices of the day
    pg 212"""
    range = high - low

def chaikan_accum_dist(open,high,low,close,volume):
    """pg 213
    close above open is accumulation
    close below open is distribution"""
    return ((close - open)/range) * volume
    return volume * ((close-low)) - (high-close))/(high-low)

def williams_accum_dist(low, high, close, yesterdays_close,volume,include_volume = True):
    """No open price used like in WVAD
    pg 214
    TRUE RANGE
    can also include or exclude volume """
    true_range_high = max(high, yesterdays_close)
    true_range_low = min(low, yesterdays_close)
    true_range = true_range_high-true_range_low
    if close > yesterdays_close == True:
        return close - true_range_low*volume
    elif close < yesterdays_close == True:
        return close - true_range_high * volume
def volume_oscillator(period1,period2):
    """pg 214
    ratio between 2 volume moving averages
    use is to determine when volume is expanding/contracting
    -- expanding volume indicates trend strength

    --useful as a confirmation indicator and advanced warning in a range or consolidation
    for the direction of the next breakout"""
    return period1/period2
def chaikan_money_flow(volume, period,close, yesterday_close):
    li = []
    accumulation = 0.00
    distribution = 0.00
    for i in range(1,period):
        x = close - yesterday_close
        if x > 0.00 == True:
            accumulation += x
        elif x < 0.00 == True:
            distribution -= x
