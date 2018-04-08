import discord
from discord.ext import commands

class Fun:
    def __init__(self, bot):
        self.bot = bot

    # shabadaba: yup
    @commands.command(name='shabadaba', description='Exactly what it sounds like')
    async def shabadaba(self, ctx):
        await ctx.send('(⋈•̀ᴗ•́⋈)')


def setup(bot):
    bot.add_cog(Fun(bot))
