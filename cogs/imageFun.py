from datetime import datetime
import random

import discord
import requests
from discord.ext import commands
from imgurpython import ImgurClient

from config import *

imgur = ImgurClient(imgurC, ImgurL)


class ImageFunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Try it and see",
                      pass_context=True)
    @commands.cooldown(1, 4, commands.BucketType.user)  # allows users to test the response of the bot from Discord
    async def tias(self, ctx):
        st = 'images/'
        await ctx.send(file=discord.File(st + 'TIAS.jpg'))
        await ctx.message.delete()

    @tias.error
    async def tias_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Go ahead, fight me",
                      pass_context=True)
    @commands.cooldown(1, 4, commands.BucketType.user)  # allows users to test the response of the bot from Discord
    async def fightme(self, ctx):
        st = 'images/'
        await ctx.send(file=discord.File(st + 'rollupbitch.png'))
        await ctx.message.delete()

    @fightme.error
    async def fightme_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Damn bro",
                      pass_context=True)
    @commands.cooldown(1, 4, commands.BucketType.user)  # allows users to test the response of the bot from Discord
    async def damn(self, ctx):
        st = 'images/'
        await ctx.send(file=discord.File(st + 'damnbro.jpg'))
        await ctx.message.delete()

    @damn.error
    async def damn_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Indeed",
                      aliases=["z","vuvu","zaza"],
                      pass_context=True)
    @commands.cooldown(1, 4, commands.BucketType.user)  # allows users to test the response of the bot from Discord
    async def blueman(self, ctx):
        varEmbed = discord.Embed(title='Zavala...')
        varEmbed.add_field(name='Whether we wanted it or not....',
                           value="***.... we've stepped into a war with the Cabal on Mars. So let's get to taking out their command, one by one. Valus Ta'aurc. From what I can gather, he commands the Siege Dancers from an Imperial Land Tank just outside of Rubicon. He's well protected, but with the right team, we can punch through those defenses, take this beast out, and break their grip on Freehold.***")
        varEmbed.color = discord.Color.orange()
        varEmbed.set_image(url='https://i.imgur.com/0Aqdhln.jpg')
        await ctx.send(embed=varEmbed)
        await ctx.message.delete()

    @blueman.error
    async def blueman_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)

    """--Utility-------------------------------------------------------------"""

    @commands.command(help="Tell your homies goodmorning",
                      aliases=["goodmorning"],
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def gm(self, ctx):
        r = requests.get(f"https://api.imgur.com/3/album/88Jc9ru/images?client_id={imgurC}").json()
        author = ctx.author
        fU=str(author)
        x=fU.index("#")
        fU=fU[0:x]
        em = discord.Embed(title=str(fU)+" said: Good morning everyone ☕", timestamp=datetime.utcnow())
        em.set_footer(text="Remind flop to pick the thicc...")
        indexmax = len(r['data']) - 1
        size = random.randrange(0, indexmax, 1)
        em.set_image(url=str(r['data'][size]['link']))
        em.color = discord.Color.magenta()
        try:
            await ctx.send(embed=em)
            await ctx.message.delete()
        except:
            await ctx.send(str(r['data'][size]['link']))

    @gm.error
    async def gm_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)

    # https://imgur.com/a/88Jc9ru

    @commands.command(help="Tell your homies goodnight",
                      aliases=["goodnight"],
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def gn(self, ctx):
        author = ctx.author
        fU = str(author)
        x = fU.index("#")
        fU = fU[0:x]
        r = requests.get(f"https://api.imgur.com/3/album/3fy68kJ/images?client_id={imgurC}").json()
        em = discord.Embed(title=str(fU)+" said: Goodnight everyone🌙", timestamp=datetime.utcnow())
        em.set_footer(text="You guys are the best and I love you all!")
        indexmax = len(r['data']) - 1
        size = random.randrange(0, indexmax, 1)
        em.set_image(url=str(r['data'][size]['link']))
        em.color = discord.Color.magenta()
        try:
            await ctx.send(embed=em)
            await ctx.message.delete()
        except:
            await ctx.send(str(r['data'][size]['link']))

    @gn.error
    async def gn_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(ImageFunCog(bot))
