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
            qr_1 = query.Query(consts.ACTION_STOCK_QUERY, symbol)
            return qr_1

        elif(len(msgArr) > 1):
            secondArg = msgArr[1].lower()

            # Information about the company
            if(secondArg == "info"):
                qr_2 = query.Query(consts.ACTION_INFO, symbol)
                qr_2.showInfo = True
                return qr_2

            # Last earnings & next earnings
            elif(secondArg == "earnings"):
                qr_3 = query.Query(consts.ACTION_EARNINGS, symbol)
                qr_3.showEarnings = True
                return qr_3

            # Stock's Price Target
            elif(secondArg == "pt"):
                qr_4 = query.Query(consts.ACTION_PT, symbol)
                qr_4.showPriceTarget = True
                return qr_4

            # News about a stock
            elif(secondArg == "news"):
                qr_5 = query.Query(consts.ACTION_NEWS, symbol)
                qr_5.showNews = True
                return qr_5

            # Stock chart
            elif(secondArg in consts.STOCK_CHARTS_PERIODS):
                try:
                    thirdArg = msgArr[2].lower()

                    # Show chart of volume
                    if(thirdArg == "volume"):
                        qr_6b = query.Query(consts.ACTION_CHART_VOLUME, symbol)
                        qr_6b.period = secondArg
                        qr_6b.showVolume = True
                        return qr_6b
                    else:
                        qr_else_6b = query.Query(
                            consts.ACTION_TYPE_MSG, symbol)
                        qr_else_6b.message = "Invalid charts option on {}".format(
                            symbol)
                        return qr_else_6b

                except:
                    # Show regular chart
                    qr_6a = query.Query(consts.ACTION_CHART, symbol)
                    qr_6a.period = secondArg
                    return qr_6a

            # Options chain
            elif(secondArg == "options"):
                try:
                    thirdArg = msgArr[2]
                    qr_7 = query.Query(consts.ACTION_CHART, symbol)
                    qr_7.optionsDate = thirdArg
                    return qr_7
                except:
                    qr_else_7 = query.Query(consts.ACTION_TYPE_MSG, symbol)
                    qr_else_7.message = "Invalid date for options on ${}".format(
                        symbol.upper())
                    return qr_else_7

            else:
                qr_else = query.Query(consts.ACTION_TYPE_MSG, symbol)
                qr_else.message = "Invalid action on ${}".format(symbol.upper())
                return qr_else

    else:
        qr_0 = query.Query(consts.ACTION_TYPE_NONE, "NONE")
        return qr_0
