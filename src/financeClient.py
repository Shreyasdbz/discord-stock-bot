import pandas as pd
import pyEX as px
import yfinance as yf
import stockquotes as sq

from src import utils
from src import result

# Serves as the api for getting finance queries answered
# @params: iexToken (str)


class FinanceClient:
    def __init__(self, iexToken):
        self.client = px.Client(api_token=iexToken, version="v1")

    # Simply returns the price of the symbol provided
    # @params: symbol name (str)
    # Returns: currentPrice (float)
    def getCurrentPrice(self, symbol):
        stockQ = sq.Stock(symbol)
        stockY = yf.Ticker(symbol)
        res = result.Result(symbol=symbol)
        res.price = stockQ.current_price
        lastClose = stockY.info['previousClose']
        res.percentChange = utils.getPercentChange(res.price, lastClose)
        res.color = utils.getStockColor(res.price, lastClose)
        return res

    # Returns some information about a company
    # @params: symbol name (str)
    # Returns: arr[string]
    def getInfo(self, symbol):
        stockQ = sq.Stock(symbol)
        stockY = yf.Ticker(symbol)
        info = stockY.info
        res = result.Result(symbol=symbol)
        res.color = utils.getStockColor(
            currentPrice=stockQ.current_price, lastClose=info['previousClose'])
        pass

    # Provides the next earnings date and last earnings' result
    # @params: symbol name (str)
    # Returns: arr[string]
    def getEarnings(self, symbol):
        pass

    # Gives back the current price target of the stock
    # @params: symbol name (str)
    # Returns: arr[string]
    def getPriceTarget(self, symbol):
        pass

    # Provides some aggregated news about a company
    # @params: symbol name (str)
    # Returns: arr[string]
    def getNews(self, symbol):
        pass

    # Gives back a candle chart of specific period of a stock's price
    # @params: symbol name (str)
    # Returns: arr[string]
    def getChart_price(self, symbol, period):
        stockY = yf.Ticker(symbol)
        hist =  stockY.history(period=period)
        print(hist)
        hist.to_csv()
        
        pass

    # Gives back a chart of specific period of a stock's volume
    # @params: symbol name (str)
    # Returns: arr[string]
    def getChart_volume(self, symbol, period):
        pass


# -------------------------------
# Starts the client
# @params: iexToken (str)
def getFinanceClient(iexToken):
    client = FinanceClient(iexToken)
    return client
