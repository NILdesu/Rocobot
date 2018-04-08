import discord
from discord.ext import commands

class Members:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='userinfo', aliases = ['uinfo'], brief='aka: uinfo')
    @commands.guild_only()
    async def user_info(self, ctx):
        username = ctx.message.author
        embed = discord.Embed(title='User Info', color=discord.Colour.gold())
        embed.add_field(name='Name', value=username)
        embed.add_field(name='Roles', value=len(username.roles) - 1)
        embed.add_field(name='ID', value=username.id)
        embed.set_thumbnail(url=username.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Members(bot))
