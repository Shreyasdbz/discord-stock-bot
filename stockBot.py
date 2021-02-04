# Libraries
import os
from dotenv import load_dotenv
# Custom src
from src import discordClient

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
IEX_TOKEN = os.getenv("IEX_TOKEN")

discordClient.runClient(DISCORD_TOKEN, IEX_TOKEN)
