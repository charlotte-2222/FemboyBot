import os
import urllib
from asyncio import sleep
from datetime import datetime
import random

import discord
from PIL.Image import Image
from discord.ext import commands
from utilityFunction.timeConvert import convert


class ServerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["gift", "giveaway", "gcreate", "gcr", "giftcr"])
    @commands.has_guild_permissions(manage_roles=True)
    async def create_giveaway(self, ctx):
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
                message = await self.bot('self', timeout=25, check=check)
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

        channel = self.bot(channel_id)
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
        embed = discord.Embed(title="Come one, come all!!!",
                              description=f"You could win: {prize}",
                              colour=discord.Color.magenta())
        embed.add_field(name="Hosted By: ", value=ctx.author.mention)
        embed.set_footer(text=f"Giveway ends in {answers[1]} from now")
        newMsg = await channel.send(embed=embed)
        await newMsg.add_reaction("<:thicc:775003570733842453>")
        # Check if Giveaway Cancelled
        self.cancelled = False
        await sleep(time)
        if not self.cancelled:
            myMsg = await channel.fetch_message(newMsg.id)

            users = await myMsg.reactions[0].users().flatten()
            users.pop(users.index(self.bot))
            # Check if User list is not empty
            if len(users) <= 0:
                emptyEmbed = discord.Embed(title="wait.... what?",
                                           description=f"You coulda won: {prize}", colour=discord.Colour.magenta())
                emptyEmbed.add_field(name="Hosted By:", value=ctx.author.mention)
                emptyEmbed.set_footer(text="No one won the Giveaway....")
                await myMsg.edit(embed=emptyEmbed)
                return
            if len(users) > 0:
                winner = random.choice(users)
                winnerEmbed = discord.Embed(title="Woooo hooo!",
                                            colour=discord.Color.magenta(),
                                            timestamp=datetime.utcnow())
                winnerEmbed.add_field(name=f"Congratulations {winner}, "
                                           f"you're the proud owner of: {prize}", value=winner.mention)
                winnerEmbed.set_image(
                    url="https://i.imgur.com/ok4Xuw4.jpg")
                await myMsg.edit(embed=winnerEmbed)
                return

    @commands.command(aliases=["poll", "vote"])
    async def create_poll(self, ctx, *args):
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

    @commands.command()
    async def announce(self, ctx):
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
                message = await self.bot('self', timeout=60, check=check)
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
        channel = self.bot(channel_id)
        # Check if Time is valid
        message = answers[1]
        await ctx.send(f"Announcement will be in {channel.mention}")
        embed = discord.Embed(title=f"Your Femboy overlord has a self:",
                              description=f"{message}",
                              colour=discord.Color.magenta())
        await channel.send(embed=embed)

    @commands.command()
    async def weather(self, ctx, city: str = None):
        URL = f"http://wttr.in/{city}_2tnp_transparency=1000_lang=en.png"
        if not city:
            await ctx.send("Please enter a valid city / town")
        else:
            with urllib.request.urlopen(URL) as url:
                with open("temp.png", "wb") as f:
                    f.write(url.read())
            img = Image.open('temp.png')
            img2 = img.crop((0, 0, 850, 420)).save("img2.png")
            file = discord.File("img2.png", filename="weather.png")
            await ctx.trigger_typing()
            await ctx.send(file=file)
            os.remove('img2.png')
            os.remove("temp.png")

    @commands.command()
    async def moon(self, ctx):
        URL = "http://wttr.in/moon.png"
        with urllib.request.urlopen(URL) as url:
            with open("temp8.png", "wb") as f:
                f.write(url.read())

        img = Image.open('temp8.png')

        img2 = img.crop((0, 0, 504, 322)).save("img8.png")

        file = discord.File("img8.png", filename="moon.png")
        await ctx.trigger_typing()
        await ctx.send(file=file)
        os.remove('img8.png')
        os.remove("temp8.png")


def setup(bot):
    bot.add_cog(ServerCog(bot))
