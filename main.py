from datetime import datetime

import discord
from discord.ext import commands

import time
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
                      'cogs.serverStuff'
                      ]

bot = commands.Bot(command_prefix=get_prefix,
                   description='Using Eviees cog rewrite',
                   help_command=None, intents=discord.Intents.all())

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


@bot.event
async def on_member_join(member: discord.Member):
    print("\n--------------\n")
    print(time.strftime("Joined at:\n" + "%H:%M:%S\n"))
    welEmb = discord.Embed(title='A new Homie just arrived!',
                               description=f"Welcome to The Fragment, {member.mention} "
                                           "We're happy to add you to this insanity."
                               , timestamp=datetime.utcnow())
    welEmb.add_field(name="Your first step: ", value="Read our rules found at: <#694715714724167731>\n"
                                                         "Then get some roles from <#694715780583129108>\n"
                                                        "*if you're a D2 player, it's very important to pick"
                                                         "up the Destiny Role.*")

    welEmb.add_field(name='Finally....', value='Be sure to tag <@&694709812528677008>', inline=False)
    welEmb.set_thumbnail(url='https://i.imgur.com/0MEtXDZ.png')
    welEmb.color = discord.Color.from_rgb(239, 124, 243)
    wel_cum = bot.get_channel(694725683242467398)
    await wel_cum.send(embed=welEmb)


bot.run(token, bot=True, reconnect=True)
