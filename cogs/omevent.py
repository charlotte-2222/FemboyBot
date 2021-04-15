import random
import discord
from discord import emoji
from discord.ext import commands


class OnMessCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        lines = open('text_dir/insults.txt').read().splitlines()
        myfile = discord.File('images/video0(1).mp4')
        if message.author.bot:
            return  # ignore all bots
        content = message.content.casefold()
        if "pog" in content:
            await message.reply("Shut the fuck up with that cringe ass bullshit")
        if "trials" in content:
            await message.reply(random.choice(lines))
        if "fuck you fembot" in content:
            await message.reply(f"fuck you {message.author.mention}")
        if "good morning" in content:
            await message.reply(f"Morning {message.author.mention}!")
        if "goodnight" in content:
            await message.reply(f"Night {message.author.mention}!")
        if "nerd" in content:
            await message.reply(file=myfile)
            await message.reply("nErD. Get fucked dumbass.")

    @commands.Cog.listener()
    async def on_message(self, message):
        ff = discord.File('images/insane.mp4')
        if message.author.bot:
            return
        content = message.content.casefold()
        if "welcome to the fragment" in content:
            await message.reply(file=ff)


def setup(bot):
    bot.add_cog(OnMessCog(bot))
