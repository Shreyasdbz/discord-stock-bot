import discord
from src import utils
from src import parser

# ------------------------------------------------------
# Primary function that is the entry point for the program
# Handles all discord's event driven functions
# @params: discordToken (string)
#          iexToken (string)
# Return:  none
# ------------------------------------------------------
def runClient(discordToken, iexToken):
    # 
    # Initialize the discord client
    client = discord.Client()

    # 
    # Runs when the client gets online for the first time
    @client.event
    async def on_ready():
        # Setting `Watching ` status
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you ... 👀"))
        print("Discord bot client has started ...")

    # 
    # Runs when a new message is received (no matter what guild/channel/type of message)
    @client.event
    async def on_message(message: discord.message.Message):
        if(message.author != client.user):
            # Check from database if the channel has been added to allowed channels
            if(utils.isValidChannel(message.channel.id)):
                actionType = ""
                # Use finance client here to figure out reply
                pass
            

    # 
    # Run the client in listening mode
    client.run(discordToken)
