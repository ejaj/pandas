import pandas as pd
import numpy as np

# dates = pd.date_range('2016-05-02', '2016-05-05')
# temp = pd.Series([80, 90, 70, 60], index=dates)
# temp_1 = pd.Series([10, 20, 30, 40], index=dates)
# temp_diffs = pd.DataFrame(
#     {
#         'Dhaka': temp,
#         'Khulna': temp_1
#     }
# )
# print(temp_diffs)
# print(temp_diffs['Dhaka'])
# print(temp_diffs['Khulna'])
# print(temp_diffs[['Khulna', 'Dhaka']])
# print(temp_diffs.Dhaka)

# temp_diffs_city = temp_diffs.Dhaka - temp_diffs.Khulna
# print(temp_diffs_city)
# temp_diffs['Difference'] = temp_diffs_city
# print(temp_diffs)
# print(temp_diffs.columns)
# print(temp_diffs.Difference[1:4])
# print(temp_diffs.iloc[1])
# print(temp_diffs.iloc[1].index)
# print(temp_diffs.loc['2016-05-02'])
# print(temp_diffs.iloc[[1, 2]].Difference)
# print(temp_diffs.Dhaka > 80)

# one_dimensional = pd.DataFrame(np.arange(1, 6))
# print(one_dimensional)
# two_dimensional = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]))
# print(two_dimensional)
# print(two_dimensional.columns)

two_dimensional = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]), columns=['A', 'B', 'C'])
print(two_dimensional)
print(len(two_dimensional))
print(two_dimensional.shape)