import os
from dotenv import load_dotenv
import discord
from discord import app_commands

# Load the token from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
if TOKEN is None:
    raise ValueError("No token found in .env file")

# Initialize the bot client
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Define a slash command using the correct decorator for v5+
@tree.command(
    name="hello",  # The name of the command in the / menu
    description="Say hello to the bot"  # Command description shown in the menu
)
async def hello(interaction):
    await interaction.response.send_message("Hello there!")  # Bot responds with a message

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)