from datetime import time, datetime

import discord
from discord.ext import commands
from main import bot


class WelcomeCog(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @bot.event
    async def on_member_join(member):
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
        wel_cum = bot.get_channel(698670684154363904)
        await wel_cum.send(embed=welEmb)