import os

__all__ = ['io']

# returns a new empty inventory to be passed to a json file
def create_empty_inventory():
    inv = {}
    inv['lemons'] = 0
    inv['picks'] = 0
    inv['break_chance'] = 0
    return inv
