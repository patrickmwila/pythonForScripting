#!/usr/bin/python3
"""
You are creating a fantasy video game. The data structure to model the
player’s inventory will be a dictionary where the keys are string values
describing the item in the inventory and the value is an integer value detail-
ing how many of that item the player has. For example, the dictionary value
{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the
player has 1 rope, 6 torches, 42 gold coins, and so on.

Write a function named displayInventory() that would take any possible
“inventory” and display it like the following:

Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62

"""

gameInventory = {'rope': 1, 'torch': 6, 'gold coin':
                 42,'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    total_value = 0

    print('Inventory:')
    for key, value in inventory.items():
        print(f'{value} {key}')
        total_value = total_value + value

    print(f'Total number of items: {total_value}')


print('Before adding to inventory!')
displayInventory(gameInventory)
print()

"""
Imagine that a vanquished dragon’s loot is represented as a list of strings
like this:
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Write a function named addToInventory(inventory, addedItems), where the
inventory parameter is a dictionary representing the player’s inventory (like
in the previous project) and the addedItems parameter is a list like dragonLoot.
The addToInventory() function should return a dictionary that represents the
updated inventory.
"""

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def addToInventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 1)

    return inventory


print('After adding to inventory!')
updated_game_inventory = addToInventory(gameInventory, dragon_loot)

displayInventory(updated_game_inventory)
