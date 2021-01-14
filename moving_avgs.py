"""moving averages calculated using a DataFrame option
 to add column with result
@@brugs_bunny
 """

import pandas as pd
import numpy as np
from pandas import DataFrame

def simple_moving_avg(series, column = 'close', n = 20, add_col = False):
    sma = df[column].rolling(n).apply(lambda x: np.sum(x)/n, raw = True).to_list()
    if add_col == True:
        df[f'{column}_SMA_{n}'] = smas
        return df
    else:
        return smas


def weighted_ma(df, column='close', n=20, add_col=False, weights = None):
    if weights = None
        weights = np.arange(1, n + 1)
    else:
        ##enable custom weighting (must be list of n size)
        weights = np.arange(weights)

    wmas = df[column].rolling(n).apply(lambda x: np.dot(x, weights) /
                                       weights.sum(), raw=True).to_list()
    if add_col == True:
        df[f'{column}_WMA_{n}'] = wmas
        return df
    else:
        return wmas

def exponential_moving_avg(df, n = 20):
    weight_current = 2/(n+1)
    weight_ma = 1.00 - weight_current

def Wilders_MA(x):
    return x

def geometric_moving_avg(x):
    return x

def triangular_moving_avg(x):
    return x

def vol_weighted_moving_avg(x):
    return x
#####MACD
def calc_macd(df, column = 'close', n1 = 12, n2 = 24, n3 = 9):
    df['Macd_sma1'] = df[column].rolling(window = n1 ,min_periods = n1).mean()
    df['Macd_sma2'] = df[column].rolling(window = n2 ,min_periods = n2).mean()
    df['MACD_sma_difference'] = df['Macd_sma1']-df['Macd_sma2']
    df['MACD_ema'] = df['MACD_sma_difference'].ewm(window = n3, min_periods =  n3).mean()
    return df
###bands and envelopes
def calc_bollinger_bands(df, column = 'close', n = 20, sd = 2, add_col = False):
    std = df[column].rolling(window = n, min_periods = n).std()
    mid = df[column].rolling(window=20,min_periods=20).mean()
    upper = mid + sd * std
    li = [mid, upper, lower]
    if add_col == True:
        for i in li:
            df[f'{column}_{i}_{n}'] = i
        return df
    else:
        return std, mid, upper, lower
