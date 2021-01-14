"""D1 and D2 used for calculation of Greeks
@@brugs_bunny"""

import numpy as np

def calc_d1(S, t, K, sigma, r, q = 0.00):
    """Returns: d1 - the probability that the option will expire in the money
    Params: S - underlying px
    t - time
    K - strike
    sigma - volatility input
    r - risk_free_rate
    q - dividend: default 0.00
    """
    # https://financetrainingcourse.com/education/wp-content/uploads/2011/03/Understanding.pdf
    #https://www.macroption.com/black-scholes-formula/
    d1 = (np.log(S/K)+((r - q)+(sigma**2*0.5)*t)/(sigma*np.sqrt(t)))
    return d1

def calc_d2(d1, sigma, t):
    """Returns: d2 - expected value, computed using risk-adjusted probabilities, of receiving the
    stock at expiration of the option, conditional probability
    Params: d1 -  the risk-adjusted probability that the option will be exercised.
    sigma - volatility
    t - time to exp
    """
    d2 = d1 - sigma*np.sqrt(t)
    return d2
