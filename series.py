import pandas as pd
import numpy as np

# s = pd.Series([1, 2, 3, 4])
# print(s)
# print(s[1])
# print(s[[1, 2]])
# s_index = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# print(s_index)
# print(s_index[['a', 'd']])
# print(s_index[[1, 2]])
# print(s_index.index)
# dates = pd.date_range('2016-05-02', '2016-05-05')
# print(dates)
# temp = pd.Series([80, 90, 70, 60], index=dates)
# print(temp)
# print(temp['2016-05-04'])
# temp_1 = pd.Series([10, 20, 30, 40], index=dates)
# temp_diffs = temp - temp_1
# print(temp_diffs)
# print(temp_diffs[2])

# np_s = pd.Series(np.arange(4, 9))
# np_s_l = pd.Series(np.linspace(0, 9, 5))
# print(np_s)
# print(np_s_l)
#
# np.random.seed(123)
# np_ran = pd.Series(np.random.normal(size=5))
# print(np_ran)

# np_s = pd.Series(np.arange(0, 5))
# np_s_mul = np_s * 2
# print(np_s_mul)

# s = pd.Series([1, 2, 3])
# print(s.values)
# print(s.index)
# print(len(s))
# print(s.size)
# print(s.shape)

# labels = ['First Name', 'Last Name']
# names = ['Kazi', 'Ejajul']
# s = pd.Series(labels, index=names)
# print(s)
# print(s.index)

# s = pd.Series(np.arange(1, 10), index=list('abcdefghi'))
# print(s.head())
# print(s.head(n=2))
# print(s.tail())
# print(s.tail(n=3))
# print(s.take([1, 5, 8]))
# s = pd.Series(np.arange(0, 5), index=list('abcde'))
# res = s >= 3
# print(res)
# print(s[s > 3])
# print((s > 3).any())

# Reindexing
# np.random.seed(123456)
# # s = pd.Series(np.random.randn(5))
# # print(s)
# # s.index = ['a', 'b', 'c', 'd', 'e']
# # print(s)
# s = pd.Series(np.random.randn(5), ['a', 'b', 'c', 'd', 'e'])
# print(s)
# s2 = s.reindex(['a', 'c', 'g'])
# print(s2)

s1 = pd.Series([0, 1, 2], index=[0, 1, 2])
s2 = pd.Series([3, 4, 5], index=['0', '1', '2'])
print(s1 + s2)
s2.index = s2.index.values.astype(int)
print(s1 + s2)
