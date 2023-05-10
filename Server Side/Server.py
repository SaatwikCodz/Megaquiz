import discord
from discord.ext import commands

def run():
    bot = commands.Bot(command_prefix = '!', intents = discord.Intents.all())
    @bot.event
    async def on_ready():
        print(bot.user + ' is Up Up and Away!!')
    async def on_message(message):
        if message.author == bot.user:
            return
        if message.content.startswith('Sending-Signup'):
            