import discord
from discord.ext import commands

import util
from util import io

import json, random

ROCO_CARDS_LOCATION = 'data/roco-cards.json'

class Fun:
    def __init__(self, bot):
        self.bot = bot

        self.rocos = util.io.read_json(ROCO_CARDS_LOCATION)

        random.seed()

    # shabadaba: yup
    @commands.command(name='shabadaba', description='Exactly what it sounds like')
    async def shabadaba(self, ctx):
        await ctx.send('(⋈•̀ᴗ•́⋈)')

    @commands.command(name='spot', description='spot a roco')
    async def spot_a_roco(self, ctx):
        if (self.rocos == None):
            embed = discord.Embed(title='No Roco Spotted :disappointed:')
            await ctx.send(embed=embed)

        roco = self.rocos[random.randint(0, len(self.rocos))]

        embed = discord.Embed(title='Roco Spotted!', color=discord.Colour.gold())
        embed.set_image(url=roco)
        await ctx.send(embed=embed)

    @commands.command(name='rawr')
    async def print_dinosaur(self, ctx, lengthoarms: int, lengtholegs: int):
        if lengthoarms > 90:
            lengthoarms = 90
        if lengtholegs > 50:
            lengtholegs = 50
        dinosaur_str = ''
        dinosaur_str += ('___________ \n')
        dinosaur_str += ("|          |\n")
        dinosaur_str += ('|        o |\n')
        dinosaur_str += ('|   _______|\n')
        dinosaur_str += ('|  |_______ \n')
        dinosaur_str += ('|__________|\n')
        dinosaur_str += ('|\n')
        for x in range(0, lengthoarms):
            dinosaur_str += ('=')
        dinosaur_str += ('|\n')

        for x in range(0, lengtholegs):
            dinosaur_str += ("|\n")

        dinosaur_str += ('=====')
        await ctx.send(f'```{dinosaur_str}```')

def setup(bot):
    bot.add_cog(Fun(bot))
