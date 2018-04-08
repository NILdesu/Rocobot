import discord
from discord.ext import commands

import sys, traceback

BOT_PREFIX = '&'
TOKEN = 'PUT TOKEN HERE'

# Set the command prefix here
bot = commands.Bot(command_prefix=BOT_PREFIX)
initial_extensions = ['cogs.fun',
                      'cogs.owner',
                      'cogs.members',
                      'cogs.lemons']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}', file=sys.stderr)
            traceback.print_exc()

# Log in event
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="with lemons"))
    print('Logged in as ' + bot.user.name)

# Start commands here

# info: displays info on the bot
@bot.command()
async def info(ctx):
    embed = discord.Embed(title='Rocobot', description='A bot that most certainly tastes like lemons', color=discord.Colour.gold())
    embed.add_field(name='Author', value='NIL')
    await ctx.send(embed=embed)

# run bot...
bot.run(TOKEN)
