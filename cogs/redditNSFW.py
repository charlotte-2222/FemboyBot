import sys
from datetime import datetime
from random import random

import discord
from discord.ext import commands
import praw
from config import *

reddit = praw.Reddit(client_id=redditC,
                     client_secret=redditCS,
                     user_agent=redditU_A)


class RedditNSFWCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nsfw_help_2(self, ctx):
        try:
            author = ctx.message.author

            n = discord.Embed(title='*I live to be horny....*',
                              description="**Just enter `^whateverHornyCommand` to complete it.\n***Commands:***",
                              timestamp=datetime.utcnow())
            n.add_field(name="`^bdsm`", value="pulls a top/hot post from r/bdsm")
            n.add_field(name="`^cum_sluts`", value="pulls a top/hot post from r/cumsluts")
            n.add_field(name="`^p15`", value="pulls a top/hot post from r/porninfifteenseconds")
            n.add_field(name="`^destiny34`", value="pulls a top/hot post from r/rule34destiny")
            n.add_field(name="`^gw`", value="pulls a top/hot post from r/gonewild")
            n.add_field(name="`^rfem`", value="pulls a top/hot post from r/femboys")
            n.add_field(name="`^shefuckshim`", value="pulls a top/hot post from r/shefuckshim")
            n.add_field(name="`^cock`", value="this is literally just a massive cock")
            n.add_field(name="`^red`", value="pulls a top/hot post from r/redheads")
            n.add_field(name="*CAUTION:*", value="Overuse of any reddit request can lead to the requests being cutoff "
                                                 "entirely.")
            n.set_thumbnail(url='https://i.imgur.com/fYonsqN.jpg')
            n.set_footer(
                text="Due to laziness, the Dev has opted to use Reddit cmds in a non-Async environment - errors may occur.")
            n.color = discord.Color.magenta()
            await ctx.author.send(embed=n)
            await ctx.message.delete()
            sys.stderr = object
        except:
            print("error sending nsfw_help message")

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def destiny34(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('rule34destiny').new()
            post_to_pick = random.randint(1, 50)
            for i in range(0, post_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)
        await ctx.message.delete()

    @destiny34.error
    async def destiny34_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="jesus fuck elsi bray will be here in a sec", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def r34(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('rule34').new()
            post_to_pick = random.randint(1, 50)
            for i in range(0, post_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)
        await ctx.message.delete()

    @r34.error
    async def r34_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="your cartoons will arrive soon just relax", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def gw(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('gonewild').new()
            post_to_pick = random.randint(1, 50)
            for i in range(0, post_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)
        await ctx.message.delete()

    @gw.error
    async def gw_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="jeez hold on", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def shefuckshim(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('shefuckshim').new()
            post_to_pick = random.randint(1, 50)
            for i in range(0, post_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)
        await ctx.message.delete()

    @shefuckshim.error
    async def shefuckshim_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="okay you need to honestly just chill", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def rfem(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('FemBoys').new()
            post_to_pick = random.randint(1, 50)
            for i in range(0, post_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)
        await ctx.message.delete()

    @rfem.error
    async def rfem_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="the pretty boys are coming to the yard, milkshakes in tow - be patient",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def cock(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('massivecock').new()
            post_to_pick = random.randint(1, 50)
            for i in range(0, post_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)
        await ctx.message.delete()

    @cock.error
    async def cock_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="cocks are falling out of the air, but it'll be a moment before they're here",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def red(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('redheads').new()
            post_to_pick = random.randint(1, 50)
            for i in range(0, post_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)
        await ctx.message.delete()

    @red.error
    async def red_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="the fiery reds are on their way", color=discord.Color.magenta())
            await ctx.send(embed=em)

    # porninfifteenseconds

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def p15(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('porninfifteenseconds').new()
            post_to_pick = random.randint(1, 50)
            for i in range(0, post_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)
        await ctx.message.delete()

    @p15.error
    async def p15_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="honestly if you're not satisfied you need to fuck off",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def cum_sluts(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('cumsluts').new()
            post_to_pick = random.randint(1, 50)
            for i in range(0, post_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)
        await ctx.message.delete()

    @cum_sluts.error
    async def cum_sluts_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="i hope you lick it off their face for them", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def bdsm(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('bdsm').new()
            post_to_pick = random.randint(1, 50)
            for i in range(0, post_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)
        await ctx.message.delete()

    @bdsm.error
    async def bdsm_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="how about I don't ask?", color=discord.Color.magenta())
            await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(RedditNSFWCog(bot))
