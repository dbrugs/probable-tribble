import numpy as np
import scipy.stats as stats
import option_math_brugs.vol_math
from scipy.stats import norm
from option_math_brugs.d1_d2 import calc_d1, calc_d2

##Greeks (add higher derivative greeks later)


def calc_delta(d1, t, CallPut, q = 0.00):
    """returns the delta   of the BS option pricing model

    Params:
    S - underlying price
    t - time
    K - strike
    r - risk-free-rate
    q - dividend rate
    sigma - vol param
    CallPut - 'CALL' or 'PUT'
    """
    #https://github.com/732jhy/Delta-Hedging/blob/master/Delta%20Hedging%20Sim.ipynb
    CallPut = CallPut.upper()
    if CallPut == 'CALL':
        delta1 = stats.norm.cdf(d1)*np.exp(-q*t)
    elif CallPut == 'PUT':
        delta1 = (stats.norm.cdf(d1)*np.exp(-q*t))-1.0000
    return delta1

def calc_gamma(d1, t, S, sigma):
    """Returns: gamma -- 1st derivative of delta
    Params: Delta: calc using delta function
    t = time
    S = underlying price
    sigma = vol input
    """
    phi_d1 = vol_math.calc_phi_d1(d1)
    #http://www.iotafinance.com/en/Formula-Gamma-of-an-option.html
    gamma = phi_d1/((S * sigma)*np.sqrt(t))
    return gamma

def calc_vega(S, phi_d1, sigma, t,):
    """Returns: vega, sensitivity of option price to changes in vol of underlying
    Params: S - Price of underlying
            phi_d1 = use calc_phi_d1 function
            t = time
    """
    #https://www.iotafinance.com/en/Formula-Vega-of-an-option.html
    vega = (S *phi_d1)*(np.sqrt(t))
    return vega

def calc_theta(S, K, phi_d1, sigma, t, CallPut, r, d2):
    """S - price of underlying
    K - Strike
    phi_d1 = use calc_phi_d1 function
    sigma = underlying iv
    t = time
    r = risk-free rate
    d2 - d2_function

    Returns: theta
    """
    CallPut = CallPut.upper()
    if CallPut == "CALL":
        #https://www.iotafinance.com/en/Formula-Theta-of-a-Call-Option.html
        theta1 = -1*((S*phi_d1*sigma)/2*np.sqrt(t))-(r*K*vol_math.e()**(-r*t)*norm.cdf(d2))
    elif CallPut == "PUT":
        #https://www.iotafinance.com/en/Formula-Theta-of-a-Put-Option.html
        theta1 = -1*((S*phi_d1*sigma)/2*np.sqrt(t))+(r*K*vol_math.e()**(-r*t)*norm.cdf(-1*d2))
    return theta1

def calc_rho(K, r, t, d2, CallPut):
    CallPut = CallPut.upper()
    if CallPut == "CALL":
        #https://www.iotafinance.com/en/Formula-Rho-of-a-call-option.html
        rho1 = K*t*vol_math.e()**((-1*r*t)*norm.cdf(d2))
    elif CallPut == "PUT":
        #https://www.iotafinance.com/en/Formula-Rho-of-a-Put-Option.html
        rho1 = -1*(K*t*vol_math.e()**((-1*r*t)*norm.cdf(d2)))
    return rho1
