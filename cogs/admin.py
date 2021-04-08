import asyncio
from datetime import datetime

import discord
from discord.ext import commands


class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Admin only - Deletes messages")
    @commands.has_guild_permissions(administrator=True)
    async def purge(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit + 1)
        await asyncio.sleep(2)
        await ctx.send('Cleared by this guy: {}'.format(ctx.author.mention))

    ##^Just purges stuff pretty much
    @purge.error  ##Simple error checking
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Ha! You're not worthy!")

    @commands.command(help="Owner only - Kicks members at will", alias=["belt"], pass_context=True)
    @commands.is_owner()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        timestamp = ctx.message.created_at.__format__('%A | %B %d, %I:%M %p UTC')
        embed = discord.Embed(
            color=0xff0000)

    @commands.command(help="Create warnings against members",
                      aliases=["warn", "slap", "whip"], pass_context=True)
    async def warn_create(self, ctx, member: discord.Member, *args):
        if ctx.message.author.guild_permissions.administrator:
            reason = " ".join(args)
            embed = discord.Embed(title="User Warned!",
                                  description=f"**{member}** was warned by **{ctx.message.author}**!",
                                  color=discord.Color.magenta())
            embed.add_field(name="Reason:", value=reason)

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



def setup(bot):
    bot.add_cog(AdminCog(bot))
