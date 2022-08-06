import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# np.random.seed(123456)
# s = pd.Series(
#     np.random.randn(1096),
#     index=pd.date_range(
#         '2012-01-01',
#         '2014-12-31'
#     )
# )
# walk_s = s.cumsum()
# walk_s.plot()
# plt.show()
# walk_df = pd.DataFrame(walk_s)
# walk_df.plot()
# plt.show()

# np.random.seed(123456)
# df = pd.DataFrame(
#     np.random.randn(1096, 2),
#     index=walk_s.index,
#     columns=list('AB')
# )
# walk_df = df.cumsum()
# print(walk_df.head())
# walk_df.plot()
# plt.show()
# walk_df.plot(
#     title="Title of the chart",
#     legend=False,
#     style=[
#         'g', '#FF0000'
#     ]
# )
# plt.xlabel('Time')
# plt.ylabel('Money')
# plt.legend(['1', '2'], loc='upper center')
# plt.show()

# t = np.arange(0., 5., 0.2)
# legend_labels = [
#     'Solid',
#     'Dashed',
#     'Dotted',
#     'Dot-dashed',
#     'Points'
# ]
#
# line_style = pd.DataFrame({
#     0: t,
#     1: t ** 1.5,
#     2: t ** 2.0,
#     3: t ** 2.5,
#     4: t ** 3.0,
# })
# ax = line_style.plot(
#     style=[
#         'r-', 'g--', 'b:', 'm-.', 'k:'
#     ]
# )
# ax.legend(
#     legend_labels, loc='upper left'
# )

#
# ticks_data = pd.DataFrame(
#     np.arange(0,5)
# )
# ticks_data.plot()
# ticks, labels = plt.xticks()
# print(ticks)
# plt.show()


# np.random.seed(123456)
# s = pd.Series(
#     np.random.randn(10) - 0.5
# )
# s.plot(kind='bar')
# plt.show()

# df2 = pd.DataFrame(
#     np.random.randn(10, 4),
#     columns=['a', 'b', 'c', 'd']
# )
# df2.plot(kind='bar')
# df2.plot(kind='bar', stacked=True)
# df2.plot(kind='barh', stacked=True)
# plt.show()


# np.random.seed(123456)
# dfh = pd.DataFrame(
#     np.random.randn(1000)
# )
# dfh.hist()
# dfh.hist(bins=100)
# plt.show()

# np.random.seed(123456)
# dfb = pd.DataFrame(
#     np.random.randn(10,5)
# )
# dfb.boxplot(return_type='axes')
# plt.show()
# dfa = pd.DataFrame(
#     np.random.randn(10, 4),
#     columns=[
#         'a', 'b', 'c', 'd'
#     ]
# )
# dfa.plot(kind='area', stacked=False)
# plt.show()

# sp_df = pd.DataFrame(
#     np.random.randn(10000, 2),
#     columns=['a', 'b']
# )
# sp_df.plot(kind='scatter', x='a', y='b')
# plt.show()

# s = pd.DataFrame(
#     np.random.randn(1000)
# )
# s.hist(normed=True)
# s.plot(kind='kde', figsize=(10, 8))

# Heat map

s = pd.Series(
    [0.0, 0.1, 0.2, 0.3, 0.4],
    ['V', 'W', 'X', 'Y', 'Z']
)
heatmap_data = pd.DataFrame(
    {
        'A': s + 0.0,
        'B': s + 0.1,
        'C': s + 0.2,
        'D': s + 0.3,
        'E': s + 0.4,
        'F': s + 0.5,
        'G': s + 0.6
    }
)
plt.imshow(
    heatmap_data,
    cmap='hot',
    interpolation='none'
)
plt.colorbar()
plt.xticks(
    range(len(heatmap_data.columns)),
    heatmap_data.columns
)
plt.yticks(
    range(len(heatmap_data.columns)),
    heatmap_data.index
)

plt.show()
