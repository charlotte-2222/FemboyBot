from datetime import datetime

import discord
from discord.ext import commands


class MisscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rg(self, ctx):
        """used to post info on roles, could be made better.
            This is honestly very stupid but it will do.
            Too bad.
            """
        r = discord.Embed(title='How to use role grab: ',
                          description='You will want to pick these roles up (as desired) in order to interact with the clan')
        r.add_field(name='Destiny related roles:',
                    value='-Destiny 2 -> Opens up the entire sub-category\n-PvE, PvP, Raid -> Roles for LFGing in D2-category')
        r.add_field(name='Server Roles:',
                    value='-18+ -> Allows you to view NSFW content\n-Weeb -> Allows you to view our anime channel\n-Funny Memes -> Allows you to view our meme channels\n-Clan News -> Receive pings/Clan updates')
        r.add_field(name='Dinner Games:',
                    value='This is a category for other games that are not destiny related (Minecraft, Halo, CoD - etc.)')
        r.add_field(name="Regions: ", value="Select your region, you can only have one.")
        r.add_field(name="Bot Category: ", value="To view bot info, react to the specified role.\n\n"
                                                 "You will see updates on YAG, Dyno, Fembot, and "
                                                 "be allowed to spam commands in a safe environment.\n"
                                                 "Additionally, should you have suggestions for FemBot, you can"
                                                 " post them in a specified channel.")
        r.color = discord.Color.magenta()
        r.set_thumbnail(url='https://i.imgur.com/0MEtXDZ.pnghttps://i.imgur.com/0MEtXDZ.png')
        await ctx.send(embed=r)
        await ctx.message.delete()

    @commands.command()
    async def help(self, ctx):
        h = discord.Embed(title='<:6291_Anna_lewd:708017347201597501> Your favorite horny bot',
                          description="All commands use the `up-carrot: ^` as a prefix\n", timestamp=datetime.utcnow())
        h.add_field(name="Animal commands", value="`^Cat` scraps a cat\n"
                                                  "`^Otter` scraps an otter\n"
                                                  "`^Dog` scraps a dog\n"
                                                  "`^Plat` scraps the best of agents\n"
                                                  "`^birb` squak squak\n"
                                                  "`^bun` the bunnies\n")
        h.add_field(name="Fun commands", value="`^roll` Will roll a Die `^roll 1d20`\n"
                                               "`^src` allows you to create a google search. `Format: '^i-cant-have-spaces`\n"
                                               "`^cumscript` run it, see\n"
                                               "`^insult` Insult a friend/fiend\n"
                                               "`^daddy` dad jokes")
        h.add_field(name="Image commands", value="`^tias` Try it and see\n"
                                                 "`^fightme` let's fockin' GO\n"
                                                 "`^blueman` the blue\n"
                                                 "`^damn` damn bro\n")
        h.add_field(name="nsfw_help", value="*Returns a list of NSFW related commands*")
        h.add_field(name="nsfw_help_2", value="*This is a list of our Reddit NSFW commands*")
        h.add_field(name="help_reddit", value="*List of our Reddit SFW commands*")
        h.set_thumbnail(url='https://i.imgur.com/fYonsqN.jpg')
        h.set_footer(text="try `^tags`....")
        h.color = discord.Color.magenta()
        await ctx.send(embed=h)
        await ctx.message.delete()

    @commands.command()
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

    @commands.command()
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

    @commands.command(description='View online helpers in Discord Bots.', aliases=['helper'], hidden=True)
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

    @commands.command()
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

    @commands.command()
    async def tClan(self, ctx):
        author = ctx.message.author
        t = discord.Embed(title='ugh....',
                          description=f"fine {author.mention}..... i guess you are my little homie-champ",
                          timestamp=datetime.utcnow(), url="https://www.bungie.net/en/ClanV2?groupid=4179219")
        t.set_thumbnail(url='https://i.imgur.com/fYonsqN.jpg')
        t.color = discord.Color.magenta()
        await ctx.send(embed=t)
        await ctx.message.delete()

    @commands.command()
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

    @commands.command()
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


def setup(bot):
    bot.add_cog(MisscCog(bot))
