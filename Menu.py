import InventoryManagement
import CharacterManager
import BattleManager
import MapManager
import in_out

def main_menu():
    '''Handles all choices for start of game'''
    while(True):
        in_out.print_menu('1. New Game \n2. Load Game \n3. Exit')
        choice = input()
        if choice == '1':
            CharacterManager.create_new_player()
        elif choice == '2':
            player = CharacterManager.load_character()
            return player
        elif choice == '3':
            return False
        else:
            in_out.invalid_choice_msg()


def inventory_menu(player):
    '''Controls Inventory'''
    while(True):
        InventoryManagement.view_player_inventory(player['inventory'])
        in_out.print_menu('Select an Item to view\nOr x to go back')
        item_id = in_out.int_or_quit()
        if item_id == False: #leaves menu
            break
        elif item_id in player['inventory']:
            if InventoryManagement.inspect_item(item_id, player) == False:
                return False #hits if consumable kills you
        else:
            in_out.invalid_choice_msg()
            
    

def explore_menu(room, player):
    '''Handles exploration, can engage inventory'''
    while(True):
        in_out.print_menu('What do you want to do? \n1) Continue to explore \n2) Check Inventory \n3) Quit')
        choice = input()
        if choice == '1':
            new_room = MapManager.select_direction(room)
            MapManager.change_discovery(new_room['id'], player)
            return new_room   
        elif choice == '2':
            if inventory_menu(player) == False:
                break
        elif choice == '3':
            return False
        else:
            in_out.invalid_choice_msg()
    #will execute if inventory_menu returns false 
    in_out.death_msg()
    return False


def battle_menu(player, enemy):
    '''Handles battle, can engage inventory'''
    in_out.enemy_message(f'Encountered {enemy["name"]}')
    combatants = BattleManager.determine_order(player, enemy['id'])
    print(f'{combatants[0]["name"]} goes first!')

    while(True):
        in_battle = True
        for i in range(len(combatants)): #Itterates through each player
            if in_battle: #Checks if a participant ran away
                if combatants[i] == enemy: #Handles enemy turn
                    if BattleManager.enemy_turn(enemy, player):
                        in_battle = False
                elif combatants[i] == player: #Hadnles player turn
                    while(True):
                            in_out.print_menu(f'1) Fight \n2) Inspect {enemy["name"]} \n3) Check Inventory \n4) Runaway')
                            choice = input()
                            if choice == '1':
                                BattleManager.reg_attack(enemy, player)
                                break
                            elif choice == '2':
                                print('look at that guy') # need an enemy 
                            elif choice == '3':
                                inventory_menu(player)
                            elif choice == '4':
                                if BattleManager.runaway(player, enemy):
                                    in_battle = False
                                    break
                            else: 
                                in_out.invalid_choice_msg()

        if in_battle: 
            combatants = BattleManager.check_combatants_status(combatants)
            if player not in combatants: #checks if player died
                return False
            elif len(combatants) == 1: #assumes only player left
                print(f'{player["name"]} has won!!')
                InventoryManagement.enemy_drop(enemy, player)
                return True
        else: #happens if someone ran away
            return True
            

