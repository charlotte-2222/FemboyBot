import asyncio
import time
from datetime import datetime
import discord
from discord.ext import commands
from config import token
from dotenv import load_dotenv
import traceback
from cogs import *

""""-----------------------------------------------"""
'''https://github.com/meew0/discord-bot-best-practices'''
"""
Trying to follow good practice
with Bot command calls. Simply using:
'!', '?', '.', etc., is problematic.
https://github.com/meew0/discord-bot-best-practices
---
Helpful:
https://github.com/Rapptz/discord.py
"""
def get_prefix(bot, message):
    prefixes = ['^']
    if not message.guild:
        return '?'
    return commands.when_mentioned_or(*prefixes),(bot,message)


initial_extensions = (
    'cogs.utilCog',
    'cogs.cogStuff',
    'cogs.fun',
    'cogs.welcome',
    'cogs.nsfw'
)

bot = commands.Bot(command_prefix=get_prefix)

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)


load_dotenv()
intents = discord.Intents.all()
intents.members = True
bot.remove_command("help")


@bot.event
async def on_ready():
    channel = bot.get_channel(694725683242467398)
    print("Ready to cum...uwu")
    print("--------------")
    print(time.strftime("Time at start:\n" + "%H:%M:%S\n" +
                        "%m/%d/%Y\n"))
    # st = 'images/'
    e = discord.Embed(title="Online!", timestamp=datetime.utcnow())
    e.set_image(url='https://i.imgur.com/eOI07Lj.jpg')
    e.color = discord.Color.magenta()
    await channel.send(embed=e)

    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game('with The Fragment'))
        await asyncio.sleep(45)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('with Jays mom'))
        await asyncio.sleep(45)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="Futa Fix 2"))
        await asyncio.sleep(45)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="For ^"))
        await asyncio.sleep(45)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='heavy moans'))
        await asyncio.sleep(45)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('Destiny 2 (Naked)'))
        await asyncio.sleep(45)
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game('Halo 3'))
        await asyncio.sleep(45)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('with all the Homies'))
        await asyncio.sleep(45)


bot.run(token, bot=True, reconnect=True)
