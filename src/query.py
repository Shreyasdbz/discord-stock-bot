from src import consts

class Query:
    def __init__(self, actionType, symbol):
        self.action = actionType
        self.symbol = symbol
        self.period = consts.STOCK_CHART_NONE
        self.optionsDate = ""
        self.showVolume = False
        self.showInfo = False
        self.showEarnings = False
        self.showPriceTarget = False
        self.showNews = False
        self.showReddit = False
        self.message = ""