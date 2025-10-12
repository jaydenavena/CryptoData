
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import copy

csv_path = os.path.expanduser(r"~\OneDrive\Documents\50_coins_crypto_1h_data_cryptocompare\BTCUSDT_1h.csv")
df = pd.read_csv(csv_path)
df = df.set_index(pd.DatetimeIndex(df['timestamp'].values))
df.drop(['timestamp'], inplace = True, axis = 1)
#drops the first column that was just numbering the rows, makes timestamp the first/organizer one ^
df = df.head(200)

#simple moving average function
def SMA(data, period = 30, column = 'close'):
    return data[column].rolling(window = period).mean()

#datasets
df['SMA'] = SMA(df, 21) 
df['Simple_Returns'] = df.pct_change(1)['close']
df['Log_Returns'] = np.log(1+df['Simple_Returns'])
df['Ratios'] = df['close'] / df['SMA']
# print(df['Ratios'].describe())

percentiles = [5, 25, 50, 75, 95]
ratios = df['Ratios'].dropna()
percentile_values = np.percentile(ratios, percentiles)
# print(percentile_values)

plt.figure(figsize=(12,6))
plt.title('Ratios')
df['Ratios'].dropna().plot(legend = True)
plt.axhline(percentile_values[0], c='green', label = '5th Percentile')
plt.axhline(percentile_values[2], c='yellow', label = '50th Percentile')
plt.axhline(percentile_values[-1], c='red', label = '95th Percentile')
plt.ylabel('Deviation')
plt.xlabel('Time')
plt.legend()

buy = percentile_values[0] #buy the 5th percentile
sell = percentile_values[-1] #sell the 95th
df['Positions'] = np.where(df.Ratios > sell, -1, np.nan)
df['Positions'] = np.where(df.Ratios < buy, 1, df['Positions'])
df['Positions'] = df['Positions'].ffill()

df['Buy'] = np.where(df.Positions == 1 , df['close'], np.nan)
df['Sell'] = np.where(df.Positions == -1 , df['close'], np.nan)

plt.figure(figsize = (12,6))
plt.title("Buy/Sell Signals")
plt.plot(df['close'], alpha = 0.3, label = 'Close')
plt.plot(df['SMA'], alpha = 0.5, label = 'SMA')
plt.scatter(df.index, df['Buy'], color = 'green', label = 'BUY', marker = '^', alpha = 0.8)
plt.scatter(df.index, df['Sell'], color = 'red', label = 'SELL', marker = 'v', alpha = 0.8)
plt.xlabel("Time")
plt.ylabel("Close Price")
plt.legend()
plt.show()

