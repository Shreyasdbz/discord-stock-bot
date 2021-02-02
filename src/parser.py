from src import consts
from src import query
from src import utils

# Parses the message text and determines which action will be taken
# @params: message (string)
# Returns: 
def getMessageType(message):
    if(message[0] == "$"):
        msgArr = message.split(" ")
        symbol = msgArr[0]
        symbol = symbol[1:]

        # Simple price query
        if(len(msgArr) == 1):
            qr_1 = query.Query(consts.ACTION_STOCK_QUERY , symbol)
            print("CASE 1 -- ACTION: {} , SYMBOL : {}".format(qr_1.action, qr_1.symbol))
            return qr_1

        
        elif(len(msgArr) > 1):
            secondArg = msgArr[1].lower()

            # Information about the company 
            if(secondArg == "info"):
                qr_2 = query.Query(consts.ACTION_INFO , symbol)
                qr_2.showInfo = True
                print("CASE 2 -- ACTION: {} , SYMBOL : {}".format(qr_2.action, qr_2.symbol))
                return qr_2

            # Last earnings & next earnings
            elif(secondArg == "earnings"):
                qr_3 = query.Query(consts.ACTION_EARNINGS , symbol)
                qr_3.showEarnings = True
                print("CASE 3 -- ACTION: {} , SYMBOL : {}".format(qr_3.action, qr_3.symbol))
                return qr_3
          
            # Stock's Price Target 
            elif(secondArg == "pt"):
                qr_4 = query.Query(consts.ACTION_PT , symbol)
                qr_4.showPriceTarget = True
                print("CASE 4 -- ACTION: {} , SYMBOL : {}".format(qr_4.action, qr_4.symbol))
                return qr_4

            # News about a stock
            elif(secondArg == "news"):
                qr_5 = query.Query(consts.ACTION_NEWS , symbol)
                qr_5.showNews = True
                print("CASE 5 -- ACTION: {} , SYMBOL : {}".format(qr_5.action, qr_5.symbol))
                return qr_5
            
            # Stock chart
            elif(secondArg in consts.STOCK_CHARTS_PERIODS):
                try:
                    thirdArg = msgArr[2].lower()

                    # Show chart of volume
                    if(thirdArg == "volume"):
                        qr_6b = query.Query(consts.ACTION_CHART_VOLUME , symbol)
                        qr_6b.period = utils.parseChartPeriod(secondArg)
                        qr_6b.showVolume = True
                        print("CASE 6 -- ACTION: {} , SYMBOL : {}".format(qr_6b.action, qr_6b.symbol))
                        return qr_6b
                    else:
                        qr_else_6b = query.Query(consts.ACTION_TYPE_MSG , symbol)
                        qr_else_6b.message = "Invalid charts option on {}".format(symbol)
                        print("CASE ELSE 7 -- ACTION: {} , SYMBOL : {}".format(qr_else_6b.action, qr_else_6b.symbol))
                        return qr_else_6b

                except:
                    # Show regular chart
                    qr_6a = query.Query(consts.ACTION_CHART , symbol)
                    qr_6a.period = utils.parseChartPeriod(secondArg)
                    print("CASE 6 -- ACTION: {} , SYMBOL : {}".format(qr_6a.action, qr_6a.symbol))
                    return qr_6a

            # Options chain
            elif(secondArg == "options"):
                try:
                    thirdArg=msgArr[2]
                    qr_7 = query.Query(consts.ACTION_CHART , symbol)
                    qr_7.optionsDate = thirdArg
                    print("CASE 7 -- ACTION: {} , SYMBOL : {}".format(qr_7.action, qr_7.symbol))
                    return qr_7
                except:
                    qr_else_7 = query.Query(consts.ACTION_TYPE_MSG , symbol)
                    qr_else_7.message = "Invalid date for options on {}".format(symbol)
                    print("CASE ELSE 7 -- ACTION: {} , SYMBOL : {}".format(qr_else_7.action, qr_else_7.symbol))
                    return qr_else_7

            else:           
                qr_else = query.Query(consts.ACTION_TYPE_MSG , symbol)
                qr_else.message = "Invalid action on {}".format(symbol)
                print("CASE ELSE -- ACTION: {} , SYMBOL : {}".format(qr_else.action, qr_else.symbol))
                return qr_else
            
    else:
        qr_0 = query.Query(consts.ACTION_TYPE_NONE, "NONE")
        print("CASE 0 -- ACTION: {} , SYMBOL : {}".format(qr_0.action, qr_0.symbol))
        return qr_0