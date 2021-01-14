README:


ENV CONFIG:

conda activate default_env
atom


GIT CONFIG:

/Desktop/scripts/yog_soggoth

TD API CONFIG:
https://github.com/areed1192/td-ameritrade-python-api/blob/master/README.md
-----------------------------------------------------------------------------
backend

data_pull
  =tda
  =quandl
data_clean
    -fastdata
      display json
    -slow_data
  |    -json to df
  |sync-quandl dict to df
  |    -yfinance dict to df
        dump
        -csv/sql/json
          --cleanup
            return DataFrame
          --store
            sql







---------------------------------------------------------------------------
Window1
  OVERVIEW TAB
  --------------------------
    Economic Bellweather Box
      Watchlist/Quotes
      "Signal Gradient Map"
    SPX Box
      Quote
      riskfree
      IV
      metrics monitor
        straddle price
        20 Delta Strangle price
        Delta
          delta bleed
        Vega
          DvegaDvol(or whatever)
    NewsBox/TextBox/Stream
      "Signal Alert"
      RSS feed

  my-tab
  ------------------------
    portfolio
      asset
  --------------
        option
  -------------
          price(quote,theoretical,sigma,time)
            d1,d2,greeks

  Settingstab
  ----------------------------------

Window2 - Visualization Window
  greek visualization for SPX
  portfolio metrics
    equity curve
    return vol viz
    netliq vol viz
    net-costs
