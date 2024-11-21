import os
import pandas as pd
from workbook import save_to_workbook
from data import download_data, import_csv

def yahoo():
    with open("symbols.txt") as f:
        symbols = f.read().splitlines()

    data = download_data(symbols)
    data = pd.DataFrame(data).dropna()

    starting_date = data.index[0].strftime('%Y-%m-%d')

    print(f'Correlation Matrix (since {starting_date}):')
    correlation_matrix = data.corr(method='pearson')
    print(correlation_matrix)

    save_to_workbook(correlation_matrix, starting_date)

def csv():
    data = import_csv()
    data = data.apply(pd.to_numeric, errors='coerce')
    data = data.dropna()

    data = data.pct_change().dropna()
    starting_date = data.index[0]

    print(f'Correlation Matrix (since {starting_date}):')
    correlation_matrix = data.corr(method='pearson')
    print(correlation_matrix)

    save_to_workbook(correlation_matrix, starting_date)

yahoo()