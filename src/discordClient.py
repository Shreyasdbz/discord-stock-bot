import os
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
                    pass

                # -- Error message to send back to the user
                if(qr.action == consts.ACTION_TYPE_MSG):
                    send = discord.Embed(color=consts.COLOR_NEUTRAL)
                    send.add_field(
                        name="Error:", value="{}".format(qr.message))
                    await message.channel.send(embed=send)

                # -- Send a simple stock price message
                elif(qr.action == consts.ACTION_STOCK_QUERY):
                    res = finance.getCurrentPrice(qr.symbol)
                    send = discord.Embed(color=res.color)
                    send.add_field(name="{}:  ${}".format(
                        res.symbol.upper(), res.price), value="{}% for the day".format(res.percentChange), inline=False)
                    await message.channel.send(embed=send)

                    imagePath = os.path.join('src', 'images', 'stonks.png')
                    await message.channel.send(file=discord.File(imagePath))

                # -- Get information about a company
                # ~TODO~
                elif(qr.action == consts.ACTION_INFO):
                    finance.getInfo(qr.symbol)

                # -- Get a price chart of a stock for a specific period
                # ~TODO~
                elif(qr.action == consts.ACTION_CHART):
                    res = finance.getChart_price(qr.symbol, qr.period)
                    await message.channel.send(file=discord.File(res.chartImage_path))

                # -- Get a volume chart of a stock for a specific period
                # ~TODO~
                elif(qr.action == consts.ACTION_CHART_VOLUME):
                    res = finance.getChart_volume(qr.symbol, qr.period)
                    await message.channel.send(file=discord.File(res.chartImage_path))

    #
    # Run the client in listening mode
    client.run(discordToken)
