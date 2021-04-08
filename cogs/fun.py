import asyncio
from urllib import parse
import aiohttp
import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
from imgurpython import ImgurClient
from config import *
from utilityFunction import lists
from utilityFunction.CommandFunc import *
from datetime import datetime

imgur = ImgurClient(imgurC, ImgurL)


class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Measure your friend's dick",
                      aliases=["dick", "penis"],
                      pass_context=True)
    async def dong(self, ctx, *, user: discord.Member):
        """Detects user's dong length"""
        state = random.getstate()
        random.seed(user.id)
        dong = "8{}D".format("=" * random.randint(0, 30))
        random.setstate(state)
        em = discord.Embed(title="{}'s Dong Size".format(user), description="Size: " + dong,
                           colour=discord.Colour.magenta())
        await ctx.send(embed=em)

    @dong.error
    async def dong_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed2 = discord.Embed(
                title="Error!",
                description="Make sure your argument is `^dong @user`",
                color=discord.Color.magenta())
            await ctx.send(embed=embed2)

    @commands.command(help="Roll a die",
                      aliases=["r", "d"],
                      pass_contex=True)
    async def roll(self, ctx, rolls: str):
        """rolls a die"""
        resultString, results, numDice = random.randint(rolls)
        e1 = discord.Embed(title=roll_str(rolls) + f" for %s" % ctx.message.author.name,
                           color=discord.Color.dark_teal())
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
                                                                          + resultString + "\n**Total:** " + str(
                    results))
            e2.set_thumbnail(url='https://i.imgur.com/fYonsqN.jpg')
            await ctx.send(embed=e2)

    @roll.error
    async def roll_error(self, ctx, error):
        """on error for die"""
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, your dice will be there in a second", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Lyrics of the cumzone, selected randomly",
                      aliases=["cs"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def cumscript(self, ctx):
        """transcript of cumzon"""
        cum = open('text_dir/cumscript.txt').read().splitlines()
        await ctx.send(random.choice(cum))
        await ctx.message.delete()

    @cumscript.error
    async def cumscript_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Really? Is this song that appealing to you?", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Search for an image from imgur",
                      pass_context=True,
                      aliases=["is", "isrc"]
                      )
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def img_src(self, ctx, *text: str):
        """Allows the user to search for an image from imgur"""
        rand = random.randint(0, 29)
        if text == ():
            await ctx.send('**Please enter a search term**')
        elif text[0] != ():
            items = imgur.gallery_search(" ".join(text[0:len(text)]), advanced=None, sort='rising', window='all',
                                         page=0)
            await ctx.send(items[rand].link)
            await ctx.message.delete()

    @img_src.error
    async def img_src_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="You literally can just go to imgur", color=discord.Color.magenta())
            await ctx.send(embed=em)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed2 = discord.Embed(
                title="Error!",
                description="Make sure your argument is `^img_src 'a cool search term'`",
                color=discord.Color.magenta())
            await ctx.send(embed=embed2)

    @commands.command(help="Find a random cat",
                      pass_context=True)
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def cat(self, ctx):
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
    async def cat_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Find a random dog"
        , pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def dog(self, ctx):
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
    async def dog_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Find a random bird",
                      aliases=["bird"],
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def birb(self, ctx):
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
    async def birb_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Find a random otter",
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def otter(self, ctx):
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

    @commands.command(help="Find a random platapuss",
                      aliases=["platapussy",
                               "platty",
                               "platt",
                               "plt"],
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def plat(self, ctx):
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
    async def plat_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Find some random buns",
                      aliases=["rabbit",
                               "bunny"],
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def bun(self, ctx):
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
    async def bun_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="generate a random insult",
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def insult(self, ctx):
        """random insult"""
        lines = open('text_dir/insults.txt').read().splitlines()
        await ctx.send(random.choice(lines))
        await ctx.message.delete()

    @insult.error
    async def insult_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Ask the 8Ball a question",
                      aliases=["8ball",
                               "8b",
                               "eb"],
                      pass_context=True)
    async def eightball(self, ctx, *, question: commands.clean_content):
        """ Consult 8ball to receive an answer """
        answer = random.choice(lists.ballresponse)
        await ctx.send(f"🎱 **Question:** {question}\n**Answer:** {answer}")

    @commands.command(help="choose between")
    async def choose(self, ctx, *choices: str):
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))

    @commands.command(help="Get a random dad joke",
                      aliases=["dad"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def daddy(self, ctx):
        author = ctx.author
        async with aiohttp.ClientSession() as session:
            async with session.get("https://dadjoke-api.herokuapp.com/api/v1/dadjoke") as r:
                data = await r.json()
                d = discord.Embed(title=f":milk: Hey, I found the milk", description=data['joke'],
                                  color=discord.Color.magenta()
                                  , timestamp=datetime.utcnow())
                await ctx.send(embed=d)

    @daddy.error
    async def daddy_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Dad jokes are temporary, just like your actual dad",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command(help="Go run it :)",
                      pass_context=True,
                      aliases=["?flop"])
    async def flop(self, ctx):
        embed = discord.Embed(title="Ping Navy? well... alright....",
                              description="commere bitch and take this ping like a good slut... <@181909185733066752>\n"
                                          "I knew you liked it.\n"
                                          "<:Dadsbelt:708018497489338479>")

        await asyncio.sleep(5)
        await ctx.send(embed=embed)

    @commands.command(help="Get a random history fact",
                      aliases=["hist", "rh", "randhist"],
                      pass_context=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def history(self, ctx):
        await ctx.message.delete()
        author = ctx.message.author
        message = await ctx.send(f"Fetching History for {ctx.author.mention}!")
        await message.delete(delay=6)
        async with aiohttp.ClientSession() as cs:
            async with cs.get('http://numbersapi.com/random/date?json') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.magenta(),
                    title="Random History! :books:",
                    description=f":point_down:**Fact**:point_down:\n\n {res['text']}\n"
                                f"\n:point_right: Year: {res['year']}"
                )
                await asyncio.sleep(1)
                await ctx.send(embed=embed)

    @history.error
    async def history_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="You're on cooldown!",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(FunCog(bot))
