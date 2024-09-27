import discord
from discord import app_commands

# Define the hello command
@app_commands.command(
    name="hello",
    description="Say hello to the bot"
)
async def hello(interaction: discord.Interaction):
    # Bot responds with a message mentioning the user
    await interaction.response.send_message(f"Hello there, {interaction.user.mention}!")

# Define the ping command
@app_commands.command(
    name="ping",
    description="Check the bot's latency"
)
async def ping(interaction: discord.Interaction):
    # Respond with bot's latency
    await interaction.response.send_message(f"Pong! {round(interaction.client.latency * 1000)}ms")


# Setup function to register the commands
async def load_commands(tree: app_commands.CommandTree):
    tree.add_command(hello)
    tree.add_command(ping)
