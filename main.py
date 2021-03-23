import discord
from discord.ext import commands

import sys, traceback
import asyncio
import time, datetime
from config import token


def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    prefixes = ['>>']
    if not message.guild:
        return '?'
    return commands.when_mentioned_or(*prefixes)(bot, message)


initial_extensions = ['cogs.admin',
                      'cogs.fun',
                      'cogs.hentai',
                      'cogs.imageFun',
                      'cogs.missc',
                      'cogs.owner',
                      'cogs.reddit',
                      'cogs.redditNSFW',
                      'cogs.serverStuff',
                      'cogs.welcome'
                      ]

bot = commands.Bot(command_prefix=get_prefix,
                   description='Using Eviees cog rewrite',
                   help_command=None)

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)


@bot.event
async def on_ready():
    print("FemBot online\n")
    print(f"Logged in as {bot.user.name} - {bot.user.id}\n")
    print("--------------")
    print(time.strftime(f"Time at start:\n"
                        "%H:%M:%S\n"
                        "%m/%d/%Y\n"))


bot.run(token, bot=True, reconnect=True)
