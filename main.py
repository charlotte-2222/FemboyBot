import discord
from discord.ext import commands

from utilityFunction.config import token


def get_prefix(bot, message):
    prefixes = ['^']
    if not message.guild:
        return '?'
    return commands.when_mentioned_or(*prefixes)(bot, message)


initial_extensions = ['cogs.admin',
                      'cogs.fun',
                      'cogs.hentai',
                      'cogs.imageFun',
                      'cogs.missc',
                      'cogs.owner',
                      'cogs.reddit',
                      'cogs.redditNSFW',
                      'cogs.serverStuff',
                      'cogs.images',
                      'cogs.events',
                      'cogs.omevent'
                      ]

bot = commands.Bot(command_prefix=get_prefix,
                   description="The Fragment's local femboy, Fembot!", intents=discord.Intents.all())


class MyNewHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page)
            emby.color = discord.Color.magenta()
            emby.set_thumbnail(url='https://i.imgur.com/0MEtXDZ.png')
            await destination.send(embed=emby)


bot.help_command = MyNewHelp()

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run(token, bot=True, reconnect=True)
