import asyncio
from datetime import datetime
import time

import discord
from discord.ext import commands


class EventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("FemBot online\n")
        print(f"Logged in as {self.bot.user} - {self.bot.user.id}\n")
        print("--------------")
        print(time.strftime(f"Time at start:\n"
                            "%H:%M:%S\n"
                            "%m/%d/%Y\n"))

        while True:
            await self.bot.change_presence(
                activity=discord.Activity(type=discord.ActivityType.watching, name="For ^ | ^help"))
            await asyncio.sleep(45)
            await self.bot.change_presence(status=discord.Status.online,
                                           activity=discord.Game('with The Fragment'))
            await asyncio.sleep(45)
            await self.bot.change_presence(status=discord.Status.online, activity=discord.Game('with code'))
            await asyncio.sleep(45)
            await self.bot.change_presence(
                activity=discord.Activity(type=discord.ActivityType.watching, name="for bugs..."))
            await asyncio.sleep(45)
            await self.bot.change_presence(
                activity=discord.Activity(type=discord.ActivityType.streaming, name="Destiny 2"))
            await asyncio.sleep(45)
            await self.bot.change_presence(
                activity=discord.Activity(type=discord.ActivityType.watching, name="twitch.tv/thefragmentd2"))
            await asyncio.sleep(45)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        print("\n--------------\n")
        print(time.strftime("Joined at:\n" + "%H:%M:%S\n"))
        welEmb = discord.Embed(title='A new Homie just arrived!',
                               description=f"Welcome to The Fragment, {member.mention} "
                                           "We're happy to add you to this insanity."
                               , timestamp=datetime.utcnow())
        welEmb.add_field(name="Your first step: ", value="Read our rules found at: <#694715714724167731>\n"
                                                         "Then get some roles from <#694715780583129108>\n"
                                                         "*Read through ALL the roles, and check pins*", inline=False)
        welEmb.add_field(name="If you need help", value="Our staff - the <@&694709812528677008> - are always willing"
                                                        " to assist you!", inline=False)

        welEmb.set_thumbnail(url='https://i.imgur.com/0MEtXDZ.png')
        welEmb.color = discord.Color.from_rgb(239, 124, 243)
        wel_cum = self.bot.get_channel(698670684154363904)
        await wel_cum.send(embed=welEmb)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        try:
            bitchChannel = self.bot.get_channel(828820781882015764)
            print("\n--------------\n")
            print(time.strftime(f"Member ({member.id}) left at:\n" + "%H:%M:%S\n"))
            bitch = discord.Embed(title="Bitch Report:", description='', timestamp=datetime.utcnow())
            bitch.add_field(name="+1 to Bitch List", value=f"Bitch: {member}\nBitch ID: {member.id}")
            await bitchChannel.send(embed=bitch)
        except:
            bitchChannel = self.bot.get_channel(828820781882015764)
            print("\n--------------\n")
            print(time.strftime(f"Member ({member.id}) left at:\n" + "%H:%M:%S\n"))
            bitch = discord.Embed(title="Bitch Report:", description='', timestamp=datetime.utcnow())
            bitch.add_field(name="+1 to Bitch List",
                            value=f"Bitch had a weird name, so here is an ID.\nBitch ID: {member.id}")
            bitch.color = discord.Color.magenta()
            await bitchChannel.send(embed=bitch)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        errorEm = discord.Embed(title="uwu Uh oh!",
                                description="OOPSIE WOOPSIE!! Uwu We make a fucky wucky!! A wittle fucko boingo! The "
                                            "code monkeys at our headquarters are working VEWY HAWD to fix this!",
                                colour=discord.Colour.magenta())
        errorEm.set_thumbnail(url="https://i.imgur.com/fYonsqN.jpg")
        errorEm.add_field(name="Error: ", value=error)
        errorEm.set_footer(text="uwu use tha hwelp cummand")
        if isinstance(error, discord.ext.commands.MemberNotFound):
            await ctx.send(embed=errorEm)
        elif isinstance(error, commands.BadArgument):
            await ctx.send(embed=errorEm)
        else:
            await ctx.send(embed=errorEm)


def setup(bot):
    bot.add_cog(EventsCog(bot))
