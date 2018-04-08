import discord
from discord.ext import commands

class Fun:
    def __init__(self, bot):
        self.bot = bot

        self.rocos = []
        with open('data/roco-cards.json', 'r') as file:
            read_data = file.read()
            self.rocos = json.loads(read_data)

        random.seed()

    # shabadaba: yup
    @commands.command(name='shabadaba', description='Exactly what it sounds like')
    async def shabadaba(self, ctx):
        await ctx.send('(⋈•̀ᴗ•́⋈)')

    @commands.command(name='spot', description='spot a roco')
    async def spot_a_roco(self, ctx):
        roco = self.rocos[random.randint(0, len(self.rocos))]
        await ctx.send(f'Roco spotted:\n{roco}')


def setup(bot):
    bot.add_cog(Fun(bot))
