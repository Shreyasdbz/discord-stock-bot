import pyEX as px
import yfinance as yf
import stockquotes as sq

# Serves as the api for getting finance queries answered
# @params: iexToken (str)
class FinanceClient:
    def __init__(self, iexToken):
        self.client =  px.Client(api_token=iexToken, version="v1")

    # Simply returns the price of the symbol provided
    # @params: symbol name (str)
    # Returns: stock price (float)
    def getCurrentPrice(self, symbol):
        stock = sq.Stock(symbol)
        return stock.current_price

    # Simply returns some information about a company
    # @params: symbol name (str)
    # Returns: information (str)
    def getInfo(self, symbol):
        pass

# -------------------------------
# Starts the client 
# @params: iexToken (str)
def getFinanceClient(iexToken):
    client = FinanceClient(iexToken)
    return client