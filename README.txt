EADME:

The idea is to create a good multi-asset strategy fund with
good Sharpe ratio. It should be scalable and look to base capital limits on optimal
R/R strategies (goal is not to have 1BB AUM, but to have the most risk adjusted positive return
for assets assumed)
  -this is because all of these strategies will have liquidity constraints(esp the income strats)
  -goal is to retire, not blow up 3 accounts
---------------------------------------------------------

Current progress (in python):
option_class
asset_class
strategy_class
portfolio_class

data pipeline (honestly probs not too hard):
td-api wrapper
homebrew with requests/json packages
-------------

data object

some ideas for strategies and their assumptions:

  -strats broken up into types:
    -income (short vol, long contango etc)
        -commodity curve strats
          -grains are the best(good, reliable contango), but most commodities have good carry
        -SPX short vol strat
          -sell 20/15 deltas 45 days out
          -buy straddles >100(200) days out
          -buy gamma risk straddles within 2 weeks of exp to prevent VIX events
          (this is where the second-order greeks come in)
          -selling short term vol/gamma scalp (quick cash, small percentage of AUM, large gamma risk)
          -adjust deltas every 5/50
          -this strat is short IV with gamma hedge
          AND owning long-term straddles as an asset)
        -future possible HFT vol arb strats(seriously so far away):
          probably need C or Fortran

    -trend following (technical analysis, 3:1 risk/reward payoff strats, fundamental theses without big premiums)

    -"black swan strats" (these types would encompass both "Big Short opps"
    AND tail risk/loss mitigation)
      -these strats will tend to have a high theta bill, so the payoffs should be 1:100+
      or easily offset by income strats

current workflow ideas:
using atom with teletype
https://blog.atom.io/2017/11/15/code-together-in-real-time-with-teletype-for-atom.html
live share VScode
https://docs.microsoft.com/en-us/visualstudio/liveshare/use/vscode
git/github
open to other collab tools
