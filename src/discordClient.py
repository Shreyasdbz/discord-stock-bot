import discord
from src import financeClient
from src import parser
from src import utils
from src import consts

# ------------------------------------------------------
# Primary function that is the entry point for the program
# Handles all discord's event driven functions
# @params: discordToken (string)
#          iexToken (string)
# Return:  none
# ------------------------------------------------------
def runClient(discordToken, iexToken):

    # Initialize the discord client
    client = discord.Client()
    # Finance client to get data from
    finance = financeClient.getFinanceClient(iexToken)

    # 
    # Runs when the client gets online for the first time
    @client.event
    async def on_ready():
        # Set `Watching` status
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you ... 👀"))
        print("Discord bot client has started ...")

    # 
    # Runs when a new message is received (no matter what guild/channel/type of message)
    @client.event
    async def on_message(message: discord.message.Message):
        if(message.author != client.user):
            # Check from database if the channel has been added to allowed channels
            if(utils.isValidChannel(message.channel.id)):
                # Figure out what action will be taken based on the message
                qr = parser.getMessageType(message.content)
                # Use finance client here to figure out reply

                # -- No action, keep listening
                if(qr.action == consts.ACTION_TYPE_NONE):
                    print("---------------------------")

                if(qr.action == consts.ACTION_TYPE_MSG):
                    print("The message is: {}".format(qr.message))
                    print("---------------------------")

                # -- Send a simple stock price message
                elif(qr.action == consts.ACTION_STOCK_QUERY):
                    currentPrice = finance.getCurrentPrice(qr.symbol)
                    print(currentPrice)
                    print("---------------------------")
                    await message.channel.send("{} is at ${}".format(qr.symbol, currentPrice))


    # 
    # Run the client in listening mode
    client.run(discordToken)
