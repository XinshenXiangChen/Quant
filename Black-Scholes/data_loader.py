import matplotlib.pyplot as plt
import pandas as pd

df =  pd.read_csv("data/combined_options_data.csv")

def plot_volatility_smile():
    expiry = "07-01-2010"
    df_filtered = df[df['EXPIRE_DATE'] == expiry].sort_values('STRIKE')

    plt.figure(figsize=(10, 6))
    plt.plot(df_filtered['STRIKE'], df_filtered['C_IV'], label='Call IV', marker='o')
    plt.plot(df_filtered['STRIKE'], df_filtered['P_IV'], label='Put IV', marker='o')

    plt.title(f'Volatility Smile for Expiry: {expiry}')
    plt.xlabel('Strike Price')
    plt.ylabel('Implied Volatility')
    plt.legend()
    plt.grid(True)
    plt.show()

def df_head():
    print(df.head())
    print(df.columns)

if __name__ == "__main__":
    plot_volatility_smile()
    df_head()
