import pandas_datareader as pdr
from pandas_datareader import wb

# all_indicators = pdr.wb.get_indicators()
# print(all_indicators.iloc[:5:2])

# le_indicators = pdr.wb.search("life expectancy")
# print(le_indicators[:5:2])
countries = pdr.wb.get_countries()
# print(countries.loc[0:5], ['name', 'capitalCity', 'iso2c'])
# le_data_all = pdr.wb.download(
#     indicator="SP.DYN.LE00.IN",
#     start=1980,
#     end=2014
# )

# print(le_data_all)
# print(le_data_all.index.levels[0])

le_data_all = pdr.wb.download(
    indicator="SP.DYN.LE00.IN",
    country=countries['iso2c'],
    start=1980,
    end=2014
)
# print(le_data_all)
le_data = le_data_all.reset_index().pivot(
    index='country',
    columns='year'
)
print(le_data.iloc[:5, 0:3])

country_with_least_expectancy = le_data.idxmin(axis=0)
print(country_with_least_expectancy[:5])

expectancy_for_least_country = le_data.min(axis=0)
print(expectancy_for_least_country[:5])
