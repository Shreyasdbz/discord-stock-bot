from datetime import datetime
from src import consts

# Get the type of market hours right now
# @params: none
# Returns: Market hours types (string consts)
def getMarketHours():
    # 1) Check date to compare against holidays / weekends
    # 2) Check hours 
    print(datetime.utcnow())
    pass

# Checks from database if the channel is valid or not
# @params: channel id
# Returns: True if valid / False if invalid
def isValidChannel(channelId):
    return True


def parseChartPeriod(text):
    return consts.STOCK_CHART_NONE