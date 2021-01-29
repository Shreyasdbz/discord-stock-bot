import discord

# Custom version of the discord client that will handle all communication
# @params:  discord client (discord client type)
class DiscordClient(discord.Client):

    # Runs whenever an initial connection is established
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    # Runs whenever a new message is received
    async def on_message(self, message):        
        print(message)

# Funtion that starts the client. Startpoint for the majority of the program
# @params: discordToken (str)
#          iexToken (str)
def runClient(discordToken, iexToken):
    dc = DiscordClient()
    dc.run(discordToken)

