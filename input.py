#ere are some other symbols that are not intuitive: SPY,$SPX.X, QQQ,$NDX.X,
#IWM,$RUT.X, IYY,$DJI2MN
#Vol indexes $VIX.X,$VXX.X,$VXN.X,$RVX.X

from auth import c
futures_months = ['F','G','H','J','K','M','N','Q','U','V','X','Z']
data_dict = dict({
#keys = instrument type, values = dict
    'Futures':{
    #keys = sector, values = dict
        #keys = symbol, values = dict
        '/ZT':{
        #keys = url, values = dict/dataobject
            'quandl_url':"CHRIS/CME_TU",
                'name': 'two_year',
                'sector': 'BONDS'},
        '/ZN':{
            'quandl_url':"CHRIS/CME_TY",
                'name': 'ten_year',
                'sector': 'BONDS'},
        '/ZF':{
            'quandl_url':"CHRIS/CME_FV",
                'name': 'five_year',
                'sector': 'BONDS'},
        '/ZB':{
            'quandl_url':"CHRIS/CME_US",
                'name': '30_year_bond',
                'sector': 'BONDS'},
        '/UB':{
            'quandl_url':"CHRIS/CME_UL2",
                'name': 'ultrabonds',
                'sector': 'BONDS'},
        '/GE':{
            'quandl_url':"CHRIS/CME_ED",
                'name': 'eurodollar',
                'sector': 'BONDS'},
        '/ES':{
            'quandl_url':"CHRIS/CME_ES",
                'name': 'sp500',
                'sector': 'EQUITIES'},
        '/NQ':{
            'quandl_url':"CHRIS/CME_NQ",
                'name': 'nasdaq_100',
                'sector': 'EQUITIES'},
        '/YM':{
            'quandl_url':"CHRIS/CME_YM",
                'name': 'Dow_20',
                'sector': 'EQUITIES'},
        '/VX':{
            'quandl_url':"CHRIS/CBOE_VX",
            'name': 'VIX',
            'sector': 'EQUITIES'},
        '/RTY':{
            'quandl_url':"None",
            'name': 'Russell_2k',
            'sector': 'EQUITIES'},
        '/NKD':{
            'quandl_url': 'CHRIS/CME_N1Y',
            'name': 'Nikkei',
            'sector':'EQUITIES'},
#AGS_GRAINS/SOFTS
        '/ZS':{
            'quandl_url':'CHRIS/CME_S',
            'name': 'soybeans',
            'sector': 'AGS_GRAINS'},
        '/ZC':{
            'quandl_url':'CHRIS/LIFFE_EMA',
            'name': 'corn',
            'sector': 'AGS_GRAINS'},
        '/ZW':{
            'quandl_url':"CHRIS/CME_W",
                'name': 'wheat',
                'sector': 'AGS_GRAINS'},
        '/ZL':{
            'quandl_url': "CHRIS/CME_BO",
            'name': 'bean_oil',
            'sector':'AGS_GRAINS'},
        '/ZM':{
            'quandl_url':'CHRIS/CME_SM',
            'name':'bean_meal',
            'sector': 'AGS_GRAINS'},
        '/LE':{
            'quandl_url':"CHRIS/CME_LC",
            'name':'live_cattle',
            'sector': 'AGS_GRAINS'},
        '/GF':{
            'quandl_url':"CHRIS/CME_FC",
            'name':'feeder_cattle',
            'sector': 'AGS_GRAINS'},
        '/HE':{
            'quandl_url':"CHRIS/CME_LN",
            'name':'live_hogs',
            'sector': 'AGS_GRAINS'},
        '/SB':{
            'quandl_url':"CHRIS/ICE_SB",
            'name':'sugar',
            'sector':'AGS_GRAINS'},
        '/OJ':{
            'quandl_url':"None",
            'name':'frozen_orange_juice',
            'sector':"SOFTS"},
        '/CC':{
            'quandl_url':"None",
            'name':'cocoa',
            'sector':'SOFTS'},
        '/KC':{
            'quandl': "None",
            'name':'coffee',
            'sector':'SOFTS'},
##currencies
        '/6A':{
            'quandl_url':"CHRIS/CME_AD",
            'name':'aussie_dollar',
            'sector':'FX'
            },
        '/6B':{
            'quandl':"CHRIS/CME_BP",
            'name':'british_pound',
            'sector':'FX'},
        '/6C':{
            'quandl_url':"CHRIS/CME_CD",
            'name':'canadian_dollar',
            'sector':'FX'},
        '/6E':{
            "CHRIS/CME_EC":{'euro':{}}},
        '/6J':{
            'quandl_url':"CHRIS/CME_JY",
            'name':'yen',
            'sector':'FX'
            },
        '/DX':{
            'quandl_url':"CHRIS/ICE_DX1",
            'name':'dollar',
            'sector':'FX'},
##energies
        '/CL':{
            'quandl_url':"CHRIS/CME_CL",
            'name':'wti_crude',
            'sector':'energies'},
        '/RB':{
            'quandl_url':["CHRIS/CME_RB","CHRIS/ICE_N"],
            'name':'RBOB_CME',
            "sector":'energies',
            },
        '/HO':{
            'quandl_url':['CHRIS/CME_YH','CHRIS/ICE_O'],
            'name': 'heating_oil',
            "sector":'energies',
            },
        '/NG':{
            'quandl_url':['CHRIS/CME_NG','CHRIS/ICE_M'],
            'name':'natural_gas',
            'sector':'energies'
        },
        '/BZ':{
        "quandl_url": 'CHRIS/ICE_B',
        'name':'brent_crude',
        'sector':'energies'
        },},
    'Indexes':{
        'SPX':{'$SPX.X'},
        'DOW':{},
        'NDX':{"$NDX.X"},
        'RTX':{"$RUT.X"},
        'DJT':{},
        'VIX':{'$VIX.X'},
        'OEX':{},
    },
    'Equities':{
        'SPY':{},
        'IWM':{},
        'QQQ':{},
        'GLD':{},
        },
    'Currencies':{
        'EUR/USD':{},
        'AUD/JPY':{},
        'GBP/USD':{},
    },
    'Bonds':''})
