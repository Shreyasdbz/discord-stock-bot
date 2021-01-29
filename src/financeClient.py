import pyEX
import yfinance as yf
import stockquotes

# Serves as the api for getting finance queries answered
# @params: iexToken (str)
class FinanceClient:
    def __init__(self, iexToken):
        self.client =  pyEX.Client(api_token=iexToken, version="v1")

    # Simply returns the price of the symbol provided
    # @params: symbol name (str)
    def getCurrentPrice(self, symbol):
        stock = stockquotes.Stock(symbol)
        print(stock.current_price)

    def getChart_weekly(self):
        pass

# Starts the client 
# @params: iexToken (str)
def getFinanceClient(iexToken):
    fc = FinanceClient(iexToken)
    return fc