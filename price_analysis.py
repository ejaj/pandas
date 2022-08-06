import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from datetime import datetime, date

import pandas_datareader as pdr


def get_stock_data(ticker, start, end):
    data = pdr.data.DataReader(
        ticker,
        'yahoo',
        start,
        end
    )
    data.insert(0, "Ticker", ticker)
    return data


start = datetime(2012, 1, 1)
end = datetime(2014, 12, 31)

data = get_stock_data(
    "MSFT",
    start,
    end
)[:5]


def get_date_for_multiple_stocks(tickers, start, end):
    stocks = dict()
    for ticker in tickers:
        s = get_stock_data(ticker, start, end)
        stocks[ticker] = s
    return stocks


raw = get_date_for_multiple_stocks(
    ['MSFT', 'AAPL', 'GE', 'IBM', 'AA', 'DAL', 'UAL', 'PEP', 'KO'],
    end, end
)


# print(raw['MSFT'][:5])

def pivot_tickers_to_columns(raw, column):
    items = []
    for key in raw:
        data = raw[key]
        subset = data[[
            "Ticker", column
        ]]
        items.append(subset)
    combined = pd.concat(items)
    ri = combined.reset_index()
    return ri.pivot(
        "Date", "Ticker", column
    )


close_px = pivot_tickers_to_columns(raw, "Close")
# print(close_px[:5])
# close_px['AAPL'].plot()
# close_px['MSFT'].plot()
# plt.show()

volumes = pivot_tickers_to_columns(
    raw,
    "Volume"
)
volumes.tail()

msft_volume = volumes[['MSFT']]
plt.bar(
    msft_volume.index, msft_volume['MSFT']
)
plt.gcf().set_size_inches(15, 8)

top = plt.subplot2grid(
    (4,4),(0,0), rowspan=3, colspan=4
)
top.plot(
    close_px['MSFT'].index, close_px['MSFT'],
    label="MSFT Close"
)
plt.title(
    "MSFT Close Price 2012-2014"
)
plt.legend(loc=2)

bottom = plt.subplot2grid(
    (4,4),(3,0), rowspan=1, colspan=4
)
bottom.bar(
    msft_volume.index, msft_volume['MSFT'],
    label="MSFT Close"
)
plt.title(
    "MSFT Close Price 2012-2014"
)
plt.legend(loc=2)

plt.show()
