import discord
import os

__all__ = ['io', 'shows']

# returns a new empty inventory to be passed to a json file
def create_empty_inventory():
    inv = {}
    inv['lemons'] = 0
    inv['picks'] = 0
    inv['break_chance'] = 0
    return inv

def get_online_members(members):
    online_members = []
    for i in range(0, len(members)):
        member = members[i]
        if (member.status == discord.Status.online):
            online_members.append(member)
    return online_members
