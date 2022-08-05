import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# s1 = pd.Series(np.arange(0, 5))
# s2 = pd.Series(np.arange(1, 5))

# print(pd.concat([s1, s2]))
# df1 = pd.DataFrame(np.arange(0, 15).reshape(5, 3),
#                    index=['a', 'b', 'c', 'd', 'e'],
#                    columns=['c1', 'c2', 'c3']
#                    )
#
# df2 = pd.DataFrame(np.arange(0, 15).reshape(5, 3),
#                    index=['a', 'b', 'c', 'd', 'e'],
#                    columns=['c1', 'c2', 'c3']
#                    )
# print(pd.concat([df1, df2]))
# print(pd.concat([df1, df2], axis=1))
# print(pd.concat([df1, df2], axis=1, join='inner'))
# df = pd.concat([df1, df2], axis=1, keys=['df1', 'df2'])
# print(df)
# print(df1.append(df2))
# print(df1.append(df2, ignore_index=True))

# Merging
# orders = {
#     'CustomerID': [10, 11, 10],
#     'OrderDate': [
#         datetime.datetime(2014, 12, 1),
#         datetime.datetime(2014, 12, 1),
#         datetime.datetime(2014, 12, 1),
#     ]
# }
# orders = pd.DataFrame(orders)
# print(orders)

# sensor_readings = pd.read_csv("data/reading.csv")
# print(sensor_readings)
# print(sensor_readings[sensor_readings['axis'] == 'X'])

# print(sensor_readings.pivot(
#     index='interval',
#     columns='axis',
#     values='reading'
# ))

# Stacking & Unstacking
df = pd.DataFrame({
    'a': [1, 2]
}, index={'one', 'two'})
# print(df)
stacked1 = df.stack()
# print(stacked1)
# print(stacked1[('one', 'a')])

stacked2 = df.stack()
print(stacked2)
