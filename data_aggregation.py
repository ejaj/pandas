import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime


# sensors_data = pd.read_csv("data/sensors.csv")
# print(sensors_data[:5])
# group_by_sensor = sensors_data.groupby('sensor')

# print(group_by_sensor)
# rint(group_by_sensor.ngroup)

# print(group_by_sensor.size())
# print(group_by_sensor.count())
# print(group_by_sensor.get_group('accel')[:5])
# print(group_by_sensor.head(3))
# print(group_by_sensor.nth(1))
# print(group_by_sensor.describe())

def print_groups(group_object):
    for name, group in group_object:
        print(name)
        print(group[:5])


# print_groups(group_by_sensor)

# msg = sensors_data.groupby(
#     ['sensor', 'axis']
# )
# print_groups(msg)

# mi = sensors_data.copy()
#
# mi = mi.set_index(
#     ['sensor', 'axis']
# )
# print(mi)
# sensor_axis_grouping = mi.groupby(
#     level=['sensor', 'axis']
# )
# print(sensor_axis_grouping.agg(np.mean))
# print(sensors_data.groupby(
#     ['sensor','axis'], as_index=False
# ).agg(np.mean))

# print(sensor_axis_grouping.mean())
# print(sensor_axis_grouping.agg([
#     np.sum, np.std
# ]))


# print(sensor_axis_grouping.agg(
#     {'interval': len, 'reading': np.mean}
# ))

# print(sensor_axis_grouping['reading'].mean())

# transform_data = pd.DataFrame({
#     'Label': ['A', 'C', 'B', 'A', 'C'],
#     'Values': [0, 1, 2, 3, 4],
#     'Values2': [5, 6, 7, 8, 9],
#     'Other': [
#         'foo',
#         'bar',
#         'baz',
#         'fix',
#         'buz'
#     ]
# }, index=list('VWXYZ'))

# print(transform_data)

# group_by_label = transform_data.groupby('Label')
# print(print_groups(group_by_label))
# cprint(group_by_label.transform(lambda x:x+10))

np.random.seed(123456)
data = pd.Series(
    np.random.normal(0.5, 2, 365 * 3),
    pd.date_range(
        '2013-01-01',
        periods=365 * 3
    )
)

rolling = data.rolling(
    window=100,
    min_periods=100,
    center=False
).mean().dropna()
# print(rolling[:5])
# rolling.plot()
# plt.show()

group_key = lambda x: x.year
groups = rolling.groupby(group_key)
groups.agg([np.mean, np.std])

zscore = lambda x: (x - x.mean()) / x.std()
normed = rolling.groupby(
    group_key
).transform(zscore)
normed.groupby(group_key).agg(np.mean, np.std)

compared = pd.DataFrame(
    {
        'Original': rolling,
        'Normed': normed
    }
)

compared.plot()
plt.show()
