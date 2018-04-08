import discord
from discord.ext import commands

import util
from util import io

import sys, traceback, os

BOT_PREFIX = '&'

TOKEN_LOCATION = 'data/api-token.txt'
TOKEN = ''

# Access the API token if it exists
if os.path.exists(TOKEN_LOCATION):
    TOKEN = util.io.read_text(TOKEN_LOCATION)
# Otherwise prompt for the API token and store it
else:
    TOKEN = input("Please enter the API token: ").strip()
    util.io.write_text(TOKEN_LOCATION, TOKEN)

# Set the command prefix here
bot = commands.Bot(command_prefix=BOT_PREFIX)
initial_extensions = ['cogs.fun',
                      'cogs.owner',
                      'cogs.members',
                      'cogs.lemons',
                      'cogs.utility']

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
    embed.add_field(name='Author', value='NIL & Wally')
    await ctx.send(embed=embed)

# run bot...
bot.run(TOKEN)
