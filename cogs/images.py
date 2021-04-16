import discord
from discord.ext import commands

import aiohttp


class ImagesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="distorts an image, use with a URL to distort `^magik url`",
                      aliases=["magic", "magikify","distort"], pass_context=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def magik(self, ctx, image:str, intensity: int = 2):
        """Actual working magik command - used an api, but is what it is"""
        emoji = "<:9154_PogU:712671828291747864>"


        await ctx.message.delete()

        message = await ctx.send(f"{emoji} — **Processing the image please wait!**")
        await message.delete(delay=3)

        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=magik&image={image}&intensity={intensity}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.magenta(),
                    title="uwu cooooool"
                )
                embed.set_image(url=res["message"])
                await ctx.send(embed=embed)

    @commands.command(help="deepfries an image, use with a URL to distort `^deepfry url`",
                      aliases=["fry", "deep", "df"], pass_context=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def deepfry(self, ctx, image: str, intensity: int = 5):
        """Deepfry - works alongside magik. """
        emoji = "<:9154_PogU:712671828291747864>"
        await ctx.message.delete()
        message = await ctx.send(f"{emoji} — **Processing the image please wait!**")
        await message.delete(delay=3)
        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                    f"https://nekobot.xyz/api/imagegen?type=deepfry&image={image}&intensity={intensity}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.magenta(),
                    title="uwu :flushed:"
                )
                embed.set_image(url=res["message"])
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ImagesCog(bot))
