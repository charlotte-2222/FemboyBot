import os
import urllib.request
from asyncio import sleep
import random
from datetime import datetime
from pytz import timezone

import discord
from PIL.Image import Image
from discord.ext import commands
from utilityFunction.timeConvert import convert


class ServerCog(commands.Cog, command_attrs=dict(hidden=True)):
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

            await ctx.send("Member list updated :thumbsup:")
            print("done")

    @commands.command()
    @commands.has_guild_permissions(manage_roles=True)
    async def thicc(self, ctx):
        """Allows server owner to pick the next thicc"""
        thicc = open('text_dir/thiccFrag.txt').read().splitlines()
        thiccy = random.choice(thicc)
        fU = str(thiccy)
        x = fU.index("#")
        fU = fU[0:x]
        await ctx.message.reply(f"The new daily thicc will be: @{fU}", mention_author=True)

    @commands.command(help="Create an awesome giveaway",
                      aliases=["gift", "giveaway", "gcreate", "gcr", "giftcr"],
                      pass_context=True)
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
    @commands.has_guild_permissions(manage_roles=True)
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

    @commands.command(help="Get the weather for a city `^weather [city]`",
                      aliases=["wt"], hidden=False)
    async def weather(self, ctx, city: str = None):
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

    @commands.command(help="View a picture of the current lunar phase", hidden=False)
    async def moon(self, ctx):
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

    @commands.command(help="Server information", aliases=['server'], hidden=False)
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

    @commands.command(help="Get the time now for places all over the world",
                      aliases=["tn", "time"], hidden=False)
    async def timeNow(self, ctx):  # formerly printCurrentTime
        fmt = "%Y-%m-%d %H:%M:%S %Z%z"
        # Current time in UTC
        now_utc = datetime.now(timezone('UTC'))
        await ctx.send(now_utc.strftime(fmt) + " (UTC) :united_nations:")

        # Convert to Europe/London time zone
        now_london = now_utc.astimezone(timezone('Europe/London'))
        await ctx.send(now_london.strftime(fmt) + " (London) :flag_gb:")

        # Convert to Europe/Berlin time zone
        now_berlin = now_utc.astimezone(timezone('Europe/Berlin'))
        await ctx.send(now_berlin.strftime(fmt) + " (Berlin) :flag_de:")

        # Convert to CET time zone
        now_cet = now_utc.astimezone(timezone('CET'))
        await ctx.send(now_cet.strftime(fmt) + " (CET) :flag_eu:")

        # Convert to AUS-S time zone
        now_aus = now_utc.astimezone(timezone('Australia/Sydney'))
        await ctx.send(now_aus.strftime(fmt) + " (Australia/Sydney):flag_au:")

        # Convert to AUS-N time zone
        now_aus = now_utc.astimezone(timezone('Australia/Darwin'))
        await ctx.send(now_aus.strftime(fmt) + " (Northern Territory/Darwin):flag_au::regional_indicator_n:")

        # Convert to Asia-Singapore
        now_asia_sing = now_utc.astimezone(timezone('Asia/Singapore'))
        await ctx.send(now_asia_sing.strftime(fmt) + " (Asia/Singapore):earth_asia:")

        # Convert to Asia-Tokyo
        now_asia_tok = now_utc.astimezone(timezone('Asia/Tokyo'))
        await ctx.send(now_asia_tok.strftime(fmt) + " (Asia/Tokyo):flag_jp:")

        # Convert to Asia-East-China
        now_asia_shang = now_utc.astimezone(timezone('Asia/Shanghai'))
        await ctx.send(now_asia_shang.strftime(fmt) + " (East China, several Locations) :flag_cn: ")

        # Convert to Israel time zone
        now_israel = now_utc.astimezone(timezone('Israel'))
        await ctx.send(now_israel.strftime(fmt) + " (Israel) :flag_il:")

        # Convert to Canada/Eastern time zone
        now_canada_east = now_utc.astimezone(timezone('Canada/Eastern'))
        await ctx.send(now_canada_east.strftime(fmt) + " (Canada/Eastern):flag_ca::regional_indicator_e: ")

        # Convert to US/Central time zone
        now_central = now_utc.astimezone(timezone('US/Central'))
        await ctx.send(now_central.strftime(fmt) + " (US/Central):flag_us::regional_indicator_c: ")

        # Convert to US/Pacific time zone
        now_pacific = now_utc.astimezone(timezone('US/Pacific'))
        await ctx.send(now_pacific.strftime(fmt) + " (US/Pacific):flag_us::regional_indicator_p: ")

    @commands.command(help="Start a poll with up to 10 choices", pass_context=True)
    async def poll(self, ctx, question: str, *options: str):
        if len(options) <= 1:
            await ctx.send('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await ctx.send('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['✅', '❌']
        else:
            reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
        embed = discord.Embed(title=''.join(question),
                              description=''.join(description),
                              colour=discord.Color.magenta())
        react_message = await ctx.send(embed=embed)
        for reaction in reactions[:len(options)]:
            await react_message.add_reaction(reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await react_message.edit(embed=embed)

    @poll.error
    async def poll_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.magenta(),
                title="Invalid Channel!",
                description='• Please put in a channel! Example: `^poll some question '
                            '"resonse1" "resonse2" "resonse3", so on up to 10`'
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.magenta(),
                title="Invalid Argument!",
                description='• Please put in a channel! Example: `^poll some question '
                            '"resonse1" "resonse2" "resonse3", so on up to 10`'
            )
            await ctx.send(embed=embed)

    @commands.command(help="Tallies up the poll results", pass_context=True)
    async def tally(self, ctx, id=None):
        poll_message = await ctx.channel.fetch_message(id)
        embed = poll_message.embeds[0]
        unformatted_options = [x.strip() for x in embed.description.split('\n')]
        print(f'unformatted{unformatted_options}')
        opt_dict = {x[:2]: x[3:] for x in unformatted_options} if unformatted_options[0][0] == '1' \
            else {x[:1]: x[2:] for x in unformatted_options}
        # check if we're using numbers for the poll, or x/checkmark, parse accordingly
        voters = [self.bot.user.id]  # add the bot's ID to the list of voters to exclude it's votes

        tally = {x: 0 for x in opt_dict.keys()}
        for reaction in poll_message.reactions:
            if reaction.emoji in opt_dict.keys():
                reactors = await reaction.users().flatten()
                for reactor in reactors:
                    if reactor.id not in voters:
                        tally[reaction.emoji] += 1
                        voters.append(reactor.id)
        output = f"Results of the poll for '{embed.title}':\n" + '\n'.join(
            ['{}: {}'.format(opt_dict[key], tally[key]) for key in tally.keys()])
        await ctx.send(output)


def setup(bot):
    bot.add_cog(ServerCog(bot))
