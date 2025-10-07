import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import copy


csv_path = os.path.expanduser(r"~\OneDrive\Documents\50_coins_crypto_1h_data_cryptocompare\BTCUSDT_1h.csv")


df = pd.read_csv(csv_path)
df = df.head(20)
# print(df.head(5))



plt.figure(figsize = (12, 6))
plt.plot(df["timestamp"], df["close"], label = "hr close")

plt.xlabel("Time")
plt.xticks(rotation = 45)
plt.ylabel("Close Price")
plt.title("BTC")
plt.legend()

plt.show()

# def load_csv(csv_path):
#     with open(csv_path, "r") as f:
#         rows = csv.DictReader(f)
#         rows = list(rows)
#         rows = copy.deepcopy(rows)
#         return rows

# BTC = load_csv(csv_path)
# for row in BTC:
#     print(row)
