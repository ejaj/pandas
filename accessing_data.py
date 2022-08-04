import numpy as np
import pandas as pd
import matplotlib.pyplot as pt
from pandas import ExcelWriter
import sqlite3

# bd_ms = pd.read_csv('data/bd-ms.csv')
# bd_ms = pd.read_csv('data/bd-ms.csv', index_col=0)
# print(bd_ms[:5])
# print(bd_ms[:5])
# print(bd_ms.dtypes)

# bd_ms = pd.read_csv("data/bd-ms.csv", dtype={'Volume': np.float64})
# print(bd_ms.dtypes)

# bd_ms = pd.read_csv("data/bd-ms.csv", header=0, names=[
#     'date', 'open', 'high', 'low', 'close', 'volume'
# ])
# print(bd_ms[:5])

# bd_ms = pd.read_csv("data/bd-ms.csv",
#                     usecols=['Date', 'Close'], index_col=['Date'])
# print(bd_ms[:5])
# Saving DateFrame to a CSV file.
# bd_ms.to_csv("data/bd-ms-modified.csv", index_label='date')
# bd_ms = pd.read_table("data/bd-ms.csv", sep=',')
# print(bd_ms[:5])

# bd_ms.to_csv("data/bd-ms-piped.txt", sep='|')

# bs_ms2 = pd.read_csv("data/bs-ms2.csv", skiprows=[0, 2, 3])
# print(bs_ms2[:5])

# bs_ms_footer = pd.read_csv("data/bd-ms-footer.csv", skipfooter=2, engine='python')
# print(bs_ms_footer[:5])

# Process the first three rows
# bs_ms = pd.read_csv("data/bd-ms.csv", nrows=3)
# print(bs_ms)
# bs_ms = pd.read_csv("data/bd-ms.csv", skiprows=100, nrows=5, header=0, names=[
#     'date', 'open', 'high', 'low', 'close', 'vol'
# ])
# print(bs_ms)

# Read from excel
bs_excel = pd.read_excel("data/bd-stocks.xlsx")
# print(bs_excel[:5])
# Read from excel sheet
# bs_excel_sheet = pd.read_excel("data/bd-stocks.xlsx", sheet_name='aapl')
# print(bs_excel_sheet[:5])
# save to .xls file
# bs_excel.to_excel("data/bd-stocks3.xls")
# bs_excel.to_excel("data/bd-stocks4.xls", sheet_name='MSFT')

# bs_json = pd.read_json("data/bd-stocks.json")
# print(bs_json[:5])

# save to html
# bs_excel.head(2).to_html("data/bd-stocks.html")

# HDF5 format files

# np.random.seed(123456)
# df = pd.DataFrame(np.random.randn(8, 3), index=pd.date_range(
#     '1/1/2000', periods=8
# ), columns=['A', 'B', 'C'])
# store = pd.HDFStore('data/store.h5')
# store['df'] = df
# print(store)
# store = pd.HDFStore("data/store.h5")
# df = store['df']
# print(df[:5])

# Write to SQLite
# msft = pd.read_csv('data/bd-ms.csv')
# msft['Symbol'] = "MSFT"
# aapl = pd.read_csv('data/bd-aapl.csv')
# aapl['Symbol'] = "AAPL"
# connection = sqlite3.connect('data/bd-stocks.sqlite')
# msft.to_sql(
#     "STOCK_DATE", connection, if_exists="replace"
# )
#
# aapl.to_sql(
#     "STOCK_DATA", connection, if_exists="append"
# )
# connection.commit()
# connection.close()

# Read from SQLite
# connection = sqlite3.connect(
#     "data/bd-stocks.sqlite"
# )
#
# data = pd.io.sql.read_sql(
#     "SELECT * FROM STOCK_DATE;",
#     connection, index_col='index'
# )
#
# connection.close()
# print(data[:5])