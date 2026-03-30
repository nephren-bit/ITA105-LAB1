import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Ngopt\Downloads\ITA105_Lab\ITA105_Lab_1.csv")  

print("Kích thước dữ liệu:", df.shape)
print(df.describe())



missing = df.isnull().sum()
print(missing)
df['Price'] = df['Price'].fillna(df['Price'].mean())
df['StockQuantity'] = df['StockQuantity'].fillna(df['StockQuantity'].median())
df['Category'] = df['Category'].fillna(df['Category'].mode()[0])
df_drop = df.dropna()
print("Kích thước sau fill:", df.shape)
print("Kích thước sau drop:", df_drop.shape)

print("Price <= 0:", (df['Price'] <= 0).sum())
print("Stock < 0:", (df['StockQuantity'] < 0).sum())
print("Rating lỗi:", ((df['Rating'] < 0) | (df['Rating'] > 5)).sum())

df_clean = df[
    (df['Price'] > 0) &
    (df['StockQuantity'] >= 0) &
    (df['Rating'].between(0, 5))
]

print("Before:", df.shape)
print("After:", df_clean.shape)
print(df_clean.head())

df['Price_Smoothed'] = df['Price'].rolling(window=3).mean()
plt.figure()

plt.plot(df['Price'], label='Original Price')
plt.plot(df['Price_Smoothed'], label='Smoothed Price')

plt.legend()
plt.title("Price Smoothing")
plt.show()

df['Category'] = df['Category'].str.lower()
df['Description'] = df['Description'].str.strip()
df['Description'] = df['Description'].str.replace(r'\s+', ' ', regex=True)
exchange_rate = 24000
df['Price_VND'] = df['Price'] * exchange_rate
print(df[['Category', 'Description', 'Price', 'Price_VND']].head())