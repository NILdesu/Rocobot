import discord
from discord.ext import commands

import util
from util import shows

class Utility:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='shows')
    async def shows(self, ctx, *args):
        """ A handy show tracker. Keeps track of shows and who is watching them.

        Subcommands:
        &shows add [show]
        - Adds [show] to the list of shows
        &shows remove [show]
        - Removes [show] from the list of shows
        &shows join [show]
        - Adds you (the current user) as a watcher of [show]
        &shows leave [show]
        - Removes you (the current user) from the list of watchers of [show]
        &shows invite [user] [show]
        - Adds [user] as a watcher of [show]
        &shows kick [user] [show]
        - Removes [user] from the list of watchers of [show]
        &shows list
        - Lists all current shows in the list
        &shows recommend
        - Recommends a show to watch based on who is currently online"""
        await util.shows.handle_command(ctx, args)

def setup(bot):
    bot.add_cog(Utility(bot))
