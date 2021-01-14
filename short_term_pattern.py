"""short term price signals
@@brugs_bunny"""
ohlc = {'open': 0.00,'high': 0.00,'low': 0.00,'close': 0.00,}

def s_t_top_bottom(top = True, close = True):
    """return True if close yesterday greater than close today ANd close 2 days ago
    close = True on whether to look for highs or close"""
