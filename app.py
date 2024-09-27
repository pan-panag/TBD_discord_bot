import os
from dotenv import load_dotenv
import discord
from discord import app_commands

# Load the commands from the commands directory
from commands.general import load_commands as general_setup

# Load the token from the .env file
if not load_dotenv():
    raise FileNotFoundError("No .env file found")

TOKEN = os.getenv('DISCORD_TOKEN')
if TOKEN is None:
    raise ValueError("No token found in .env file")

# Initialize the bot client
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


def print_list(l: list, msg: str):
    print(msg + ":")
    for i in l:
        print(f"\t{i}")
    print("End of " + msg)

async def setup_commands():
    await general_setup(tree)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    await setup_commands()
    
    synced = await tree.sync()
    print_list(synced, "Synced commands")


if __name__ == '__main__':
    try:
        client.run(TOKEN)
    except discord.errors.LoginFailure:
        print("Invalid token provided")
    except discord.errors.HTTPException as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

