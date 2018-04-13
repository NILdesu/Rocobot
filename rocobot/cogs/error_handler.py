import discord
from discord.ext import commands

import traceback, sys

class CommandErrorHandler:
    def __init__(self, bot):
        self.bot = bot


    async def on_command_error(self, ctx, error):
        """ Generic error handler for commands

        ctx: context
        error: exception
        """

        # Prevents this handler from handling commands that have local handlers
        if hasattr(ctx.command, 'on_error'):
            return

        # Ignored commands
        ignored = ()

        # Allows us to check for original exceptions raised and sent to CommandInvokeError.
        # If nothing is found. We keep the exception passed to on_command_error.
        error = getattr(error, 'original', error)

        # Ignore commands from ignored
        if isinstance(error, ignored):
            return

        # Handle cooldown errors
        elif isinstance(error, commands.CommandOnCooldown):
            time_str = self.pretty_time(error.retry_after)
            return await ctx.send(f'You may call this command again after {time_str}')

        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


    def pretty_time(self, time):
        """ Return a gramatically correct time string """
        hours = int(time / 3600)
        minutes = int((time - hours * 3600) / 60)
        seconds = int(time - minutes * 60 - hours * 3600)

        hour_str = 'hours'
        minute_str = 'minutes'
        second_str = 'seconds'
        if hours == 1:
            hour_str = 'hour'
        if minutes == 1:
            minute_str = 'minute'
        if seconds == 1:
            second_str = 'second'

        return f'{hours} {hour_str}, {minutes} {minute_str}, and {seconds} {second_str}'


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
