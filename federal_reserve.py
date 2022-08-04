import pandas_datareader as pdr
import pandas as pd
import datetime

start = datetime.datetime(2005, 5, 1)
end = datetime.datetime(2020, 6, 1)

df = pdr.DataReader('PAYEMS', 'fred', start, end)
print(df)
