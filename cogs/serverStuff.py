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

    @commands.command()
    @commands.has_guild_permissions(manage_roles=True)
    async def memList(self, ctx):
        """Returns full list of server members + client ID's
        useful for a number of functions - will likely consult client needs,
        build more functions based on this"""
        with open('text_dir/thiccFrag.txt', 'w')as f:
            for member in ctx.guild.members:
                try:
                    print(f"{member}", "--", f'{member.id}', file=f)
                except:
                    print(f"Unable to write a name: {member.id}")
                    continue

            print("done")

    @commands.command()
    @commands.has_guild_permissions(manage_roles=True)
    async def thicc(self,ctx):
        """Allows server owner to pick the next thicc"""
        thicc = open('text_dir/thiccFrag.txt').read().splitlines()
        await ctx.send(random.choice(thicc))
        await ctx.message.delete()

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
                emptyEmbed.set_footer(
                    text="No one won the Giveaway...."

                )
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

    @commands.command()
    async def poll(self, ctx, channel: discord.TextChannel, *, question):
        sender = ctx.author
        embed = discord.Embed(
            color=discord.Color.magenta(),
            title="A Poll for me to Dance on... 📊"
        )
        embed.add_field(name="Question:", inline=False, value=question)
        embed.set_footer(text=f"— Poll from {sender}", icon_url=ctx.author.avatar_url)
        await ctx.message.delete()

        message = await channel.send(embed=embed)
        await message.add_reaction("👍")
        await message.add_reaction("👎")

    @poll.error
    async def poll_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.magenta(),
                title="Invalid Channel!",
                description="• Please put in a channel! Example: `^poll #channel 'question...'`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.magenta(),
                title="Invalid Argument!",
                description="• Please put in a valid option! Example: `^poll #channel 'question...'`"
            )
            await ctx.send(embed=embed)

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

    @commands.command(aliases=['server'])
    async def serverinfo(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(
            color=discord.Color.magenta(), timestamp=datetime.utcnow(),
            title=f":face_with_monocle:  Server Info For {guild.name}",
            description="\n— "
                        "\n➤ Shows all information about a guild."
                        "\n➤The information will be listed below!"
                        "\n —"
        )
        regions = {
            "us_west": ":flag_us: — USA West",
            "us_east": ":flag_us: — USA East",
            "us_central": ":flag_us: — USA Central",
            "us_south": ":flag_us: — USA South",
            "sydney": ":flag_au: — Sydney",
            "eu_west": ":flag_eu: — Europe West",
            "eu_east": ":flag_eu: — Europe East",
            "eu_central": ":flag_eu: — Europe Central",
            "singapore": ":flag_sg: — Singapore",
            "russia": ":flag_ru: — Russia",
            "southafrica": ":flag_za:  — South Africa",
            "japan": ":flag_jp: — Japan",
            "brazil": ":flag_br: — Brazil",
            "india": ":flag_in: — India",
            "hongkong": ":flag_hk: — Hong Kong",
        }
        verifications = {
            "none": "<:white__circle:625695417782239234> — No Verification",
            "low": "<:green_circle:625541294525251643> — Low Verification",
            "medium": "<:yellow_circle:625540435820937225> — Medium Verification",
            "high": "<:orange_circle:625542217100165135> — High Verification",
            "extreme": "<:red__circle:625833379258040330> — Extreme Verification"
        }
        embed.set_thumbnail(url=guild.icon_url_as(size=1024, format=None, static_format="png"))
        embed.add_field(name="• Guild name: ", value=str(guild.name))
        embed.add_field(name="• Guild ID: ", value=str(guild.id))
        embed.add_field(name="• Guild owner: ", value=guild.owner)
        embed.add_field(name="• Guild owner ID: ", value=guild.owner_id)
        embed.add_field(name="• Guild made in: ", value=guild.created_at.strftime("%A %d, %B %Y"))
        embed.add_field(name="• Channels count: ", value=len(guild.channels))
        embed.add_field(name="• Guild region: ", value=regions[guild.region.name])
        embed.add_field(name="• Guild verification: ", value=verifications[guild.verification_level.name])
        embed.add_field(name="• Member count: ", value=f"{guild.member_count}")
        embed.add_field(name="• Nitro boosters: ", value=guild.premium_subscription_count or "No Nitro Boosters!")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ServerCog(bot))
