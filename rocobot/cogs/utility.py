import discord
from discord.ext import commands

import util
from util import shows

class Utility:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='shows')
    async def shows(self, ctx, *args):
        await util.shows.handle_command(ctx, args)

def setup(bot):
    bot.add_cog(Utility(bot))
