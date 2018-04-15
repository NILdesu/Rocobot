import discord
from discord.ext import commands

import util
from util import io

import json, random

ROCO_CARDS_LOCATION = 'data/roco-cards.json'

class Fun:
    """ Fun Commands

    Commands that have no real purpose other than fun
    """
    def __init__(self, bot):
        self.bot = bot
        self.rocos = util.io.read_json(ROCO_CARDS_LOCATION)
        random.seed()

    @commands.command(name='shabadaba', brief='\u200B')
    async def shabadaba(self, ctx):
        """ Prints out a fun roco face """
        await ctx.send('(⋈•̀ᴗ•́⋈)')

    @commands.command(name='spot', brief='\u200B')
    async def spot_a_roco(self, ctx):
        """ Display a random roco picture """
        if (self.rocos == None):
            embed = discord.Embed(title='No Roco Spotted :disappointed:')
            await ctx.send(embed=embed)

        roco = self.rocos[random.randint(0, len(self.rocos))]

        embed = discord.Embed(title='Roco Spotted!', color=discord.Colour.gold())
        embed.set_image(url=roco)
        await ctx.send(embed=embed)

    @commands.command(name='rawr', brief='\u200B', usage='<lengthoarms> <lengtholegs>')
    async def print_dinosaur(self, ctx, lengthoarms: int, lengtholegs: int):
        """ Display a dinosaur with varying proportions

        lengthoarms: The length of arms for the dinosaur
        lengtholegs: The length of legs for the dinosaur
        """
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
