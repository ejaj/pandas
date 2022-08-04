import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# np.random.seed(123456)
# df = pd.DataFrame(np.random.randn(5, 4), columns=['A', 'B', 'C', 'D'])
# print(df)
# print(df * 2)
# s = df.iloc[0]
# diff = df - s
# print(df)
# diff = s - df
# print(diff)

# s = pd.Series(['a', 'a', 'b', 'c', np.NaN])
# print(s.count())
# print(s)
# print(s.unique())
# print(s.nunique())
# print(s.nunique(dropna=False))

df = pd.read_csv('data/prices.csv')
# print(df[['MSFT', 'AAPL']].min())
# print(df[['MSFT', 'AAPL']].max())
# print(df[['MSFT', 'AAPL']].idxmin())
# print(df[['MSFT', 'AAPL']].idxmax())
# print(df.nsmallest(4, ['MSFT'])['MSFT'])

# cl = pd.Series([1,2,3,4]).cumprod()
# print(cl)

# cl = pd.Series([1, 2, 3, 4]).cumsum()
# print(cl)

# print(df.describe())
# print(df.MSFT.describe())
# print(df.MSFT.describe()['mean'])
# non_num = pd.Series(['a', 'a', 'b', 'b', 'c', np.NaN])
# print(non_num.describe())
# print(df.mean(axis=1)[:5])
# print(df.median())
# print(df.var())
# print(df.std())
# print(df.MSFT.cov(df.AAPL))
# print(df[['MSFT']].pct_change()[:5])

np.random.seed(123456)
s = pd.Series(np.random.rand(1000)).cumsum()
print(s[:5])

s[0:100].plot()
plt.show()
