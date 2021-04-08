import sys
from datetime import datetime
import random

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
        print(f"{ctx.author} is asking for d34 porn")

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
        print(f"{ctx.author} is asking for r34 porn")

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
        print(f"{ctx.author} is asking for gw porn")

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
        print(f"{ctx.author} is asking for shefuckshim porn")

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
        print(f"{ctx.author} is asking for femboy porn")

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
        print(f"{ctx.author} is asking for cock porn")

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
        print(f"{ctx.author} is asking for redhead porn")

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
        print(f"{ctx.author} is asking for porninfifteenseconds porn")

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
        print(f"{ctx.author} is asking for cumslut porn")

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
        print(f"{ctx.author} is asking for bdsm porn")

    @bdsm.error
    async def bdsm_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="how about I don't ask?", color=discord.Color.magenta())
            await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(RedditNSFWCog(bot))
