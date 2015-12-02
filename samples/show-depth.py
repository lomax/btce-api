#!/usr/bin/python
import sys
import matplotlib.pyplot as plt
import numpy as np
import time

import btceapi

timeout = 10
# If an argument is provided to this script, it will be interpreted
# as a currency pair for which depth should be displayed. Otherwise
# the BTC/USD depth will be displayed.
pairs = list()

if len(sys.argv) >= 2:
    pairs = sys.argv[1:]
    print "Showing depth for %s" % pairs
else:
    print "No currency pair provided, defaulting to btc_usd"
    pairs = ['btc_usd']

shown = False

while(not shown):

  fig = plt.figure()
  rows = len(pairs)
  pi = 1
  for p in pairs:

    asks, bids = btceapi.getDepth(p)

    ask_prices, ask_volumes = zip(*asks)
    bid_prices, bid_volumes = zip(*bids)

    print len(asks), len(bids)
    ax = fig.add_subplot(rows, 1, pi)
    plt.title("%s depth at %s" % (p,time.strftime("%Y-%m-%d %H:%M:%S")))
    pi = pi + 1
    ax.plot(ask_prices, np.cumsum(ask_volumes), 'r-')
    ax.plot(bid_prices, np.cumsum(bid_volumes), 'g-')
    ax.grid()

  plt.show(block=True)
