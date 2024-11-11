import pandas as pd
from workbook import save_to_workbook
from data import download_data

with open("symbols.txt") as f:
    symbols = f.read().splitlines()

data = download_data(symbols)
data = pd.DataFrame(data).dropna()

starting_date = data.index[0].strftime('%Y-%m-%d')

print(f'Correlation Matrix (since {starting_date}):')
correlation_matrix = data.corr(method='pearson')
print(correlation_matrix)

save_to_workbook(correlation_matrix, starting_date)