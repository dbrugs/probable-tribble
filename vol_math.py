"""volatility math functions
@@brugs_bunny"""

import numpy as np
from option_math_brugs.d1_d2 import calc_d1, calc_d2
from scipy.stats import norm
import math
from datetime import datetime

def unix_time_milliseconds(dt):
    #grab starting point so time = 0
    epoch = datetime.utcfromtimestamp(0)

    return (dt - epoch).total_seconds()*1000


def e(n = 10):
    """Returns Eulers number"""
    return sum(1/ float(math.factorial(i)) for i in range(n))

def calc_phi_d1(d1):
    """Returns: Phi-d1 - inverse of the natural log around a radius"""
    d1_phi = (1/((e())**((d1**2)/2)))/(np.sqrt(2*np.pi))
    return d1_phi

def GBM_approx(S, mu, T, sigma, N):
  """
  Simulates a single path of Brownian motion

  Args: S - initial path value
        mu - mean parameter
        T - time parameter
        N - number of steps in path

  """
  dt = T/N
  W = np.random.standard_normal(size = N - 1)
  W = np.array[0]+list(np.cumsum(W)*np.sqrt(dt))
  t = np.linspace(0, T, N)
  S = S*np.exp((mu - 0.5*sigma**2)*t + sigma*W)
  return S, t

def calc_risk_free(symbol = 'SPX'):
    """
    quote SPX 100/200 call spread price
    """
    pass

def historical_volatility(sym, days):
    pass

def garman_klass_volatility(sym, days):
    pass

def BlackScholes(CallPut,S,K,t,r,sigma):
    #https://www.macroption.com/black-scholes-excel/
    CallPut = str(CallPut).upper()
    d1 = calc_d1(S, t, K, sigma = sigma, r = r, q = 0.00)
    d2 = calc_d2(d1, sigma, t)
    if CallPut == 'CALL':
        return S * norm.cdf(d1) - K * np.exp(-r * t) *  norm.cdf(d2)
    elif CallPut == 'PUT':
        return K * np.exp(-r * t) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        print('Not a Call or Put')

def calc_vix_daily_move(VIX):
    return VIX/np.sqrt(252.00)
def calc_vix_monthly_move(VIX):
    return VIX/np.sqrt(12.00)
