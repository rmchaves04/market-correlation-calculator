import os
import pandas as pd
import yfinance as yf

def download_data(symbols):
    data = {}
    for symbol in symbols:
        data[symbol] = yf.download(symbol)['Close'].pct_change().dropna()
    return data

def import_csv():
    files = os.listdir('data')
    df = pd.DataFrame()

    for file in files:
        if file.endswith('.csv'):
            name = file.split('.')[0]
            data = pd.read_csv(f'data/{file}', index_col=0).dropna()
            data.columns = [name]
            df = pd.concat([df, data], axis=1)

    df = df.dropna()
    return df
