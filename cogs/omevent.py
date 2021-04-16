import random
import discord
from discord import emoji
from discord.ext import commands


class OnMessCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        insults = open('text_dir/insults.txt').read().splitlines()
        morning = open('text_dir/mornList.txt').read().splitlines()
        goodnight = open('text_dir/gnList').read().splitlines()
        dg = discord.Embed(title="uwu", description="",
                           colour=discord.Colour.magenta())
        dg.set_image(url="https://i.imgur.com/6hmvMu2.png")
        myfile = discord.File('images/video0(1).mp4')
        if message.author.bot:
            return  # ignore all bots
        content = message.content.casefold()
        if "pog" in content:
            await message.reply("Shut the fuck up with that cringe ass bullshit")
        if "trials" in content:
            await message.add_reaction("<:no:795350056151941120>")
        if "fuck you fembot" in content:
            await message.reply(f"fuck you {message.author.mention}")
        if "morning" in content:
            await message.reply(random.choice(morning))
        if "goodnight" in content:
            await message.channel.send(random.choice(goodnight))
        if "nerd" in content:
            await message.reply(file=myfile)
            await message.reply("nErD. Get fucked dumbass.")
        if "god is dead" in content:
            await message.reply(embed=dg)


def setup(bot):
    bot.add_cog(OnMessCog(bot))
