"""Market Breadth Measurements
@@@brugs_bunny"""

def advance_decline(close,close_yesterday):
    if close_yesterday < close:
        advance = True
        decline = False
    elif close_yesterday > close:
        advance = False
        decline = True
    return advance, decline

def a_d_oscillator(adv, decl):
    return adv-decl

def advance_decline_line(adv_dec,index_value):
    return adv_dec + index_value
