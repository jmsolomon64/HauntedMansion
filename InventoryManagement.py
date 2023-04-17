import json
import in_out
import random

item_path = './assets/items.json'
item_file = open(item_path)
item_data = json.load(item_file)

#convert array of dics to dic of dics (data table) with item id as key
all_items = {}
for item in item_data:
    all_items[item['id']] = item

def view_player_inventory(item_ids):
    '''Converts int array of item Ids into actual items'''
    print('Inventory:')
    for item_id in item_ids:
        item_name = all_items[item_id]['itemName']
        print(f'{item_id}) {item_name}')


def use_consumable(item_id, player):
    '''Heal or posion yourself'''
    in_out.consumable_message(f'{player["name"]} used {all_items[item_id]["itemName"]}')
    player['health'] += all_items[item_id]['health']
    if player['health'] <= 0:
        return False


def equip_armor(item_id, player):
    '''Equip/UnEquip armor'''
    if item_id == player['upperBody']:
        in_out.armor_message(f'{player["name"]} unequipped {all_items[item_id]["itemName"]}')
        player['upperBody'] = None

    elif item_id == player['lowerBody']:
        in_out.armor_message(f'{player["name"]} unequipped {all_items[item_id]["itemName"]}')
        player['lowerBody'] = None

    elif 'Upper' in all_items[item_id]['type']:
            in_out.armor_message(f'{player["name"]} equipped {all_items[item_id]["itemName"]}')
            player['upperBody'] = item_id

    elif 'Lower' in all_items[item_id]['type']:
        in_out.armor_message(f'{player["name"]} equipped {all_items[item_id]["itemName"]}')
        player['lowerBody'] = item_id


def equip_weapon(item_id, player):
    '''Equip/Unequip players weapon'''
    if item_id == player['weapons']:
        in_out.weapon_message(f'{player["name"]} unequipped {all_items[item_id]["itemName"]}')
        player['weapons'] = None
    else:
        in_out.weapon_message(f'{player["name"]} equipped {all_items[item_id]["itemName"]}')
        player['weapons'] = item_id


def inspect_item(item_id, player):
    '''View details of an item'''
    if item_id in all_items:
        while(True):
            print(all_items[item_id])
            in_out.print_menu('1) Interact\n2) Back')
            choice  = input()
            if choice =='1': 
                if all_items[item_id]['type'] =='Consumable':
                    if use_consumable(item_id, player) == False:
                        return False #If you died from consumable 
                elif 'Armor' in all_items[item_id]['type']:
                    equip_armor(item_id, player)
                elif 'Weapon' in all_items[item_id]['type']:
                    equip_weapon(item_id, player)
            elif choice == '2':
                break
            else:
                print('Please enter a valid id#')
    else:
        print("Please enter valid id#")

def enemy_drop(enemy, player):
    '''randomly drops item from enemy'''
    item_count = len(enemy['inventory'])
    if item_count > 1:
        drop_index = random.randint(0, item_count - 1)
        drop_item = enemy['inventory'][drop_index]
        player['inventory'].append(drop_item['id'])
        print(f'{player["name"]} picked up {drop_item["itemName"]} from {enemy["name"]}')

    elif item_count == 1:
        drop_item = enemy['inventory'][0]
        player['inventory'].append(drop_item)
        print(f'{player["name"]} picked up something from {enemy["name"]}')

def find_item(room, player):
    '''Handles Item discovery for room,
    will probably delete if I flesh out rooms and add puzzles'''   
    if len(room['items']) > 0:
        for item in room['items']:
            player['inventory'].append(item)
            print(f'{player["name"]} found {all_items[item]}')