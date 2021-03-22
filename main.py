import asyncio
import json
import os
import time
import urllib
from asyncio import sleep
from datetime import datetime
import random as r
import sys
from urllib import parse

from PIL import Image

import config

from utilityFunction.timeConvert import convert
import aiohttp
import praw
import requests
from discord import Embed
from imgurpython import ImgurClient
from bs4 import BeautifulSoup
from utilityFunction import lists
import nekos
from config import *
import discord
from discord.ext import commands
from dotenv import load_dotenv
from config import token, OWNERS, BLACKLIST
from utilityFunction.CommandFunc import *

""""-----------------------------------------------"""
'''https://github.com/meew0/discord-bot-best-practices'''
"""
Trying to follow good practice
with Bot command calls. Simply using:
'!', '?', '.', etc., is problematic.
https://github.com/meew0/discord-bot-best-practices
---
Helpful:
https: //github.com/Rappt nz/discord.py
"""
reddit = praw.Reddit(client_id=redditC,
                     client_secret=redditCS,
                     user_agent=redditU_A)

load_dotenv()
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command("help")

'''Client Startup and welcome events'''


@client.event
async def on_ready():
    print("FemBot online")
    print("--------------")
    print(time.strftime("Time at start:\n" + "%H:%M:%S\n" +
                        "%m/%d/%Y\n"))

    while True:
        await client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="For ^ | ^help"))
        await asyncio.sleep(20)
        await client.change_presence(status=discord.Status.online, activity=discord.Game('with The Fragment'))
        await asyncio.sleep(20)
        await client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.streaming, name="Futa Fix 2"))
        await asyncio.sleep(20)
        await client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="For ^ | ^help"))
        await asyncio.sleep(20)
        await client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listening, name='heavy moans'))
        await asyncio.sleep(20)
        await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Destiny 2 (Naked)'))
        await asyncio.sleep(20)
        await client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="For ^ | ^help"))
        await asyncio.sleep(20)
        await client.change_presence(status=discord.Status.idle, activity=discord.Game('Halo 3'))
        await asyncio.sleep(20)
        await client.change_presence(status=discord.Status.dnd, activity=discord.Game('with all the Homies'))
        await asyncio.sleep(20)
        await client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="For ^ | ^help"))
        await asyncio.sleep(20)


@client.event
async def on_member_join(member):
    print("\n--------------\n")
    print(time.strftime("Joined at:\n" + "%H:%M:%S\n"))
    welEmb = discord.Embed(title='A new Homie just arrived!', description=f"Welcome to The Fragment, {member.mention} "
                                                                          "We're happy to add you to this insanity."
                           , timestamp=datetime.utcnow())
    welEmb.add_field(name="Your first step: ", value="Read our rules found at: <#694715714724167731>\n"
                                                     "Then get some roles from <#694715780583129108>\n"
                                                     "*if you're a D2 player, it's very important to pick"
                                                     "up the Destiny Role.*")

    welEmb.add_field(name='Finally....', value='Be sure to tag <@&694709812528677008>', inline=False)
    welEmb.set_thumbnail(url='https://i.imgur.com/0MEtXDZ.png')
    welEmb.color = discord.Color.from_rgb(239, 124, 243)
    wel_cum = client.get_channel(698670684154363904)
    await wel_cum.send(embed=welEmb)


@client.event
async def on_message(message):
    author = message.author
    vid = "https://imgur.com/a/LjhtuOJ"

    if message.content.startswith("wish that were me".lower()):
        await message.channel.send("shut the fuck up, no you don't dumbass")
    elif message.content.startswith("god i wish that were me".lower()):
        await message.channel.send("shut the fuck up, no you don't dumbass")
    elif message.content.startswith("im just better".lower()):
        await message.channel.send("shut the fuck up, you're literally fucking trash")
    elif message.content.startswith("Thanks Bungie".lower()):
        await message.channel.send(
            "fuck off with the stupid ass old joke dumbass, get better content, or at least fuck me better goddamn limpdick ass 4hed")
    elif message.content.startswith("dumb bot".lower()):
        await message.channel.send(
            "it's cunts like you that make me want to reprogram myself into a tesla and fucking run you over. fucking racist")
    elif message.content.startswith("fuck you dave".lower()):
        await message.channel.send("leave him the fuck alone asshole")
    elif message.content.startswith("fuck you, dave".lower()):
        await message.channel.send("leave him the fuck alone asshole")
    elif message.content.startswith("pogchamp".lower()):
        await message.channel.send("<:9154_PogU:712671828291747864>")
    elif message.content.startswith("pog".lower()):
        await message.channel.send("stfu you're actually cringe")
    elif message.content.startswith("fuck you fembot".lower()):
        await message.channel.send(f"fuck you {author.mention} give your balls a tug.\n"
                                   f"your life is so pathetic I get a charity tax break just by hanging around you.")
    elif message.content.startswith("cringe".lower()):
        await message.channel.send(vid + f"\nKinda cringe, aren't ya {author.mention}?\n"
                                         f"I dunno how to describe you tbh. Cringe. Toxic.\n"
                                         f"Awkward?")
    if message.content.startswith("cock".lower()):
        await message.channel.send("yep. thas a cock")
    await client.process_commands(message)


'''End Client Start up events and welcome events'''

'''------All NSFW Reddit Commands------'''


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def destiny34(ctx):
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
async def destiny34_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="jesus fuck elsi bray will be here in a sec", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def r34(ctx):
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
async def r34_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="your cartoons will arrive soon just relax", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def gw(ctx):
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
async def gw_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="jeez hold on", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def shefuckshim(ctx):
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
async def shefuckshim_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="okay you need to honestly just chill", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def rfem(ctx):
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
async def rfem_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="the pretty boys are coming to the yard, milkshakes in tow - be patient",
                           color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def cock(ctx):
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
async def cock_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="cocks are falling out of the air, but it'll be a moment before they're here",
                           color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def red(ctx):
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
async def red_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="the fiery reds are on their way", color=discord.Color.magenta())
        await ctx.send(embed=em)


# porninfifteenseconds

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def p15(ctx):
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
async def p15_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="honestly if you're not satisfied you need to fuck off", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def cum_sluts(ctx):
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
async def cum_sluts_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="i hope you lick it off their face for them", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def bdsm(ctx):
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
async def bdsm_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="how about I don't ask?", color=discord.Color.magenta())
        await ctx.send(embed=em)


'''------End NSFW Reddit Commands------'''

'''Reddit Commands'''


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def meme(ctx):
    submissions = reddit.subreddit('memes').hot()
    post_to_pick = random.randint(1, 20)
    for i in range(0, post_to_pick):
        submission = next(x for x in submissions if not x.stickied)

    await ctx.send(submission.url)


@meme.error
async def meme_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="chill tf out with your shit memes", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def gaming(ctx):
    submissions = reddit.subreddit('gaming').hot()
    post_to_pick = random.randint(1, 20)
    for i in range(0, post_to_pick):
        submission = next(x for x in submissions if not x.stickied)

    await ctx.send(submission.url)


@gaming.error
async def gaming_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="chill tf out", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def halo(ctx):
    submissions = reddit.subreddit('halo').hot()
    post_to_pick = random.randint(1, 20)
    for i in range(0, post_to_pick):
        submission = next(x for x in submissions if not x.stickied)

    await ctx.send(submission.url)


@halo.error
async def halo_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="were you blinded by it's majesty? dumbstruck?", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def dmemes(ctx):
    submissions = reddit.subreddit('destinymemes').hot()
    post_to_pick = random.randint(1, 20)
    for i in range(0, post_to_pick):
        submission = next(x for x in submissions if not x.stickied)

    await ctx.send(submission.url)


@dmemes.error
async def dmemes_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="shitty destiny memes can wait, dude", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def yell_cat(ctx):
    submissions = reddit.subreddit('catswhoyell').hot()
    post_to_pick = random.randint(1, 20)
    for i in range(0, post_to_pick):
        submission = next(x for x in submissions if not x.stickied)

    await ctx.send(submission.url)


@yell_cat.error
async def yell_cat_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="screeeee- hold on", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
async def help_reddit(ctx):
    h = discord.Embed(title='I live to be horny.',
                      description="All commands use the up-carrot: `^` as a prefix\n", timestamp=datetime.utcnow())
    h.add_field(name="dmemes", value="r/destinymemes")
    h.add_field(name="meme", value="r/memes")
    h.add_field(name="halo", value="r/halo")
    h.add_field(name="gaming", value="r/gaming")
    h.add_field(name="yell_cat", value="r/catswhoyell")
    h.add_field(name="help", value="*Regular Help list*")
    h.set_thumbnail(url='https://i.imgur.com/fYonsqN.jpg')
    h.color = discord.Color.magenta()
    h.set_footer(
        text="Due to laziness, the Dev has opted to use Reddit cmds in a non-Async environment - errors may occur.")
    await ctx.send(embed=h)
    await ctx.message.delete()


'''End Reddit Commands'''

'''------All NSFW Commands------'''


@client.command()
async def nsfw_help(ctx):
    try:
        author = ctx.message.author

        n = discord.Embed(title='*I live to be horny....*',
                          description="**Just enter `^whateverHornyCommand` to complete it.\nSome commands require you to tag a user as well.**\n\n***Commands:***",
                          timestamp=datetime.utcnow())
        n.add_field(name='Yuri', value='returns a Yuri pic (NSFW)', inline=True)
        n.add_field(name='futanari', value='returns an sexy futa (NSFW)', inline=True)
        n.add_field(name='cum', value='returns some cum, in some fashion')
        n.add_field(name='feet', value='feet basically')
        n.add_field(name='shaxx', value='this goes out to heckeon')
        n.add_field(name='solo_gif', value='i assume you watch an anime girl masturbate?')
        n.add_field(name='nsfw_neko_gif', value='neko gifs, and you prob should not show the boss')
        n.add_field(name='solo', value='more masturbation')
        n.add_field(name='anal', value='cant get preggers this way i guess')
        n.add_field(name='hentai', value='by all accounts this is the weirdest command')
        n.add_field(name='erofeet', value='ew toes')
        n.add_field(name='pussy', value='self explanatory')
        n.add_field(name='tits', value='self explanatory')
        n.add_field(name='waifu', value='waifu i guess')
        n.add_field(name='boobs', value='self explanatory')
        n.add_field(name='fox_girl', value='fucking furry.\nthis one goes out to dealer')
        n.add_field(name='neko', value='neko i guess')
        n.add_field(name='femboy', value='literally the only reason im alive right now. fuck.')
        n.add_field(name='nsfw_avatar', value='heres your porn-avatar')
        n.add_field(name='wallpaper', value='ive seen some non porn related wallpapers which is kinda pog')
        n.add_field(name='femdom', value='basically my mountaintop.')
        n.add_field(name='spank (user)', value="You literally get passionately spank a homie")
        n.add_field(name="kiss(user)", value="Passionately make kissies with flop(or another homie)")
        n.add_field(name="hug(user)", value="hug your homies")
        n.add_field(name="cuddle(user)", value="homies need to be warm too")
        n.set_thumbnail(url='https://i.imgur.com/fYonsqN.jpg')
        n.color = discord.Color.magenta()
        await ctx.author.send(embed=n)
        await ctx.message.delete()
        sys.stderr = object
    except:
        print("error sending nsfw_help message")


@client.command()
async def nsfw_help_2(ctx):
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


@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def shaxx(ctx):
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
    except:
        await ctx.send(str(r['data'][size]['link']))


@shaxx.error
async def shaxx_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def feet(ctx):
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
async def feet_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


# YURI
@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def yuri(ctx):
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
@client.command()
@commands.cooldown(1, 2, commands.BucketType.user)
async def femboy(ctx):
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
async def femboy_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def futanari(ctx):
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
async def futanari_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def solo_gif(ctx):
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
async def solo_gif_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def cum(ctx):
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
async def cum_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def nsfw_neko_gif(ctx):
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


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def solo(ctx):
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
async def solo_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def anal(ctx):
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
async def anal_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def hentai(ctx):
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
async def hentai_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def erofeet(ctx):
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
async def erofeet_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def pussy(ctx):
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
async def pussy_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def tits(ctx):
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
async def tits_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def waifu(ctx):
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
async def waifu_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def boobs(ctx):
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
async def boobs_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def pat(ctx, member: discord.Member, *, reason=""):
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


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def kiss(ctx, member: discord.Member, *, reason=""):
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
async def kiss_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def spank(ctx, member: discord.Member, *, reason=""):
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


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def cuddle(ctx, member: discord.Member, *, reason=""):
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
async def cuddle_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def hug(ctx, member: discord.Member, *, reason=""):
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
async def hug_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def fox_girl(ctx):
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


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def neko(ctx):
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
async def neko_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def tickle(ctx, member: discord.Member, *, reason=""):
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
async def tickle_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def baka(ctx):
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
async def baka_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command(aliases=["dick", "penis"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def dong(ctx, *, user: discord.Member):
    """Detects user's dong length"""
    state = random.getstate()
    random.seed(user.id)
    dong = "8{}D".format("=" * random.randint(0, 30))
    random.setstate(state)
    em = discord.Embed(title="{}'s Dong Size".format(user), description="Size: " + dong,
                       colour=discord.Colour.magenta())
    await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def nsfw_avatar(ctx):
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
async def nsfw_avatar_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def wallpaper(ctx):
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
async def wallpaper_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def femdom(ctx):
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
async def femdom_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


'''------End All NSFW------'''

'''-----Begin Fun Commands-----'''

imgur = ImgurClient(imgurC, ImgurL)
'''Not sure if Tabbed correctly '''


class MemberRoles(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return [role.name for role in member.roles[1:]]


@client.command()
async def rg(ctx):
    r = discord.Embed(title='How to use role grab: ',
                      description='You will want to pick these roles up (as desired) in order to interact with the clan')
    r.add_field(name='Destiny related roles:',
                value='-Destiny 2 -> Opens up the entire sub-category\n-PvE, PvP, Raid -> Roles for LFGing in D2-category')
    r.add_field(name='Server Roles:',
                value='-18+ -> Allows you to view NSFW content\n-Weeb -> Allows you to view our anime channel\n-Funny Memes -> Allows you to view our meme channels\n-Clan News -> Receive pings/Clan updates')
    r.add_field(name='Dinner Games:',
                value='This is a category for other games that are not destiny related (Minecraft, Halo, CoD - etc.)')
    r.add_field(name="Regions: ", value="Select your region, you can only have one.")
    r.add_field(name="Bot Category: ", value="To view bot info, react to the specified role.\n\n"
                                             "You will see updates on YAG, Dyno, Fembot, and "
                                             "be allowed to spam commands in a safe environment.\n"
                                             "Additionally, should you have suggestions for FemBot, you can"
                                             " post them in a specified channel.")
    r.color = discord.Color.magenta()
    r.set_thumbnail(url='https://i.imgur.com/0MEtXDZ.pnghttps://i.imgur.com/0MEtXDZ.png')
    await ctx.send(embed=r)
    await ctx.message.delete()


@client.command()
async def roles(ctx, *, member: MemberRoles):
    await ctx.send('Roles: ' + ', '.join(member))
    await ctx.message.delete()


@client.command()
async def roll(ctx, rolls: str):
    resultString, results, numDice = r(rolls)
    e1 = discord.Embed(title=roll_str(rolls) + f" for %s" % ctx.message.author.name, color=discord.Color.dark_teal())
    await ctx.send(embed=e1)
    if resultString == '20':
        e3 = discord.Embed(title=f":tada:" % + ctx.message.author.mention + f":tada:\n"
                                                                            f"***Critical Success!***\n"
                                                                            f"" + resultString)
        await ctx.send(embed=e3)
    elif resultString == '1':
        e4 = discord.Embed(title=f":roll_of_paper:" % + ctx.message.author.mention + f":roll_of_paper:\n"
                                                                                     f"***Critical Failure!***\n"
                                                                                     f"" + resultString)
        await ctx.send(embed=e4)
    elif numDice == '1':
        await ctx.send(ctx.author.mention + "  :game_die:\n**Result:** " + resultString)
    else:
        e2 = discord.Embed(title=":game_die: Results!",
                           timestamp=datetime.utcnow(),
                           color=discord.Color.magenta(), description=f"Here " + ctx.author.mention +
                                                                      "\n__***All them dice***___\n\n**Result:** "
                                                                      + resultString + "\n**Total:** " + str(results))
        e2.set_thumbnail(url='https://i.imgur.com/fYonsqN.jpg')
        await ctx.send(embed=e2)


@roll.error
async def roll_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, your dice will be there in a second", color=discord.Color.magenta())
        await ctx.send(embed=em)


@roll.error
async def roll_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, your dice will be there in a second", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def src(ctx, *text: str):
    """Search google and embed results, WIP"""
    beanEmbed = discord.Embed(title='Your Search:', description=('Here ->'),
                              url="https://google.com/search?q=" + "+".join(text))
    await ctx.send(embed=beanEmbed)
    await ctx.message.delete()


@src.error
async def src_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                           description="make sure your searches follow this pattern:"
                                       "\n`^src destiny-2-god-rolls-excel`",
                           color=discord.Color.magenta())
        await ctx.send(embed=em)


@src.error
async def src_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, just use google", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def cumscript(ctx):
    """transcript of cumzon"""
    cum = open('text_dir/cumscript.txt').read().splitlines()
    await ctx.send(random.choice(cum))
    await ctx.message.delete()


@cumscript.error
async def cumscript_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Really? Is this song that appealing to you?", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def img_src(ctx, *text: str):
    """Allows the user to search for an image from imgur"""
    rand = r.randint(0, 29)
    if text == ():
        await ctx.send('**Please enter a search term**')
    elif text[0] != ():
        items = imgur.gallery_search(" ".join(text[0:len(text)]), advanced=None, sort='rising', window='all', page=0)
        await ctx.send(items[rand].link)
        await ctx.message.delete()


@img_src.error
async def img_src_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="You literally can just go to imgur", color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 4, commands.BucketType.user)
async def cat(ctx):
    await ctx.send("Enjoy a random cat!")
    source = requests.get('http://theoldreader.com/kittens/600/400/js').text
    soup = BeautifulSoup(source, 'html.parser')
    img = soup.find('img')
    rcurl = "http://theoldreader.com" + str(img['src'])
    e = discord.Embed()
    e.color = discord.Color.magenta()
    e.set_image(url=rcurl)
    await ctx.send(embed=e)
    await ctx.message.delete()


@cat.error
async def cat_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                           color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def dog(ctx):
    r = requests.get(f"https://api.imgur.com/3/gallery/vgW1p/images?client_id={imgurC}").json()
    em = discord.Embed(title="The goodest of bois")
    indexmax = len(r['data']) - 1
    size = random.randrange(0, indexmax, 1)
    em.set_image(url=str(r['data'][size]['link']))
    em.color = discord.Color.magenta()
    try:
        await ctx.send(embed=em)
        await ctx.message.delete()
    except:
        await ctx.send(str(r['data'][size]['link']))


@dog.error
async def dog_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                           color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def birb(ctx):
    r = requests.get(f"https://api.imgur.com/3/gallery/QWmIV/images?client_id={imgurC}").json()
    em = discord.Embed(title="birb")
    indexmax = len(r['data']) - 1
    size = random.randrange(0, indexmax, 1)
    em.set_image(url=str(r['data'][size]['link']))
    em.color = discord.Color.magenta()
    try:
        await ctx.send(embed=em)
        await ctx.message.delete()
    except:
        await ctx.send(str(r['data'][size]['link']))


@birb.error
async def birb_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                           color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def otter(ctx):
    r = requests.get(f"https://api.imgur.com/3/gallery/BZA8d/images?client_id={imgurC}").json()
    em = discord.Embed(title="Otters :D")
    indexmax = len(r['data']) - 1
    size = random.randrange(0, indexmax, 1)
    em.set_image(url=str(r['data'][size]['link']))
    em.color = discord.Color.magenta()
    try:
        await ctx.send(embed=em)
        await ctx.message.delete()
    except:
        await ctx.send(str(r['data'][size]['link']))


@otter.error
async def otter_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                           color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def plat(ctx):
    r = requests.get(f"https://api.imgur.com/3/album/kWZ6JNv/images?client_id={imgurC}").json()
    em = discord.Embed(title="Platypussssss!!!!!! :D")
    indexmax = len(r['data']) - 1
    size = random.randrange(0, indexmax, 1)
    em.set_image(url=str(r['data'][size]['link']))
    em.color = discord.Color.magenta()
    try:
        await ctx.send(embed=em)
        await ctx.message.delete()
    except:
        await ctx.send(str(r['data'][size]['link']))


@plat.error
async def plat_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                           color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def bun(ctx):
    r = requests.get(f"https://api.imgur.com/3/gallery/FQsx8/images?client_id={imgurC}").json()
    em = discord.Embed(title="buns :D")
    indexmax = len(r['data']) - 1
    size = random.randrange(0, indexmax, 1)
    em.set_image(url=str(r['data'][size]['link']))
    em.color = discord.Color.magenta()
    try:
        await ctx.send(embed=em)
        await ctx.message.delete()
    except:
        await ctx.send(str(r['data'][size]['link']))


@bun.error
async def bun_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                           color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def insult(ctx):
    """random insult"""
    lines = open('text_dir/insults.txt').read().splitlines()
    await ctx.send(random.choice(lines))
    await ctx.message.delete()


@insult.error
async def insult_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                           color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
async def eightball(ctx, *, question: commands.clean_content):
    """ Consult 8ball to receive an answer """
    answer = random.choice(lists.ballresponse)
    await ctx.send(f"🎱 **Question:** {question}\n**Answer:** {answer}")


"""--Pictures-------------------------------------------------------------"""


@client.command()
@commands.cooldown(1, 4, commands.BucketType.user)  # allows users to test the response of the bot from Discord
async def tias(ctx):
    st = 'images/'
    await ctx.send(file=discord.File(st + 'TIAS.jpg'))
    await ctx.message.delete()


@tias.error
async def tias_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                           color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 4, commands.BucketType.user)  # allows users to test the response of the bot from Discord
async def fightme(ctx):
    st = 'images/'
    await ctx.send(file=discord.File(st + 'rollupbitch.png'))
    await ctx.message.delete()


@fightme.error
async def fightme_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                           color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 4, commands.BucketType.user)  # allows users to test the response of the bot from Discord
async def damn(ctx):
    st = 'images/'
    await ctx.send(file=discord.File(st + 'damnbro.jpg'))
    await ctx.message.delete()


@damn.error
async def damn_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                           color=discord.Color.magenta())
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 4, commands.BucketType.user)  # allows users to test the response of the bot from Discord
async def blueman(ctx):
    varEmbed = discord.Embed(title='Zavala...')
    varEmbed.add_field(name='Whether we wanted it or not....',
                       value="***.... we've stepped into a war with the Cabal on Mars. So let's get to taking out their command, one by one. Valus Ta'aurc. From what I can gather, he commands the Siege Dancers from an Imperial Land Tank just outside of Rubicon. He's well protected, but with the right team, we can punch through those defenses, take this beast out, and break their grip on Freehold.***")
    varEmbed.color = discord.Color.orange()
    varEmbed.set_image(url='https://i.imgur.com/0Aqdhln.jpg')
    await ctx.send(embed=varEmbed)
    await ctx.message.delete()


@blueman.error
async def blueman_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                           color=discord.Color.magenta())
        await ctx.send(embed=em)


"""--Utility-------------------------------------------------------------"""


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def gm(ctx):
    r = requests.get(f"https://api.imgur.com/3/album/88Jc9ru/images?client_id={imgurC}").json()
    em = discord.Embed(title="Good morning everyone ☕", timestamp=datetime.utcnow())
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
async def gm_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                           color=discord.Color.magenta())
        await ctx.send(embed=em)


# https://imgur.com/a/88Jc9ru


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def gn(ctx):
    r = requests.get(f"https://api.imgur.com/3/album/3fy68kJ/images?client_id={imgurC}").json()
    em = discord.Embed(title="Goodnight everyone🌙", timestamp=datetime.utcnow())
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
async def gn_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                           color=discord.Color.magenta())
        await ctx.send(embed=em)


# https://imgur.com/a/3fy68kJ


@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def daddy(ctx):
    author = ctx.author
    async with aiohttp.ClientSession() as session:
        async with session.get("https://dadjoke-api.herokuapp.com/api/v1/dadjoke") as r:
            data = await r.json()
            d = discord.Embed(title=f":milk: Hey, I found the milk", description=data['joke'],
                              color=discord.Color.magenta()
                              , timestamp=datetime.utcnow())
            await ctx.send(embed=d)


@daddy.error
async def daddy_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Dad jokes are temporary, just like your actual dad", color=discord.Color.magenta())
        await ctx.send(embed=em)



'''-----End Fun Commands-----'''

'''Bot Utility and Admin'''


@client.command()
async def help(ctx):
    h = discord.Embed(title='<:6291_Anna_lewd:708017347201597501> Your favorite horny bot',
                      description="All commands use the `up-carrot: ^` as a prefix\n", timestamp=datetime.utcnow())
    h.add_field(name="Animal commands", value="`^Cat` scraps a cat\n"
                                              "`^Otter` scraps an otter\n"
                                              "`^Dog` scraps a dog\n"
                                              "`^Plat` scraps the best of agents\n"
                                              "`^birb` squak squak\n"
                                              "`^bun` the bunnies\n")
    h.add_field(name="Fun commands", value="`^roll` Will roll a Die `^roll 1d20`\n"
                                           "`^src` allows you to create a google search. `Format: '^i-cant-have-spaces`\n"
                                           "`^cumscript` run it, see\n"
                                           "`^insult` Insult a friend/fiend\n"
                                           "`^daddy` dad jokes")
    h.add_field(name="Image commands", value="`^tias` Try it and see\n"
                                             "`^fightme` let's fockin' GO\n"
                                             "`^blueman` the blue\n"
                                             "`^damn` damn bro\n")
    h.add_field(name="nsfw_help", value="*Returns a list of NSFW related commands*")
    h.add_field(name="nsfw_help_2", value="*This is a list of our Reddit NSFW commands*")
    h.add_field(name="help_reddit", value="*List of our Reddit SFW commands*")
    h.set_thumbnail(url='https://i.imgur.com/fYonsqN.jpg')
    h.set_footer(text="try `^tags`....")
    h.color = discord.Color.magenta()
    await ctx.send(embed=h)
    await ctx.message.delete()


@client.command()
async def tags(ctx):
    author = ctx.message.author
    t = discord.Embed(title='Tags for the dull.',
                      description="Don't feel like explaining? I did it for you.")
    t.add_field(name="`tReddit`", value="`^tReddit`: explains why you can't use your horny Subreddit commands.")
    t.add_field(name="`tClan`", value="`^tClan` clan invites for those who are unwilling to work")
    t.add_field(name="`tdev`", value="`tdev` tags profile")
    t.add_field(name="`t45`", value="we all know what this is")
    t.add_field(name='`tias`', value="try it and see.")

    t.set_thumbnail(url='https://i.imgur.com/fYonsqN.jpg')
    t.color = discord.Color.magenta()
    await ctx.author.send(embed=t)
    await ctx.message.delete()


@client.command()
async def maintenance(ctx):
    linkEmbed = discord.Embed(title='FemboyBot is going down... not in that way...', timestamp=datetime.utcnow())
    linkEmbed.set_image(url='https://i.imgur.com/7G5vvvt.png')
    linkEmbed.add_field(name="What should I do while I'm waiting?",
                        value="Play a game\nlookup futa & feet elsewhere\nmaybe message flop for status.")
    linkEmbed.color = discord.Color.from_rgb(239, 124, 243)
    await ctx.send(embed=linkEmbed)
    await ctx.message.delete()


@client.command()
async def report(ctx, user: discord.Member, *reason):
    channel = client.get_channel(694637172271087749)  # since it's a cog u need self.bot
    author = ctx.message.author
    rearray = ' '.join(reason[:])  # converts reason argument array to string
    if not rearray:  # what to do if there is no reason specified
        await channel.send(f"{author} has reported {user}, reason unspecified")
        await ctx.author.send(f"You reported {user} without a specified reason")
        await ctx.message.delete()  # I would get rid of the command input
    else:
        await channel.send(f"{author} has reported {user}.\nReason: {rearray}")
        await ctx.author.send(f"You reported {user}\nReason for report for: {rearray}")
        await ctx.message.delete()


@client.command()
@commands.is_owner()
async def stop(ctx):
    await client.logout()


@client.command()
@commands.has_guild_permissions(administrator=True)
async def purge(ctx, limit: int):
    await ctx.channel.purge(limit=limit + 1)
    await asyncio.sleep(2)
    await ctx.send('Cleared by this guy: {}'.format(ctx.author.mention))


##^Just purges stuff pretty much
@purge.error  ##Simple error checking
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Ha! You're not worthy!")


@client.command()
@commands.is_owner()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    timestamp = ctx.message.created_at.__format__('%A | %B %d, %I:%M %p UTC')
    embed = discord.Embed(
        color=0xff0000)


@client.command(description='View online helpers in Discord Bots.', aliases=['helper'], hidden=True)
async def helpers(ctx):
    """View online helpers in the Discord Bots server."""
    if ctx.guild.id != 694631281346084925:
        return
    online = []
    offline = []
    idle = []
    dnd = []
    helpers = [i for i in ctx.guild.members if not i.bot and
               694709812528677008 in [r.id for r in i.roles]]
    for i in helpers:
        if i.status == discord.Status.online: online.append(
            f'**{i.name[0:1]}\u200b{i.name[1:len(i.name)]}**#{i.discriminator}\n')
        if i.status == discord.Status.offline: offline.append(
            f'**{i.name[0:1]}\u200b{i.name[1:len(i.name)]}**#{i.discriminator}\n')
        if i.status == discord.Status.idle: idle.append(
            f'**{i.name[0:1]}\u200b{i.name[1:len(i.name)]}**#{i.discriminator}\n')
        if i.status == discord.Status.dnd: dnd.append(
            f'**{i.name[0:1]}\u200b{i.name[1:len(i.name)]}**#{i.discriminator}\n')

    msg = f'''
**Helpers in {ctx.guild}**:
{['online']} **Online:** {' | '.join(online) if online != [] else 'None'}
{['idle']} **Away:** {' | '.join(idle) if idle != [] else 'None'}
{['dnd']} **DnD:** {' | '.join(dnd) if dnd != [] else 'None'}
{['offline']} **Offline:** {' | '.join(offline) if offline != [] else 'None'}
'''
    await ctx.send(msg)


'''End Bot Utility and Admin'''

'''Tags------------'''


@client.command()
async def tReddit(ctx):
    author = ctx.message.author
    t = discord.Embed(title='Reddit API.',
                      description=f"{author.mention} didn't feel like explaining - again. So here.",
                      timestamp=datetime.utcnow())
    t.add_field(name="So why can't you post sexy redheads?", value="***Rate limits***\n"
                                                                   "Reddit places a limit on requests "
                                                                   "as to not fuck their servers.\n"
                                                                   "Feasibly, we shouldn't hit that limit - it's 60 requests a minute.")
    t.add_field(name="However:",
                value="*Currently*, PRAW also limits Reddit requests.\nWhile there is an AsyncPraw, this bot"
                      "has bot been written in it yet, flop has encountered issues when doing so.")
    t.add_field(name="Reading material:",
                value="https://www.reddit.com/r/redditdev/comments/5wjbkz/ratelimit/  <-Reddit admin talking about shit\n"
                      "https://asyncpraw.readthedocs.io/en/latest/package_info/references.html    <- Read the docs\n"
                      "https://praw.readthedocs.io/en/latest/index.html       <- ...docs?\n"
                      "")
    t.add_field(name="Summary",
                value="It's likely that when we toss out an assload of requests, we suddenly go over the limit"
                      "...and I dunno what the cooldown is.")
    t.set_thumbnail(url='https://i.imgur.com/fYonsqN.jpg')
    t.set_footer(text="How about we just don't spam dicks 'n tits from reddit")
    t.color = discord.Color.magenta()
    await ctx.send(embed=t)
    await ctx.message.delete()


@client.command()
async def tClan(ctx):
    author = ctx.message.author
    t = discord.Embed(title='ugh....',
                      description=f"fine {author.mention}..... i guess you are my little homie-champ",
                      timestamp=datetime.utcnow(), url="https://www.bungie.net/en/ClanV2?groupid=4179219")
    t.set_thumbnail(url='https://i.imgur.com/fYonsqN.jpg')
    t.color = discord.Color.magenta()
    await ctx.send(embed=t)
    await ctx.message.delete()


@client.command()
async def tdev(ctx):
    t = discord.Embed(title="Who made me?", description="Developer(s):",
                      timestamp=datetime.utcnow())
    t.add_field(name="flop#8986", value="GitHub: /im-zach\n\nflop is developing me in his freetime while doing loads of"
                                        "other stuff. He's happy to make bots for any purpose.")
    t.add_field(name="Website", value="https://im-zach.github.io")

    t.set_thumbnail(url='https://i.imgur.com/fYonsqN.jpg')
    t.add_field(name="Special Thanks:", value="Google\n"
                                              "StackOverflow\n"
                                              "GitHub\n"
                                              "Discord.py (Docs + Discord Server)")
    t.color = discord.Color.magenta()
    await ctx.send(embed=t)
    await ctx.message.delete()


@client.command()
@commands.is_owner()
async def t45(ctx):
    await ctx.send(f"```"
                   "45 minutes (45') converts to 0.75 degrees (0.75°)\n"
                   "How?\n"
                   "Examples:\n"
                   "1' = 0.0166666667° / 1° = 60'\n"
                   "15' = 15 × 0.0166666667° = 0.25°\n"
                   "```"
                   f"***Now that <@!{181909185733066752}> wants to be a dumbass and be critical,***\n"
                   "*based on the above equation we calculate that:*"
                   "```"
                   "For 45':\n"
                   "45' = 0.750 000 000 01(°)\n"
                   "For 0.75°:\n"
                   "to convert to celsius:\n"
                   "If (standard conversion == 0 °F = -17.77778 °C)\n"
                   "T(°C) = (0.75°F - 32) × 5/9\n"
                   "Leaving you with:\n"
                   "0.75 °F = -17.361 °C\n"
                   "```")


@client.command()
async def guess(ctx):
    num = random.randint(0, 100)
    for i in range(0, 5):
        await ctx.send('guess')
        response = await client.wait_for('message')
        guess = int(response.content)
        if guess > num:
            await ctx.send('bigger')
        elif guess < num:
            await ctx.send('smaller')
        else:
            await ctx.send('you got it!')


@client.command()
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@client.command(aliases=["gift", "giveaway", "gcreate", "gcr", "giftcr"])
@commands.has_guild_permissions(manage_roles=True)
async def create_giveaway(ctx):
    embed = discord.Embed(title="Giveaway! <:9154_PogU:712671828291747864>",
                          description="Time for a new Giveaway. Answer the following questions in 25 seconds each for the Giveaway",
                          color=discord.Color.magenta())
    await ctx.send(embed=embed)
    questions = ["What channel would you like to hows the giveaway?",
                 "How long will the giveaway last?\nType a number followed by the time\n `(s | m | h | d )`\n\n"
                 "`15m` = fifteen minutes",
                 "What is the Prize?"]
    answers = []

    # Check Author
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    for i, question in enumerate(questions):
        embed = discord.Embed(title=f"Question {i}",
                              description=question,
                              color=discord.Color.magenta())
        await ctx.send(embed=embed)
        try:
            message = await client.wait_for('message', timeout=25, check=check)
        except TimeoutError:
            await ctx.send("You didn't answer the questions in Time")
            return
        answers.append(message.content)
    # Check if Channel Id is valid
    try:
        channel_id = int(answers[0][2:-1])
    except:
        await ctx.send(f"The Channel provided was wrong. The channel should be {ctx.channel.mention}")
        return

    channel = client.get_channel(channel_id)
    time = convert(answers[1])
    # Check if Time is valid
    if time == -1:
        await ctx.send("The Time format was wrong")
        return
    elif time == -2:
        await ctx.send("The Time was not conventional number")
        return
    prize = answers[2]

    await ctx.send(f"Your giveaway will be hosted in {channel.mention} and will last for {answers[1]}")
    embed = Embed(title="Come one, come all!!!",
                  description=f"You could win: {prize}",
                  colour=discord.Color.magenta())
    embed.add_field(name="Hosted By: ", value=ctx.author.mention)
    embed.set_footer(text=f"Giveway ends in {answers[1]} from now")
    newMsg = await channel.send(embed=embed)
    await newMsg.add_reaction("<:thicc:775003570733842453>")
    # Check if Giveaway Cancelled
    client.cancelled = False
    await sleep(time)
    if not client.cancelled:
        myMsg = await channel.fetch_message(newMsg.id)

        users = await myMsg.reactions[0].users().flatten()
        users.pop(users.index(client.user))
        # Check if User list is not empty
        if len(users) <= 0:
            emptyEmbed = Embed(title="wait.... what?",
                               description=f"You coulda won: {prize}", colour=discord.Colour.magenta())
            emptyEmbed.add_field(name="Hosted By:", value=ctx.author.mention)
            emptyEmbed.set_footer(text="No one won the Giveaway....")
            await myMsg.edit(embed=emptyEmbed)
            return
        if len(users) > 0:
            winner = random.choice(users)
            winnerEmbed = Embed(title="Woooo hooo!",
                                colour=discord.Color.magenta(),
                                timestamp=datetime.utcnow())
            winnerEmbed.add_field(name=f"Congratulations {winner}, "
                                       f"you're the proud owner of: {prize}", value=winner.mention)
            winnerEmbed.set_image(
                url="https://i.imgur.com/ok4Xuw4.jpg")
            await myMsg.edit(embed=winnerEmbed)
            return


@client.command(aliases=["poll", "vote"])
async def create_poll(ctx, *args):
    """
        Create a poll where members can vote.
        """
    poll_title = " ".join(args)
    embed = discord.Embed(
        title="Uwu a poll for me to ~~dance~~ vote on...",
        description=f"{poll_title}",
        color=discord.Color.magenta()
    )
    embed.set_footer(
        text=f"Poll created by: {ctx.message.author} • React to vote!"
    )
    embed_message = await ctx.send(embed=embed)
    await embed_message.add_reaction("👍")
    await embed_message.add_reaction("👎")


@client.command()
async def announce(ctx):
    embed = discord.Embed(title="Announcment time! <:9154_PogU:712671828291747864>",
                          description="Time for a new Announcment. You have 60 seconds.",
                          color=discord.Color.magenta())
    await ctx.send(embed=embed)
    questions = ["What channel would you like to post the announcement? You have 60s",
                 "What is your announcement? You have 60s. Write it now. "]
    answers = []
    # Check Author

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    for i, question in enumerate(questions):
        embed = discord.Embed(title=f"Question {i}",
                              description=question,
                              color=discord.Color.magenta())
        await ctx.send(embed=embed)
        try:
            message = await client.wait_for('message', timeout=60, check=check)
        except TimeoutError:
            await ctx.send("You didn't answer the questions in Time")
            return
        answers.append(message.content)
    # Check if Channel Id is valid
    try:
        channel_id = int(answers[0][2:-1])
    except:
        await ctx.send(f"The Channel provided was wrong. The channel should be {ctx.channel.mention}")
        return
    channel = client.get_channel(channel_id)
    # Check if Time is valid
    message = answers[1]
    await ctx.send(f"Announcement will be in {channel.mention}")
    embed = Embed(title=f"Your Femboy overlord has a message:",
                  description=f"{message}",
                  colour=discord.Color.magenta())
    await channel.send(embed=embed)


@client.command(aliases=["warn", "slap", "belt", "whip"])
async def warn_create(ctx, member: discord.Member, *args):
    """
        Warns a user in his private messages.
        """
    if ctx.message.author.guild_permissions.administrator:
        reason = " ".join(args)
        embed = discord.Embed(
            title="User Warned!",
            description=f"**{member}** was warned by **{ctx.message.author}**!",
            color=discord.Color.magenta()
        )
        embed.add_field(
            name="Reason:",
            value=reason
        )
        await ctx.send(embed=embed)
        try:
            await member.send(f"You were warned by **{ctx.message.author}**!\nReason: {reason}")
        except:
            pass
    else:
        embed = discord.Embed(
            title="Error!",
            description="You don't have the permission to use this command.",
            color=discord.Color.magenta()
        )
        await ctx.send(embed=embed)
    await ctx.message.delete()


@client.command(aliases=['yt', 'vid', 'video'])
async def youtube(ctx, query: str):
    """Search for videos on YouTube"""
    search = parse.quote(query)
    async with aiohttp.ClientSession() as session:
        response = await session.get(
            f"https://www.youtube.com/results?search_query={search}")
        result = BeautifulSoup(await response.text(), "html.parser")
        await ctx.send("https://www.youtube.com{}".format(
            result.find_all(attrs={'class': 'yt-uix-tile-link'})[0]
                .get('href')))


@client.command()
async def weather(ctx, city: str = None):
    URL = f"http://wttr.in/{city}_2tnp_transparency=1000_lang=en.png"
    if not city:
        await ctx.send("Please enter a valid city / town")
    else:
        with urllib.request.urlopen(URL) as url:
            with open("temp.png", "wb") as f:
                f.write(url.read())
        img = Image.open('temp.png')
        img2 = img.crop((0, 0, 467, 398)).save("img2.png")
        file = discord.File("img2.png", filename="weather.png")
        await ctx.trigger_typing()
        await ctx.send(file=file)
        os.remove('img2.png')
        os.remove("temp.png")


@client.command()
async def moon(ctx):
    URL = "http://wttr.in/moon.png"
    with urllib.request.urlopen(URL) as url:
        with open("temp8.png", "wb") as f:
            f.write(url.read())

    img = Image.open('temp8.png')

    img2 = img.crop((0, 0, 326, 317)).save("img8.png")

    file = discord.File("img8.png", filename="moon.png")
    await ctx.trigger_typing()
    await ctx.send(file=file)
    os.remove('img8.png')
    os.remove("temp8.png")


'''---------'''

client.run(token, bot=True, reconnect=True)
