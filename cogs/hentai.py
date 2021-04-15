from datetime import datetime
from random import random
from imgurpython import ImgurClient

from utilityFunction.config import *
import discord
import requests
from discord.ext import commands

import nekos
import sys

imgur = ImgurClient(imgurC, ImgurL)


class NekosCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Shaxx porn")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def shaxx(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            r = requests.get(f"https://api.imgur.com/3/album/OVCCqqa/images?client_id={imgurC}").json()
            em = discord.Embed(title="uwu shaxxy-waxxie's thicc cock")
            indexmax = len(r['data']) - 1
            size = random.randrange(0, indexmax, 1)
            em.set_image(url=str(r['data'][size]['link']))
            em.color = discord.Color.magenta()
        try:
            await ctx.send(embed=em)
            await ctx.message.delete()
            print(f"{ctx.author} is asking for shaxx porn")
        except:
            await ctx.send(str(r['data'][size]['link']))

    @shaxx.error
    async def shaxx_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Foot hentai")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def feet(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title='feet doe :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        feet = nekos.img("feet")

        embed.set_image(url=feet)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @feet.error
    async def feet_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    # YURI
    @commands.command(help="I don't actually know what a yuri is, but this is that")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def yuri(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title='yuri doe :flushed:',
                description='',
                colour=discord.Color.magenta()
            )
        yur1 = nekos.img("yuri")

        embed.set_image(url=yur1)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @yuri.error
    async def yuri_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    # traps
    @commands.command(help="Femboy porn")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def femboy(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            author = ctx.message.author
            embed = discord.Embed(
                title='mmmm uwu....',
                description='',
                colour=discord.Colour.magenta()
            )
        trap = nekos.img("trap")
        embed.set_image(url=trap)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @femboy.error
    async def femboy_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Futa porn",
                      aliases=["futa"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def futanari(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title='futanari doe :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        futanari = nekos.img("futanari")

        embed.set_image(url=futanari)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @futanari.error
    async def futanari_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Gif of (supposedly) someone alone, likely masturbation - idk")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def solo_gif(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=':flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        solog = nekos.img("solog")

        embed.set_image(url=solog)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @solo_gif.error
    async def solo_gif_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Elmers")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def cum(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title='cum :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        cum = nekos.img("cum")

        embed.set_image(url=cum)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @cum.error
    async def cum_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Cat girl porn - in motion")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def nsfw_neko_gif(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=' :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        nsfw_neko_gif = nekos.img("nsfw_neko_gif")
        embed.set_image(url=nsfw_neko_gif)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @nsfw_neko_gif.error
    async def nsfw_neko_gif(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Masturbation i think")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def solo(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=' :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        solo = nekos.img("solo")

        embed.set_image(url=solo)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @solo.error
    async def solo_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="what what? In the butt - of course.")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def anal(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=' :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        anal = nekos.img("anal")

        embed.set_image(url=anal)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @anal.error
    async def anal_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="just hentai")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def hentai(self, ctx):
        global embed
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=' :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        hentai = nekos.img("hentai")

        embed.set_image(url=hentai)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @hentai.error
    async def hentai_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="it's like feet, but more erotic")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def erofeet(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=' :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        erofeet = nekos.img("erofeet")

        embed.set_image(url=erofeet)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @erofeet.error
    async def erofeet_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="it's a cat or something")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def pussy(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=' :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        pussy = nekos.img("pussy")

        embed.set_image(url=pussy)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @pussy.error
    async def pussy_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="isn't this a bird?")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def tits(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=' :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        tits = nekos.img("tits")

        embed.set_image(url=tits)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @tits.error
    async def tits_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="wish i were someone's waifu",
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def waifu(self, ctx):
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.magenta()
        )
        waifu = nekos.img("waifu")

        embed.set_image(url=waifu)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @waifu.error
    async def waifu_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Self explanatory")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def boobs(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=' :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        boobs = nekos.img("boobs")

        embed.set_image(url=boobs)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @boobs.error
    async def boobs_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Pat someone's head",
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def pat(self, ctx, member: discord.Member, *, reason=""):
        embed = discord.Embed(
            title=f"{ctx.message.author} patted {member.name}",
            description='',
            colour=discord.Colour.magenta()
        )
        pat = nekos.img("pat")

        embed.set_image(url=pat)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @pat.error
    async def pat_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Kiss someone",
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def kiss(self, ctx, member: discord.Member, *, reason=""):
        embed = discord.Embed(
            title=f"{ctx.message.author} kissed {member.name} {reason}",
            description='',
            colour=discord.Colour.magenta()
        )
        kiss = nekos.img("kiss")

        embed.set_image(url=kiss)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @kiss.error
    async def kiss_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Erotically spank your homie",
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def spank(self, ctx, member: discord.Member, *, reason=""):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=f"{ctx.message.author} spanked {member.name} {reason}",
                description='',
                colour=discord.Colour.magenta()
            )
        spank = nekos.img("spank")

        embed.set_image(url=spank)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @spank.error
    async def spank_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Cuddle your homie",
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def cuddle(self, ctx, member: discord.Member, *, reason=""):
        embed = discord.Embed(
            title=f"{ctx.message.author} cuddled {member.name} {reason}",
            description='',
            colour=discord.Colour.magenta()
        )
        cuddle = nekos.img("cuddle")

        embed.set_image(url=cuddle)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @cuddle.error
    async def cuddle_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Hug your homie",
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def hug(self, ctx, member: discord.Member, *, reason=""):
        embed = discord.Embed(
            title=f"{ctx.message.author} hugged {member.name} {reason}",
            description='',
            colour=discord.Colour.magenta()
        )
        hug = nekos.img("hug")

        embed.set_image(url=hug)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Furries are gross")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def fox_girl(self, ctx):
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.magenta()
        )
        fox_girl = nekos.img("fox_girl")

        embed.set_image(url=fox_girl)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @fox_girl.error
    async def fox_girl_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Furries are gross")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def neko(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=' nekos:flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        neko = nekos.img("neko")

        embed.set_image(url=neko)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @neko.error
    async def neko_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Tickle your homie",
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def tickle(self, ctx, member: discord.Member, *, reason=""):
        embed = discord.Embed(
            title=f"{ctx.message.author} tickled {member.name} {reason}",
            description='',
            colour=discord.Colour.magenta()
        )
        tickle = nekos.img("tickle")

        embed.set_image(url=tickle)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @tickle.error
    async def tickle_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="it's not like i wanted to do any of this... really")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def baka(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title='b-baka! :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        baka = nekos.img("baka")

        embed.set_image(url=baka)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @baka.error
    async def baka_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="nsfw avatar creation")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def nsfw_avatar(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=' :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        nsfw_avatar = nekos.img("nsfw_avatar")

        embed.set_image(url=nsfw_avatar)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @nsfw_avatar.error
    async def nsfw_avatar_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="makes a wallpaper, I've seen non-NSFW")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def wallpaper(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title='wallpaper :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        wallpaper = nekos.img("wallpaper")

        embed.set_image(url=wallpaper)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @wallpaper.error
    async def wallpaper_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Get pegged 4 hed")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def femdom(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title='domination... :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        femdom = nekos.img("femdom")
        embed.set_image(url=femdom)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @femdom.error
    async def femdom_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
            await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(NekosCog(bot))
