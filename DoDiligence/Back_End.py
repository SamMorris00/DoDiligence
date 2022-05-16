import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ticker = input("Enter company ticker:") - TEMPORARY COMMENTED DURING DEBUGGING
company_ticker = "LGEN.L"
whole_company_data = yf.Ticker(company_ticker)

historical_data = whole_company_data.history(start="2000-01-01")
historical_dividend_data = historical_data['Dividends']
historical_dividend_payout_dates = historical_dividend_data[historical_dividend_data.Dividends != 0]  # filters old to remove entries = 0

grouped_historical_dividend_payout_dates = historical_dividend_payout_dates.resample('A').sum()
print(grouped_historical_dividend_payout_dates)

# #subplot creation
fig, (close, dividends) = plt.subplots(nrows=2, ncols=1)

# CLose price plot

y = historical_data['Close']
x = historical_data.index
close.plot(x, y, linewidth=1.0)

# Dividend plot
y_div = grouped_historical_dividend_payout_dates['Dividends']
x_div = grouped_historical_dividend_payout_dates.index
dividends.plot(x_div, y_div, linewidth=1.0)
plt.show()



