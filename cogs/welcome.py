import discord
from discord.ext import commands
from discord.ext.commands import bot


class welcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}, read the rules and grab some roles!'.format(member))

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member:
            await ctx.send('Hello {0.name}!'.format(member))
        else:
            await ctx.send('Wait a minute... I know {0.name}'.format(member))
        self._last_member = member


bot.add_cog(welcome(bot))
