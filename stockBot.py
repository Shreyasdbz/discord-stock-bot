# Libraries
import os
from dotenv import load_dotenv
# Custom src
from src import discordClient
from src import financeClient
from src import utils

load_dotenv()
DISCORD_CLIENT_TOKEN = os.getenv("DISCORD_CLIENT_TOKEN")
IEX_TOKEN = os.getenv("IEX_TOKEN")

# All the servers where stockBot is currently active on
activeGuilds = ["$Moves", "Bread Winners"]

# discordClient.runClient(DISCORD_CLIENT_TOKEN, IEX_TOKEN)
# fc = financeClient.getFinanceClient(IEX_TOKEN)
# fc.getCurrentPrice("AAPL")

utils.getMarketHours()
