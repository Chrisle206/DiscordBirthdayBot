import discord
from discord.ext import commands
from datetime import datetime

# Initialize intents
intents = discord.Intents.default()
intents.presences = True
intents.members = True

# Initialize Discord bot
bot = discord.Client(intents=intents)

# Define a list of tuples containing people's names and their birthdays
birthday_data = [
    #example: ("Alice", "01/15"),
    ("Beza", "03/30"),
    ("Karla Carrera", "01/21"),
    ("Amir", "02/26"),
    ("Evert Freeman", "05/02"),
    ("Kevin Le", "05/29"),
    ("Yohana Gebregziabher", "07/16"),
    ("Alex", "07/16"),
    ("Ivan Matev", "07/27"),
    ("Austin Nguyen", "08/28"),
    ("Julia", "09/04"),
    ("Haylee", "09/07"),
    ("Minh", "09/08"),
    ("Ariana Simon", "10/21"),
    ("Angie", "10/26"),
    ("Ernesto Martinez", "11/11"),
    ("BiniyamG", "12/18"),
    ("Luis Huizar", "11/25"),
    # Add more entries as needed
]

# Function to check birthdays
async def check_birthdays():
    try:
        now = datetime.now()
        current_date = now.strftime("%m/%d")  # Format: MM/DD
        
        # Get the channel object
        channel = bot.get_channel(1221889322387505300)  # Replace with your channel ID
        
        for name, birthday in birthday_data:
            if birthday == current_date:
                # Send birthday message to Discord channel
                await channel.send(f"@everyone Wish {name} a Happy Birthday!")
    except Exception as e:
        print(f"An error occurred while sending birthday message: {e}")

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

    # Check birthdays when bot is ready
    await check_birthdays()

# Run the bot
bot.run('insert Bot ID')
