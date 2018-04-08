import discord
from discord.ext import commands

import json, random, os

INVENTORY_LOCATION = 'inventory/inventory.json'
class Lemons:
    def __init__(self, bot):
        self.bot = bot

        self.inventory = {}
        if os.path.exists(INVENTORY_LOCATION):
            with open(INVENTORY_LOCATION, 'r') as file:
                read_data = file.read()
                self.inventory = json.loads(read_data)
        else:
            with open(INVENTORY_LOCATION, 'w') as file:
                file.write("")

        random.seed()

    ###########################################################################
    # BOT COMMANDS
    ###########################################################################
    # Displays the amount of lemons a user has
    @commands.command(name='lemons', description='lemonade')
    async def lemons(self, ctx):
        username = ctx.message.author
        userid = str(username.id)
        if userid not in self.inventory.keys():
            self.inventory[userid] = self.create_empty_inventory()
            with open(INVENTORY_LOCATION, 'w') as file:
                file.write(json.dumps(self.inventory))

        userinv = self.inventory[userid]

        num_lemons = self.get_lemons_text(userinv['lemons'])
        await ctx.send(f':lemon: {username.mention} You have {num_lemons} :lemon:')


    @commands.command(name='mine', description='get more lemons')
    async def mine(self, ctx):
        username = ctx.message.author
        userid = str(username.id)
        if userid not in self.inventory.keys():
            self.inventory[userid] = self.create_empty_inventory()

        userinv = self.inventory[userid]

        if userinv['picks'] == 0:
            await ctx.send(f'{username.mention} You don\'t have any pickaxes! Buy one first')

        else:
            # Use double roll rng to determine whether the pick breaks
            if((random.randint(0, 100) + random.randint(0, 100)) / 2 < userinv['break_chance']):
                await ctx.send(f'{username.mention} Your pickaxe broke!')
                userinv['picks'] -= 1
                userinv['break_chance'] = 0

            else:
                lemons_gained = random.randint(3, 10)
                userinv['lemons'] += lemons_gained
                userinv['break_chance'] = 60 if userinv['break_chance'] == 60 else userinv['break_chance'] + 10
                lemon_str = self.get_lemons_text(userinv['lemons'])
                await ctx.send(f':lemon: {username.mention} You mined {lemons_gained} lemons. You now have {lemon_str} :lemon:')


        with open(INVENTORY_LOCATION, 'w') as file:
            file.write(json.dumps(self.inventory))

    # Rudimentary market support.
    # Currently only supports buying picks
    @commands.command(name='buy')
    async def buy(self, ctx):
        username = ctx.message.author
        userid = str(username.id)
        if userid not in self.inventory.keys():
            self.inventory[userid] = self.create_empty_inventory()
        userinv = self.inventory[userid]

        if userinv['lemons'] < 20 and userinv['picks'] == 0:
            await ctx.send("You seem to be starting out. Here's a pickaxe for free")
            await ctx.send("You got a pickaxe, free of charge!")

        elif userinv['lemons'] < 20 and userinv['picks'] > 0:
            await ctx.send("You can't afford this!")

        else:
            userinv['lemons'] -= 20;
            await ctx.send("You bought one pickaxe for 20 lemons")

        userinv['picks'] += 1;
        with open(INVENTORY_LOCATION, 'w') as file:
            file.write(json.dumps(self.inventory))

    @commands.command(name='inventory', aliases=['inv'])
    async def display_inventory(self, ctx):
        username = ctx.message.author
        userid = str(username.id)
        if userid not in self.inventory.keys():
            self.inventory[userid] = self.create_empty_inventory()
        userinv = self.inventory[userid]

        embed = discord.Embed(title=f'{username}\'s Inventory', color=discord.Colour.gold())

        lemons = userinv['lemons']
        picks = userinv['picks']

        embed.add_field(name=f':lemon: Lemon x {lemons}', value='\u200B', inline=False)
        embed.add_field(name=f':pick: Pickaxe x {picks}', value='\u200B', inline=False)

        await ctx.send(embed=embed)


    # Rolls the slots to win lemons
    @commands.command(name='slots', description='roco themed slot machine')
    async def spin_slots(self, ctx):
        message_parts = []
        username = ctx.message.author
        userid = str(username.id)
        if userid not in self.inventory.keys():
            self.inventory[userid] = self.create_empty_inventory

        userinv = self.inventory[userid]
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
        userinv['lemons'] += num_lemons
        with open(INVENTORY_LOCATION, 'w') as file:
            file.write(json.dumps(self.inventory))

        # Add the inventory to the message
        inventory_lemons = self.get_lemons_text(userinv['lemons'])
        message_parts.append(f':lemon: You now have {inventory_lemons} :lemon:')

        # Embed the message and then send
        embed = discord.Embed(color=discord.Colour.gold())
        await ctx.send(username.mention)
        embed.add_field(name='Slots', value=pretty_slots, inline=False)
        embed.add_field(name='\u200B', value='\n'.join(message_parts), inline=False)
        await ctx.send(embed=embed)

    ###########################################################################
    # HELPER FUNCTIONS
    ###########################################################################
    # Returns a random thing that Roco likes
    def random_roco_thing(self):
        roco_things = [':lemon:', ':sheep:', ':paintbrush:', ':art:', ':headphones:', ':dress:']
        return roco_things[random.randint(0, len(roco_things) - 1)]

    # Returns a grammatically correct count of lemons
    def get_lemons_text(self, num_lemons):
        if (num_lemons == 1):
            return '1 lemon'
        return f'{num_lemons} lemons'

    # returns a new empty inventory to be passed to a json file
    def create_empty_inventory(self):
        inv = {}
        inv['lemons'] = 0;
        inv['picks'] = 0;
        inv['break_chance'] = 0;
        return inv

def setup(bot):
    bot.add_cog(Lemons(bot))
