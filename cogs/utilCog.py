from datetime import datetime
import discord
from discord.ext import commands


class utilCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


@commands.command()
async def help(self, ctx):
    h = discord.Embed(title='I live to be horny.',
                      description="All commands use the up-carrot: **'^'** as a prefix\n", timestamp=datetime.utcnow())
    h.add_field(name="Animal commands", value="**- Cat** -> scraps a cat\n"
                                              "**- Otter** -> scraps an otter\n"
                                              "**- Dog** -> scraps a dog\n"
                                              "**- Plat** -> scraps the best of agents\n"
                                              "**- birb** -> squak squak\n"
                                              "**- bun** -> the bunnies\n")
    h.add_field(name="Fun commands", value="**- d** -> Will roll a Die **(^d20)**\n"
                                           "**- src** -> allows you to create a google search. Format: '^i-cant-have-spaces\n"
                                           "**- cumscript** -> run it, see\n"
                                           "**- insult** -> GET FUCKED\n")
    h.add_field(name="Image commands", value="**- tias** -> Try it and see\n"
                                             "**- fightme** -> let's fockin' GO\n"
                                             "**- blueman** -> the blue\n"
                                             "**- damn** -> damn bro\n")
    h.add_field(name="nsfw_help", value="*Returns a list of NSFW related commands*")
    h.set_thumbnail(url='https://i.imgur.com/fYonsqN.jpg')
    h.color = discord.Color.magenta()
    await ctx.send(embed=h)


@commands.command()
async def maintenance(self, ctx):
    linkEmbed = discord.Embed(title='FemboyBot is going down... not in that way...', timestamp=datetime.utcnow())
    linkEmbed.set_image(url='https://i.imgur.com/7G5vvvt.png')
    linkEmbed.add_field(name="What should I do while I'm waiting?",
                        value="Play a game\nlookup futa & feet elsewhere\nmaybe message flop for status.")
    linkEmbed.color = discord.Color.from_rgb(239, 124, 243)
    await ctx.send(embed=linkEmbed)


def setup(bot):
    bot.add_cog(utilCog(bot))
