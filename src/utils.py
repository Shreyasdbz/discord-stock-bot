from datetime import datetime
from src import consts

# ---------------------------Discord Client Utilities---------------------------

# Checks from database if the channel is valid or not
# @params: channel id
# Returns: True if valid / False if invalid


def isValidChannel(channelId):
    return True


# ---------------------------Finance Client Utilities---------------------------

# Get the type of market hours right now
# @params: none
# Returns: Market hours types (string consts)
def getMarketHours():
    # 1) Check date to compare against holidays / weekends
    # 2) Check hours
    print(datetime.utcnow())
    pass


# Based on if the stock is +/-, return corrosponding color
# @params: currentPrice(float)
#          last closing price
# Returns: color (const)
def getStockColor(currentPrice, lastClose):
    if(currentPrice >= lastClose):
        return consts.COLOR_POSITIVE
    elif(currentPrice < lastClose):
        return consts.COLOR_NEGATIVE
    else:
        return consts.COLOR_NEUTRAL


# Get the % change for the day
# @params: currentPrice(float)
#          last close (float)
# Returns: percentChange (float)
def getPercentChange(currentPrice, lastClose):
    change = ((currentPrice - lastClose)/lastClose)*100
    change = round(change, 2)
    return change


def getFormattedLargeNumber(largeNum):
    num = "{:,}".format(largeNum)
    return num
