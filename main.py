import asyncio
import time
from datetime import datetime
import random
import random as r
import sys
import requests
from imgurpython import ImgurClient
from bs4 import BeautifulSoup
import nekos
from config import *
import discord
from discord.ext import commands
from dotenv import load_dotenv
from config import token

""""-----------------------------------------------"""
'''https://github.com/meew0/discord-bot-best-practices'''
"""
Trying to follow good practice
with Bot command calls. Simply using:
'!', '?', '.', etc., is problematic.
https://github.com/meew0/discord-bot-best-practices
---
Helpful:
https://github.com/Rapptz/discord.py
"""

load_dotenv()
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='^', intent=intents)
client.remove_command("help")

'''Client Startup and welcome events'''


@client.event
async def on_ready():
    channel = client.get_channel(694725683242467398)
    print("Ready to cum...uwu")
    print("--------------")
    print(time.strftime("Time at start:\n" + "%H:%M:%S\n" +
                        "%m/%d/%Y\n"))
    # st = 'images/'
    e = discord.Embed(title="Online!", timestamp=datetime.utcnow())
    e.set_image(url='https://i.imgur.com/eOI07Lj.jpg')
    e.color = discord.Color.magenta()
    await channel.send(embed=e)

    while True:
        await client.change_presence(status=discord.Status.online, activity=discord.Game('with The Fragment'))
        await asyncio.sleep(45)
        await client.change_presence(status=discord.Status.dnd, activity=discord.Game('with Jays mom'))
        await asyncio.sleep(45)
        await client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.streaming, name="Futa Fix 2"))
        await asyncio.sleep(45)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="For ^"))
        await asyncio.sleep(45)
        await client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listening, name='heavy moans'))
        await asyncio.sleep(45)
        await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Destiny 2 (Naked)'))
        await asyncio.sleep(45)
        await client.change_presence(status=discord.Status.idle, activity=discord.Game('Halo 3'))
        await asyncio.sleep(45)
        await client.change_presence(status=discord.Status.dnd, activity=discord.Game('with all the Homies'))
        await asyncio.sleep(45)


@client.event
async def on_member_join(member):
    print("\n--------------\n")
    print(time.strftime("Joined at:\n" + "%H:%M:%S\n" +
                        "%m/%d/%Y\n"))
    print(f'{member} just joined at ')
    welEmb = discord.Embed(title=f'{member} just joined!',
                           description=f'Thanks for joining The Fragment, {member}!', timestamp=datetime.utcnow())
    welEmb.add_field(name='What we need you to do:', value='Make sure you read the <#694715714724167731>\n'
                                                           'Make sure you get some roles from <#694715780583129108>'
                                                           '\nIf you play Destiny be sure to pick up the Destiny Role.',
                     inline=True)
    welEmb.add_field(name='Finally....', value='Be sure to tag <@&694709812528677008>', inline=False)
    welEmb.set_thumbnail(url='https://i.imgur.com/0MEtXDZ.png')
    welEmb.color = discord.Color.from_rgb(239, 124, 243)
    wel_cum = client.get_channel(698670684154363904)
    await wel_cum.send(embed=welEmb)


'''End Client Start up events and welcome events'''

'''------All NSFW Commands------'''


@client.command()
async def nsfw_help(ctx):
    try:
        author = ctx.message.author
        n = discord.Embed(title='*I live to be horny....*',
                          description="**Just enter '^whateverHornyCommand' to complete it.\nSome commands require you to tag a user as well.**\n\n***Commands:***",
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


@tickle.error
async def tickle_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
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


@femdom.error
async def femdom_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title="Slow tf down, captain horny", color=discord.Color.magenta())
        await ctx.send(embed=em)


'''------End All NSFW------'''

'''-----Begin Fun Commands-----'''

imgur = ImgurClient(imgurC, ImgurL)


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
    r.color = discord.Color.magenta()
    r.set_thumbnail(url='https://i.imgur.com/0MEtXDZ.pnghttps://i.imgur.com/0MEtXDZ.png')
    await ctx.send(embed=r)


@client.command()
async def roles(ctx, *, member: MemberRoles):
    await ctx.send('Roles: ' + ', '.join(member))


@client.command()
async def d(ctx, die: int):
    results = []
    for role in range(1):
        x = random.randint(1, die)
        results.append(x)
        embedVar = discord.Embed(title="You rolled a D" + str(die), description="And you got " + str(results) + "!")
        embedVar.color = discord.Color.dark_gold()
        await ctx.send(embed=embedVar)


@client.command()
async def src(ctx, *text: str):
    """Search google and embed results, WIP"""
    beanEmbed = discord.Embed(title='Your Search:', description=('Here ->'),
                              url="https://google.com/search?q=" + "+".join(text))
    await ctx.send(embed=beanEmbed)


@client.command()
async def cumscript(ctx):
    """transcript of cumzon"""
    cum = open('text_dir/cumscript.txt').read().splitlines()
    await ctx.send(random.choice(cum))


@client.command()
async def img_src(ctx, *text: str):
    """Allows the user to search for an image from imgur"""
    rand = r.randint(0, 29)
    if text == ():
        await ctx.send('**Please enter a search term**')
    elif text[0] != ():
        items = imgur.gallery_search(" ".join(text[0:len(text)]), advanced=None, sort='rising', window='all', page=0)
        await ctx.send(items[rand].link)


@client.command()
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


@client.command()
async def dog(ctx):
    r = requests.get(f"https://api.imgur.com/3/gallery/vgW1p/images?client_id={imgurC}").json()
    em = discord.Embed(title="The goodest of bois")
    indexmax = len(r['data']) - 1
    size = random.randrange(0, indexmax, 1)
    em.set_image(url=str(r['data'][size]['link']))
    em.color = discord.Color.magenta()
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['data'][size]['link']))


@client.command()
async def birb(ctx):
    r = requests.get(f"https://api.imgur.com/3/gallery/QWmIV/images?client_id={imgurC}").json()
    em = discord.Embed(title="birb")
    indexmax = len(r['data']) - 1
    size = random.randrange(0, indexmax, 1)
    em.set_image(url=str(r['data'][size]['link']))
    em.color = discord.Color.magenta()
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['data'][size]['link']))


@client.command()
async def otter(ctx):
    r = requests.get(f"https://api.imgur.com/3/gallery/BZA8d/images?client_id={imgurC}").json()
    em = discord.Embed(title="Otters :D")
    indexmax = len(r['data']) - 1
    size = random.randrange(0, indexmax, 1)
    em.set_image(url=str(r['data'][size]['link']))
    em.color = discord.Color.magenta()
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['data'][size]['link']))


@client.command()
async def plat(ctx):
    r = requests.get(f"https://api.imgur.com/3/album/kWZ6JNv/images?client_id={imgurC}").json()
    em = discord.Embed(title="Platypussssss!!!!!! :D")
    indexmax = len(r['data']) - 1
    size = random.randrange(0, indexmax, 1)
    em.set_image(url=str(r['data'][size]['link']))
    em.color = discord.Color.magenta()
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['data'][size]['link']))


@client.command()
async def bun(ctx):
    r = requests.get(f"https://api.imgur.com/3/gallery/FQsx8/images?client_id={imgurC}").json()
    em = discord.Embed(title="buns :D")
    indexmax = len(r['data']) - 1
    size = random.randrange(0, indexmax, 1)
    em.set_image(url=str(r['data'][size]['link']))
    em.color = discord.Color.magenta()
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['data'][size]['link']))


@client.command()
async def insult(ctx):
    """random insult"""
    lines = open('text_dir/insults.txt').read().splitlines()
    await ctx.send(random.choice(lines))


"""--Pictures-------------------------------------------------------------"""


@client.command()  # allows users to test the response of the bot from Discord
async def tias(ctx):
    st = 'images/'
    await ctx.send(file=discord.File(st + 'TIAS.jpg'))


@client.command()  # allows users to test the response of the bot from Discord
async def fightme(ctx):
    st = 'images/'
    await ctx.send(file=discord.File(st + 'rollupbitch.png'))


@client.command()  # allows users to test the response of the bot from Discord
async def damn(ctx):
    st = 'images/'
    await ctx.send(file=discord.File(st + 'damnbro.jpg'))


@client.command()  # allows users to test the response of the bot from Discord
async def blueman(ctx):
    varEmbed = discord.Embed(title='Zavala...')
    varEmbed.add_field(name='Whether we wanted it or not....',
                       value="***.... we've stepped into a war with the Cabal on Mars. So let's get to taking out their command, one by one. Valus Ta'aurc. From what I can gather, he commands the Siege Dancers from an Imperial Land Tank just outside of Rubicon. He's well protected, but with the right team, we can punch through those defenses, take this beast out, and break their grip on Freehold.***")
    varEmbed.color = discord.Color.orange()
    varEmbed.set_image(url='https://i.imgur.com/0Aqdhln.jpg')
    await ctx.send(embed=varEmbed)


"""--Utility-------------------------------------------------------------"""


@client.command()
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
    except:
        await ctx.send(str(r['data'][size]['link']))


# https://imgur.com/a/88Jc9ru


@client.command()
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
    except:
        await ctx.send(str(r['data'][size]['link']))


# https://imgur.com/a/3fy68kJ
'''-----End Fun Commands-----'''

'''Bot Utility and Admin'''

@client.command()
async def report(self, ctx, user : discord.Member, *reason):
    channel = self.bot.get_channel(694637172271087749) #since it's a cog u need self.bot
    author = ctx.message.author
    rearray = ' '.join(reason[:]) #converts reason argument array to string
    if not rearray: #what to do if there is no reason specified
        await channel.send(f"{author} has reported {user}, reason: Not provided")
        await ctx.message.delete() #I would get rid of the command input
    else:
        await channel.send(f"{author} has reported {user}, reason: {rearray}")
        await ctx.message.delete()

@client.command()
async def help(ctx):
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


@client.command()
async def maintenance(ctx):
    linkEmbed = discord.Embed(title='FemboyBot is going down... not in that way...', timestamp=datetime.utcnow())
    linkEmbed.set_image(url='https://i.imgur.com/7G5vvvt.png')
    linkEmbed.add_field(name="What should I do while I'm waiting?",
                        value="Play a game\nlookup futa & feet elsewhere\nmaybe message flop for status.")
    linkEmbed.color = discord.Color.from_rgb(239, 124, 243)
    await ctx.send(embed=linkEmbed)





'''End Bot Utility and Admin'''

client.run(token, bot=True, reconnect=True)
