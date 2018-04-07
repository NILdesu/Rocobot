import discord
from discord.ext import commands
import json

class Fun:
    def __init__(self, bot):
        self.bot = bot

        self.inventory = {};
        with open('inventory/inventory.json', 'r') as file:
            read_data = file.read()
            self.inventory = json.loads(read_data)


    # shabadaba: yup
    @commands.command(name='shabadaba', description='Exactly what it sounds like')
    async def shabadaba(self, ctx):
        await ctx.send('(⋈•̀ᴗ•́⋈)')

    @commands.command(name='lemons', description='lemonade')
    async def lemons(self, ctx):
        user = str(ctx.message.author.id)
        if user not in self.inventory.keys():
            self.inventory[user] = 0
            with open('inventory/inventory.json', 'w') as file:
                file.write(json.dumps(self.inventory))

        await ctx.send(f':lemon: You have {self.inventory[user]} lemons :lemon:')

    @commands.command(name='pick', description='get more lemons')
    async def get_lemon(self,ctx):
        user = str(ctx.message.author.id)
        if user not in self.inventory.keys():
            self.inventory[user] = 0

        self.inventory[user] += 1
        with open('inventory/inventory.json', 'w') as file:
            file.write(json.dumps(self.inventory))

        await ctx.send(f':lemon: You picked one lemon :lemon:')
        await ctx.send(f':lemon: You now have {self.inventory[user]} lemons :lemon:')

def setup(bot):
    bot.add_cog(Fun(bot))
