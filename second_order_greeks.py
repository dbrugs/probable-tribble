"""Second order greeks
@@brugs_bunny"""

#from greeks import *
#import d1_d2 as d
import numpy as np
from scipy.stats import norm
from vol_math import e
#http://investment-and-finance.net/derivatives/s/second-order-greeks.html

def calc_volga(d1,d2,t, sigma, S, K):
    """d1
    d2
    t = time
    sigma
    S = underlying price
    K = strike"""
    #https://quant.stackexchange.com/questions/7025/how-to-calculate-vomma-of-black-scholes-model
    volga = S*np.sqrt(t)*d1*d2*norm.cdf(d1)/sigma
    return volga

def calc_vomma():
    """DvegaDvol - sensitivity of vega to changes in iv
    vega convexity"""
    vomma = 0.00
    return vomma/10000

def calc_vanna(d1,d2,t,sigma,r = 0.01, b = 0.01):
    """DdeltaDvol is same as DVegaDSpot(VANNA)
    r - risk free rate
    b - cost of carry
    """
    vanna = -e()**(((r-b)*t)*d2)/sigma*norm.cdf(d1)
    return vanna

def calc_charm(CallPut,d1,d2,sigma,t,r = 0.001,b = 0.001,):
    """DdeltaDtime - delta bleed"""
    CallPut = str(CallPut.upper())
    if CallPut == 'CALL':
        charm = -e()**((b-r*t*(norm.cdf(d1)*(b/(sigma*np.sqrt(t))-(d2/(2*t)))+(b-r)*norm.cdf(d1))))
    elif CallPut == 'PUT':
        charm = -e()**((b-r*t*(norm.cdf(d1)*(b/(sigma*t)-(d2/(2*t)))-(b-r)*norm.cdf(-d1))))
    return charm

def calc_DvegaDtime():
    DvegaDtime = 0.00
    return DvegaDtime

def calc_DvannaDvol(d1,d2,sigma,t,r = 0.001, b = 0.001,):
    """second order partial derivative of delta re vol
    DdeltaDvol sensitivity to vol"""
    DvannaDvol = ((-e()**((b-r)*t)*d2)/sigma)*norm.cdf(d1)*1/sigma(d1*d2-(d1/d2)-1)
    return DvannaDvol/10000#it is necessary to divide by 10k to get the greek on the metric of
    #1 point change in volatility

def calc_DgammaDvol():
    DgammaDvol = 0.00
    return DgammaDvol
