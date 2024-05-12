import discord
from discord.ext import commands
from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime
import service_key.json

# Initialize Discord bot
bot = commands.Bot()

# Google Sheets API setup
SPREADSHEET_ID = 'insert spreadsheet id'
RANGE_NAME = 'Form Responses 1!B:C'
SERVICE_ACCOUNT_FILE = service_key.json

# Authenticate using service account credentials
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)

# Build the Google Sheets service
service = build('sheets', 'v4', credentials=creds)

# Function to check birthdays
async def check_birthdays():
    now = datetime.now()
    current_date = now.strftime("%m/%d")  # Format: MM/DD
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])
    
    if not values:
        print('No data found.')
    else:
        for row in values:
            if len(row) >= 2 and row[1] == current_date:
                # Send birthday message to Discord channel
                channel = bot.get_channel('channel_id')
                await channel.send(f"Happy Birthday, {row[0]}!")

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

    # Check birthdays when bot is ready
    await check_birthdays()

# Run the bot
bot.run('bot_id')
