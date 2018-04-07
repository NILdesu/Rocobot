import discord
from discord.ext import commands
import json
import random

class Fun:
    def __init__(self, bot):
        self.bot = bot

        self.inventory = {};
        with open('inventory/inventory.json', 'r') as file:
            read_data = file.read()
            self.inventory = json.loads(read_data)

        random.seed()

    # Returns a random thing that Roco likes
    def random_roco_thing(self):
        roco_things = [':lemon:', ':sheep:', ':paintbrush:', ':art:', ':headphones:', ':dress:']
        return roco_things[random.randint(0, len(roco_things) - 1)]

    # Returns a grammatically correct count of lemons
    def get_lemons_text(self, num_lemons):
        if (num_lemons == 1):
            return '1 lemon'
        return f'{num_lemons} lemons'

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

    @commands.command(name='slots', description='roco themed slot machine')
    async def spin_slots(self, ctx):
        message_parts = []
        user = str(ctx.message.author.id)
        if user not in self.inventory.keys():
            self.inventory[user] = 0

        # Build the slots
        slots = []
        for i in range(0, 3):
            row = []
            for j in range(0, 3):
                row.append(self.random_roco_thing())
            slots.append(row)

        # Make the slots pretty
        pretty_slots_rows = []
        for i in range(len(slots)):
            pretty_slots_rows.append(' '.join(slots[i]))
        pretty_slots = '\n'.join(pretty_slots_rows)

        num_lemons = 0

        # Check the diagonals
        if (slots[0][0] == slots[1][1]) and (slots[1][1] == slots[2][2]):
            num_lemons += 1
        if (slots[0][2] == slots[1][1]) and (slots[2][0] == slots[1][1]):
            num_lemons += 1

        # Check the rows
        for i in range(0, 3):
            if (slots[i].count(slots[i][0]) == 3):
                num_lemons += 1

        # Add the score to the message
        score_lemons = self.get_lemons_text(num_lemons)
        message_parts.append(f':lemon: You won {score_lemons} :lemon:')

        # Add lemons to the inventory
        self.inventory[user] += num_lemons
        with open('inventory/inventory.json', 'w') as file:
            file.write(json.dumps(self.inventory))

        # Add the inventory to the message
        inventory_lemons = self.get_lemons_text(self.inventory[user])
        message_parts.append(f':lemon: You now have {inventory_lemons} :lemon:')

        # Send the message
        await ctx.send(pretty_slots)
        await ctx.send('\n'.join(message_parts))


def setup(bot):
    bot.add_cog(Fun(bot))
