import os
from dotenv import load_dotenv
import interactions

# Load the token from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
if TOKEN is None:
    raise ValueError("No token found in .env file")

# Initialize the bot client
bot = interactions.Client(token=TOKEN)

# Define a slash command using the correct decorator for v5+
@interactions.slash_command(
    name="hello",  # The name of the command in the / menu
    description="Say hello to the bot"  # Command description shown in the menu
)
async def hello(ctx: interactions.SlashCommand):
    await ctx.send("Hello, world!")  # Bot responds with a message

# Run the bot
try:
    bot.start()
except interactions.errors.LibraryException as e:
    print(f"An error occurred: {e}")
except KeyboardInterrupt:
    print("Bot stopped by user.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


