import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ticker = input("Enter company ticker:") - TEMPORARY COMMENTED DURING DEBUGGING
company_ticker = "LGEN.L"
whole_company_data = yf.Ticker(company_ticker)

hist_data = whole_company_data.history(start="2000-01-01")
hist_div_payout_dates = hist_data[hist_data.Dividends != 0]  # filters old to remove entries = 0
hist_div_data = hist_div_payout_dates['Dividends']

grp_hist_div_payout_dates = hist_div_data.resample('A').sum()
#print(grp_hist_div_payout_dates)

div_yield = 100*hist_div_data/hist_data['Close']
div_yield = div_yield.dropna()
grp_div_yield = div_yield.resample('A').mean()
print(grp_div_yield)

# #subplot creation
fig, (close, dividends, dividend_yield) = plt.subplots(nrows=3, ncols=1)

# Historical cLose price plot
y = hist_data['Close']
x = hist_data.index
close.plot(x, y, linewidth=1.0)

# Dividend plot
y_div = grp_hist_div_payout_dates.iloc[:, ]
x_div = grp_hist_div_payout_dates.index
dividends.bar(x_div, y_div,100)

#Dividend yield plot
y_ydiv = grp_div_yield.iloc[:,]
x_ydiv = grp_div_yield.index
dividend_yield.bar(x_ydiv, y_ydiv, 100)
plt.show()