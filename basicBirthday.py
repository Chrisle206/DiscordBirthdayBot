import discord
from discord.ext import tasks
from datetime import datetime

# Initialize intents
intents = discord.Intents.default()
intents.presences = True
intents.members = True

# Initialize Discord bot
bot = discord.Client(intents=intents)

# Define a list of tuples containing people's names and their birthdays
birthday_data = [

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

# Schedule the check_birthdays function to run daily
@tasks.loop(hours=24)
async def scheduled_check_birthdays():
    await check_birthdays()

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    scheduled_check_birthdays.start()  # Start the scheduled task when the bot is ready

# Run the bot
bot.run('insert discord bot key')
