from tkinter import *
from tkinter import filedialog as fd
def file(title):
    the_file = fd.askopenfilename(  
      title = title,  
      filetypes = [("Text Files", "*.*")]  
      )  
def client(uname: string, i = 0, message: str):
    import discord
    from discord.ext import commands
    a = commands.Bot(command_prefix = '!', intents = discord.Intents.all())
    @a.event
    async def on_ready():
        print(f'{a.user} is online')
        b = a.get_channel(1095047694499708988)
        b.send(f'{uname} is trying to communicate {len(uname)}')
    @a.event
    async def on_message(message):
        if message.author == a.user:
            return
        if message.content.startswith(uname):
            messages = message.content[:len(uname)]
            if messages.startswith(' '):
                messages = messages[0:]
            if messages.startswith('Ready'):
                q = uname + message + str(len(uname))
                message.channel.send(q)
            if messages.startswith('Error Code:'):
                l = message.content.split(':')
                code = l[1]
            if messages.startswith