import pandas as pd
import numpy as np
import matplotlib as plt
import csv
# # C:\Users\jayde\OneDrive\Documents\
# def load_csv(file_path):
#     with open(file_path, "r") as f:
#         rows = csv.DictReader(f)
#         print(rows)

# BTC = load_csv("..\\..\\50_coins_crypto_1h_data_cryptocompare\\BTCUSDT_1h.csv")
# for row in BTC:
#     print(row)



# file_path = r"..\..\OneDrive\Documents\50_coins_crypto_1h_data_cryptocompare\BTCUSDT_1h.csv"

# with open(file_path, "r") as f:
#     data = f.read()

# print(data[:200])  # first 200 characters


import os

csv_path = os.path.expanduser(r"~\OneDrive\Documents\50_coins_crypto_1h_data_cryptocompare\BTCUSDT_1h.csv")

with open(csv_path, "r") as f:
    data = f.read()

print(csv_path)
print(data[:200])

        
