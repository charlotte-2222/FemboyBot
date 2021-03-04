from discord.ext import commands


class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['r', 'reload'])
    @commands.is_owner()
    async def restart(self, ctx, *, cog:str):
        """Restart Cog"""
        message = await ctx.send(f'Restarting `{cog}`...')
        self.bot.unload_extension(f'cogs.{cog}')
        self.bot.load_extension(f'cogs.{cog}')
        await message.edit(content=f'Restarted `{cog}`')

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, *, cog:str):
        """Load Cog"""
        self.bot.load_extension(f'cogs.{cog}')
        await ctx.send(f'Loaded `{cog}`')

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, *, cog:str):
        """Unload Cog"""
        self.bot.unload_extension(f'cogs.{cog}')
        await ctx.send(f'Unloaded `{cog}`')


def setup(bot):
    bot.add_cog(Dev(bot))