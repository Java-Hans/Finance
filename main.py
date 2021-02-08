import yfinance as yf
import json

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #msft = yf.Ticker("SMWH.L")
    msft = yf.Ticker("BTC-USD")

    data = yf.download("BTC-USD XRP-USD", start="2021-02-01")
    # print(data['Close']['BTC-USD'])

    # tickers = yf.Tickers('msft aapl goog aame f gme WTBL')
    # ^ returns a named tuple of Ticker objects

    # access each ticker using (example)
    # print(tickers.tickers.MSFT.info)

    # print(tickers.tickers.AAPL.history(period="1mo"))
    # print(tickers.tickers.GOOG.actions)
    try:
        print(msft.info)
    except ValueError:
        print('can\'t find shit')


    # stock_dict = msft.info
    # for item in stock_dict:
    #     print(f'{item}: {stock_dict[item]}')
    # print(msft)


def crypto_checker():
    with open('cryptocurrencies.json') as f:
        crypto_data = json.load(f)
        looper = 0
        for point in crypto_data:
            print(f'{point}: {crypto_data[point]}')
            looper += 1
            if (looper > 9):
                break
