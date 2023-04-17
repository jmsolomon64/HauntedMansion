import in_out
import random
import json
import InventoryManagement

enemy_path = './assets/enemies.json'
enemy_file = open(enemy_path)
enemy_data = json.load(enemy_file)
enemies = {}
for enemy in enemy_data:
    enemies[enemy['id']] = enemy

def load_enemy(enemy_id):
    '''Grabs enemy from id'''
    return enemies[enemy_id]


#Enemy is Id here so we pull a 'fresh' enemy into combat
def determine_order(player, enemy_id):
    '''Appends players to combatents array in proper order'''
    combatants = []
    if player['speed'] > enemies[enemy_id]['speed']:
        combatants.append(player)
        combatants.append(enemies[enemy_id])
    else:
        combatants.append(enemies[enemy_id])
        combatants.append(player)
    return combatants


def check_combatants_status(combatants):
    '''Removes any combatant with 0 or lower health'''
    players = []
    for i in range(len(combatants)):
        if combatants[i]['health'] <= 0:
            in_out.enemy_message(f'{combatants[i]["name"]} has died.')
        else:
            players.append(combatants[i])
    return players
            

def calc_attack_points(attacker):
    '''Takes attacker object and decides attack'''
    #winging it on the math
    damage = 0
    speed = attacker['speed']/4 
    strength = attacker['strength']/2
    if attacker['weapon'] != None: #checks for weapon
        damage = InventoryManagement.all_items[attacker['weapon']]['damage']

    return (speed + strength + damage)/2


def calc_defense_points(defender):
    '''Takes defender object and decides defense'''
    #ALSO winging it
    resistance = 0
    if defender['upperBody'] != None:
        upperArmor = InventoryManagement.all_items[defender['upperBody']]
        resistance += upperArmor['resistance']
    if defender['lowerBody'] != None:
        lowerArmor = InventoryManagement.all_items[defender['lowerBody']]
        resistance += lowerArmor['resistance']

    return resistance/2

    
def check_accuracy(attacker, defender):
    '''checks if attack hits'''
    attack_speed = attacker['speed']
    defend_speed = defender['speed']
    if defend_speed/2 > attack_speed:
        return False
    else:
        return True   


def reg_attack(defender, attacker): 
    '''Takes target and source to do damage'''
    if check_accuracy(attacker, defender):
        total = calc_attack_points(attacker) - calc_defense_points(defender)
        defender['health'] -= total
        in_out.hit_msg(f'{defender["name"]} took {total} points of damage.')


def runaway(runner, chaser):
    '''checks if enemy/player can get away'''
    run_speed = runner['speed']
    chase_speed = chaser['speed'] 
    if run_speed > chase_speed:
        in_out.run_msg(f'{runner["name"]} got away', True)
        return True
    else:
        in_out.run_msg(f'{chaser["name"]} caught {runner["name"]}', False) 
        reg_attack(runner, chaser)
        return False


def enemy_turn(enemy, player):
    '''Handles turn for enemy'''
    in_out.enemy_message(f'{enemy["name"]}\' turn')
    while(True): #while loop used to continue if inventory empty
        choice = random.randint(1, 3) #create choice
        if choice == 1: #use item if available
            if len(enemy['inventory']) > 0:
                for item_id in enemy['inventory']:
                    if InventoryManagement.all_items[item_id]["type"] == 'Consumable':
                        InventoryManagement.use_consumable(item_id, enemy)
                        break
        elif choice == 2: 
            reg_attack(player, enemy)
            break
        elif choice == 3:
            return runaway(enemy, player)
    
