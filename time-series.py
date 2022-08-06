import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from pandas.tseries.offsets import *
from pandas.tseries.holiday import *

# dti = pd.date_range('2014-08-29', '2014-09-05', freq='B')
# print(dti.values)
# print(dti.freq)

# days = pd.date_range(
#     '2014-08-29', '2014-09-05', freq='B'
# )
# d = datetime.datetime(2014, 8, 29)
# do = pd.DateOffset(days=1)
# print(d + do)
# print(d+BusinessDay())
# print(d+2*BusinessDay())
# print(d+BMonthEnd())
#
# print(BMonthEnd().rollforward(datetime.datetime(2014, 9, 15)))
#
# print(d - Week(weekday=1))

# qends = pd.date_range(
#     '2014-01-01', '2014-12-31', freq='BQS-JUN'
# )
# print(qends.values)


# aug = pd.Period('2014-08', freq='M')
# print(aug)
# print(aug.start_time, aug.end_time)
# sep = aug+1
# print(sep)

# mp2013 = pd.period_range(
#     '1/1/2013',
#     '12/31/2013',
#     freq='M'
# )
# print(mp2013)

# for p in mp2013:
#     print("{0} {1}".format(p.start_time, p.end_time))


# US FederalCalendar
# cal = USFederalHolidayCalendar()
# for d in cal.holidays(start='2014-01-01', end='2014-12-31'):
#     print(d)

# Custom businessDay
# cbd = CustomBusinessDay(holidays=cal.holidays())
# print(datetime(2014, 8, 29) + cbd)


count = 24*60*60*5
np.random.seed(123456)
values = np.random.randn(count)
ws = pd.Series(values)
walk = ws.cumsum()
walk.index = pd.date_range(
    '2014-08-01',
    periods=count,
    freq="S"
)
# print(walk)
# print(walk.resample("1Min").mean())
# print(walk['2014-08-01 00:00'].mean())
# print(walk.resample("1Min", closed='right').mean())

# first_minute = walk['2014-08-01 00:00']
# means = first_minute.rolling(
#     window=5,
#     center=False
# ).mean()
# means.plot()
# plt.show()

hlw = walk['2014-08-01 00:00']
means2 = hlw.rolling(
    window=2, center=False
).mean()
means3 = hlw.rolling(
    window=5, center=False
).mean()
means4 = hlw.rolling(
    window=10, center=False
).mean()

hlw.plot()
means2.plot()
means3.plot()
means4.plot()
plt.show()
