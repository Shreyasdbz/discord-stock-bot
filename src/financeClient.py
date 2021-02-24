from typing import final
import pandas as pd
import pyEX as px
import yfinance as yf
import stockquotes as sq

from src import utils
from src import result
from src import consts

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
        a = 1+1
        return res

    # Returns some information about a company
    # @params: symbol name (str)
    # Returns: arr[string]
    def getInfo(self, symbol):
        stockQ = sq.Stock(symbol)
        stockY = yf.Ticker(symbol)
        info = stockY.info
        res = result.Result(symbol=symbol)
        res.price = stockQ.current_price
        res.logoUrl = info['logo_url']
        res.companyName = info['longName']
        res.companyDesc = info['longBusinessSummary']
        # res.color = utils.getStockColor(
        #     currentPrice=stockQ.current_price, lastClose=info['previousClose'])
        res.color = consts.COLOR_NEUTRAL
        # Company Sector
        try:
            res.infoFields_values.append(info['sector'])
            res.infoFields_labels.append('Sector')
        except:
            print("Couldn't get info ~ sector for {}".format(symbol))
        # Employees
        try:
            res.infoFields_values.append(info['fullTimeEmployees'])
            res.infoFields_labels.append('FullTime Employees')
        except:
            print("Couldn't get info ~ full time employees for {}".format(symbol))
        # Location
        try:
            company_location = info['city'] + ", " + \
                info['state'] + " " + info['country']
            res.infoFields_values.append(company_location)
            res.infoFields_labels.append('Location')
        except:
            print("Couldn't get info ~ location for {}".format(symbol))
        # Dividend
        try:
            res.infoFields_values.append(info['dividendRate'])
            res.infoFields_labels.append('Dividend Rate')
        except:
            print("Couldn't get info ~ dividend for {}".format(symbol))
        # Market Cap
        try:
            res.infoFields_values.append(
                "$" + str(utils.getFormattedLargeNumber(info['marketCap'])))
            res.infoFields_labels.append('Market Cap')
        except:
            print("Couldn't get info ~ marketcap for {}".format(symbol))
        # 52 Week High/Low
        try:
            high_low = "$" + str(info['fiftyTwoWeekHigh']) + \
                " / $" + str(info['fiftyTwoWeekLow'])
            res.infoFields_values.append(high_low)
            res.infoFields_labels.append('52 Week High/Low')
        except:
            print("Couldn't get info ~ 52 week for {}".format(symbol))
        # Short Ratio
        try:
            res.infoFields_values.append(info['shortRatio'])
            res.infoFields_labels.append('Short Ratio')
        except:
            print("Couldn't get info ~ short ration for {}".format(symbol))
        # Avg / Current Volume
        try:
            avg_current_vol = str(
                utils.getFormattedLargeNumber(info['averageVolume'])) + " / " + str(utils.getFormattedLargeNumber(info['volume']))
            res.infoFields_values.append(avg_current_vol)
            res.infoFields_labels.append('Average / Current Volume')
        except:
            print("Couldn't get info ~ avg/current volume for {}".format(symbol))
        # Profit Margins
        try:
            res.infoFields_values.append(info['profitMargins'])
            res.infoFields_labels.append('Profit Margins')
        except:
            print("Couldn't get info ~ avg/current volume for {}".format(symbol))

        return res
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
        hist = stockY.history(period=period)
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
