from datetime import datetime

# Get the type of market hours right now
# @params: none
# Returns: Market hours types (string consts)
def getMarketHours():
    # 1) Check date to compare against holidays / weekends
    # 2) Check hours 
    print(datetime.utcnow())
    pass