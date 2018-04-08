import discord
from discord.ext import commands

class Utility:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='remind', brief='remind [who/where] [what] [when]')
    async def user_info(self, ctx, who, what, when):
        message_parts = []
        message_parts.append(f'who: {who}')
        message_parts.append(f'what: {what}')
        message_parts.append(f'when: {when}')
        await ctx.send('\n'.join(message_parts))


def setup(bot):
    bot.add_cog(Utility(bot))
