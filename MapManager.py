import json
import in_out
import random
import BattleManager
import InventoryManagement

#You reminded me global variables exist in your screenshot Ryan
room_path = './assets/rooms.json'
room_file = open(room_path)
room_data = json.load(room_file)
rooms = {}
for room in room_data:
    rooms[room['id']] = room

def change_discovery(room_id, player):
    if rooms[room_id]['discovered'] == False:
        in_out.found_direction(f'You have discovered {rooms[room_id]["roomName"]}')
        InventoryManagement.find_item(rooms[room_id], player)
        rooms[room_id]['discovered'] = True


def select_direction(room):
    print('Where do you want to go?\nOr x to go back')
    for direction in room['directions']:
        if rooms[direction['roomId']]['discovered'] == False:
            in_out.unknown_direction(f"{direction['roomId']}) {direction['direction']}")
        else:
            in_out.known_direction(f"{direction['roomId']}) {rooms[direction['roomId']]['roomName']}")
    return rooms[in_out.int_or_quit()]


def check_for_enemies(room_id):
    '''Checks enemies array in a room'''
    enemies = rooms[room_id]['enemies']
    enemy_count = len(enemies)
    if enemy_count == 0:
        return False
    else: 
        will_encounter = random.randint(0, 1) #decides if you will encounter
        if will_encounter == 1: # 1 = encounter
            return BattleManager.load_enemy(enemies[random.randint(0, enemy_count - 1)])
        else:
            return False
