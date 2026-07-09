import discord
import random
from discord.ext import commands

import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    # Ignore other bots
    if message.author.bot:
        return

    text = message.content.lower()

    # Dictionary of trigger words and their replies
    responses = {
        "tay": [
            "iegjeifijdvjcds",
            "Tao will unban Tay soon btw.",
            "Tay pls autograph asldhwgjrf"
        ],

        "ban": [
            "You just reminded me time to go false ban some niggas now 🤣🤣🤣",
            "Your banned next kid",
            "who to ban next 🤣"
        ],

        "X": [
            "Hey nigga",
            "Stop saying my name... I really d-d-dont like it when people do that..",
            "Say my name again and ur banned kid"
        ],

        "tank": [
            "that tank guy is pretty cool",
            "Ill unban tank at some point",
            "asldkwdejk"
        ]
        
    }

    # Check every trigger word
    for word, replies in responses.items():
        if word in text:
            await message.channel.send(random.choice(replies))
            break  # Stops after the first matching word

    await bot.process_commands(message)

bot.run(TOKEN)