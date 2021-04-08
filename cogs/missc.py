from datetime import datetime

import discord
from discord.ext import commands


class MisscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="View tags to remind members of important info",
                      aliases=["t"])
    async def tags(self, ctx):
        author = ctx.message.author
        t = discord.Embed(title='Tags for the dull.',
                          description="Don't feel like explaining? I did it for you.")
        t.add_field(name="`tReddit`", value="`^tReddit`: explains why you can't use your horny Subreddit commands.")
        t.add_field(name="`tClan`", value="`^tClan` clan invites for those who are unwilling to work")
        t.add_field(name="`tdev`", value="`tdev` tags profile")
        t.add_field(name="`t45`", value="we all know what this is")
        t.add_field(name='`tias`', value="try it and see.")

        t.set_thumbnail(url='https://i.imgur.com/fYonsqN.jpg')
        t.color = discord.Color.magenta()
        await ctx.author.send(embed=t)
        await ctx.message.delete()

    @commands.command(help="Report a fellow member for misconduct")
    async def report(self, ctx, user: discord.Member, *reason):
        channel = self.bot(694637172271087749)  # since it's a cog u need self.bot
        author = ctx.message.author
        rearray = ' '.join(reason[:])  # converts reason argument array to string
        if not rearray:  # what to do if there is no reason specified
            await channel.send(f"{author} has reported {user}, reason unspecified")
            await ctx.author.send(f"You reported {user} without a specified reason")
            await ctx.message.delete()  # I would get rid of the command input
        else:
            await channel.send(f"{author} has reported {user}.\nReason: {rearray}")
            await ctx.author.send(f"You reported {user}\nReason for report for: {rearray}")
            await ctx.message.delete()

    @commands.command(help='View online helpers in Discord Bots.', aliases=['helper'], hidden=False)
    async def helpers(self, ctx):
        """View online helpers in the Discord Bots server."""
        if ctx.guild.id != 694631281346084925:
            return
        online = []
        offline = []
        idle = []
        dnd = []
        helpers = [i for i in ctx.guild.members if not i.bot and
                   694709812528677008 in [r.id for r in i.roles]]
        for i in helpers:
            if i.status == discord.Status.online: online.append(
                f'**{i.name[0:1]}\u200b{i.name[1:len(i.name)]}**#{i.discriminator}\n')
            if i.status == discord.Status.offline: offline.append(
                f'**{i.name[0:1]}\u200b{i.name[1:len(i.name)]}**#{i.discriminator}\n')
            if i.status == discord.Status.idle: idle.append(
                f'**{i.name[0:1]}\u200b{i.name[1:len(i.name)]}**#{i.discriminator}\n')
            if i.status == discord.Status.dnd: dnd.append(
                f'**{i.name[0:1]}\u200b{i.name[1:len(i.name)]}**#{i.discriminator}\n')

        msg = f'''
    **Helpers in {ctx.guild}**:
    {['online']} **Online:** {' | '.join(online) if online != [] else 'None'}
    {['idle']} **Away:** {' | '.join(idle) if idle != [] else 'None'}
    {['dnd']} **DnD:** {' | '.join(dnd) if dnd != [] else 'None'}
    {['offline']} **Offline:** {' | '.join(offline) if offline != [] else 'None'}
    '''
        await ctx.send(msg)

    @commands.command(help="Reddit Tag")
    async def tReddit(self, ctx):
        author = ctx.message.author
        t = discord.Embed(title='Reddit API.',
                          description=f"{author.mention} didn't feel like explaining - again. So here.",
                          timestamp=datetime.utcnow())
        t.add_field(name="So why can't you post sexy redheads?", value="***Rate limits***\n"
                                                                       "Reddit places a limit on requests "
                                                                       "as to not fuck their servers.\n"
                                                                       "Feasibly, we shouldn't hit that limit - it's 60 requests a minute.")
        t.add_field(name="However:",
                    value="*Currently*, PRAW also limits Reddit requests.\nWhile there is an AsyncPraw, this bot"
                          "has bot been written in it yet, flop has encountered issues when doing so.")
        t.add_field(name="Reading material:",
                    value="https://www.reddit.com/r/redditdev/comments/5wjbkz/ratelimit/  <-Reddit admin talking about shit\n"
                          "https://asyncpraw.readthedocs.io/en/latest/package_info/references.html    <- Read the docs\n"
                          "https://praw.readthedocs.io/en/latest/index.html       <- ...docs?\n"
                          "")
        t.add_field(name="Summary",
                    value="It's likely that when we toss out an assload of requests, we suddenly go over the limit"
                          "...and I dunno what the cooldown is.")
        t.set_thumbnail(url='https://i.imgur.com/fYonsqN.jpg')
        t.set_footer(text="How about we just don't spam dicks 'n tits from reddit")
        t.color = discord.Color.magenta()
        await ctx.send(embed=t)
        await ctx.message.delete()

    @commands.command(help="Clan Tag")
    async def tClan(self, ctx):
        author = ctx.message.author
        t = discord.Embed(title='ugh....',
                          description=f"fine {author.mention}..... i guess you are my little homie-champ",
                          timestamp=datetime.utcnow(), url="https://www.bungie.net/en/ClanV2?groupid=4179219")
        t.set_thumbnail(url='https://i.imgur.com/fYonsqN.jpg')
        t.color = discord.Color.magenta()
        await ctx.send(embed=t)
        await ctx.message.delete()

    @commands.command(help="Dev Tag")
    async def tdev(self, ctx):
        t = discord.Embed(title="Who made me?", description="Developer(s):",
                          timestamp=datetime.utcnow())
        t.add_field(name="flop#8986",
                    value="GitHub: /im-zach\n\nflop is developing me in his freetime while doing loads of"
                          "other stuff. He's happy to make bots for any purpose.")
        t.add_field(name="Website", value="https://im-zach.github.io")

        t.set_thumbnail(url='https://i.imgur.com/fYonsqN.jpg')
        t.add_field(name="Special Thanks:", value="Google\n"
                                                  "StackOverflow\n"
                                                  "GitHub\n"
                                                  "Discord.py (Docs + Discord Server)")
        t.color = discord.Color.magenta()
        await ctx.send(embed=t)
        await ctx.message.delete()

    @commands.command(help="math Tag")
    @commands.is_owner()
    async def t45(self, ctx):
        await ctx.send(f"```"
                       "45 minutes (45') converts to 0.75 degrees (0.75°)\n"
                       "How?\n"
                       "Examples:\n"
                       "1' = 0.0166666667° / 1° = 60'\n"
                       "15' = 15 × 0.0166666667° = 0.25°\n"
                       "```"
                       f"***Now that <@!{181909185733066752}> wants to be a dumbass and be critical,***\n"
                       "*based on the above equation we calculate that:*"
                       "```"
                       "For 45':\n"
                       "45' = 0.750 000 000 01(°)\n"
                       "For 0.75°:\n"
                       "to convert to celsius:\n"
                       "If (standard conversion == 0 °F = -17.77778 °C)\n"
                       "T(°C) = (0.75°F - 32) × 5/9\n"
                       "Leaving you with:\n"
                       "0.75 °F = -17.361 °C\n"
                       "```")

    @commands.command(aliases=["ping", "p"],
                      help="Shows the bot latency from the discord websocket.")
    async def pping(self, ctx):
        e=discord.Embed(title="PP",
            description=f"Your pp lasted `{self.bot.latency * 1000:.2f}ms`")
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(MisscCog(bot))
