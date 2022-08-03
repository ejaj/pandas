import pandas as pd
import numpy as np

sp = pd.read_csv('data/business_analysis.csv', index_col='Symbol', usecols=[0, 2, 3, 7])
# print(sp.head())

# sp_new = sp.rename(columns={'Book Value': 'BookValue'})
# print(sp_new[:2])

# sp_copy = sp.copy()
# sp_copy['RoundPrice'] = sp_copy.Price.round()
# print(sp_copy[:2])
# sp_copy.insert(1, 'RoundPrice', sp_copy.Price.round())
# print(sp_copy[:2])

# ss = sp[:3].copy()
# ss.loc[:, 'PER'] = 0
# print(ss)
# np.random.seed(123456)
# ss.loc[:, 'PER'] = pd.Series(np.random.normal(size=3), index=ss.index)
# print(ss)

rounded_price = pd.DataFrame({'RoundPrice': sp.Price.round()})

concat = pd.concat([sp, rounded_price], axis=1)
print(concat[:5])
