import yfinance as yf

def download_data(symbols):
    data = {}
    for symbol in symbols:
        data[symbol] = yf.download(symbol)['Close']
    return data