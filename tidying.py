import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

df = pd.DataFrame(np.arange(0, 15).reshape(5, 3),
                  index=['a', 'b', 'c', 'd', 'e'],
                  columns=['c1', 'c2', 'c3']
                  )

df['c4'] = np.nan
df.loc['f'] = np.arange(15, 19)
df.loc['g'] = np.nan
df['c5'] = np.nan
df['c4']['a'] = 20
# print(df)
# print(df.isnull())
# print(df.isnull().sum())
# print(df.isnull().sum().sum())
# print(df.count())
# print(df.c4[df.c4.notnull()])
# print(df.c4.dropna())
# print(df.c4)
# print(df.dropna(how='all'))
# print(df.dropna(how='all', axis=1))
# df2 = df.copy()
# df2.loc['g'].c1 = 0
# df2.loc['g'].c3 = 0
# print(df2)
# print(df2.dropna(how='any', axis=1))

# a = np.array([1, 2, np.nan, 3])
# s = pd.Series(a)
# print(a.mean(), s.mean())
# print(df.fillna(0))
# print(df.c4.fillna(method="bfill"))
# fill_values = pd.Series(
#     [100, 101, 102], index=['a', 'e', 'g']
# )
# print(fill_values)
# print(df.c4.fillna(fill_values))
# print(df.fillna(df.mean()))

# s = pd.Series(
#     [1, np.nan, np.nan, np.nan, 2]
# )
# print(s.interpolate)

# ts = pd.Series(
#     [1, np.nan, 2],
#     index=[
#         datetime.datetime(2014, 1, 1),
#         datetime.datetime(2014, 2, 1),
#         datetime.datetime(2014, 4, 1)
#     ]
# )
# print(ts.interpolate())
# print(ts.interpolate(method="time"))

# Handling duplicate value
# data = pd.DataFrame({
#     'a': ['x'] * 3 + ['y'] * 4,
#     'b': [1, 1, 2, 3, 3, 4, 4]
# })
# print(data)
# print(data.duplicated())
# print(data.drop_duplicates())
# print(data.drop_duplicates(keep='last'))
# data['c'] = range(7)
# print(data.duplicated())
# print(data.drop_duplicates(['a', 'b']))


# Mapping date into different values
# x = pd.Series(
#     {'one': 1, 'two': 2, 'three': 3}
# )
# y = pd.Series({
#     1: "a", 2: "b", 3: "c"
# })
# print(x)
# print(y)
# print(x.map(y))

# Replacing values
# s = pd.Series([0., 1., 2., 3., 2., 4.])
# print(s)
# print(s.replace(2,5))
# print(s.replace([
#     0, 1, 2, 3, 4
# ], [
#     4, 3, 2, 1, 0
# ]))

# print(s.replace({
#     0: 10, 1: 100
# }))
# df = pd.DataFrame({
#     'a': [0, 1, 2, 3, 4],
#     'b': [5, 6, 7, 8, 9]
# })
# print(df)
# print(df.replace([1, 2, 3], method='pad'))

# s = pd.Series(np.arange(0, 5))
# print(s.apply(lambda v: v * 2))
# print(df.apply(lambda col: col.sum()))
# print(df.apply(lambda row:row.sum(), axis=1))

