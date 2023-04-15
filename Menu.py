import CharacterManager
import MapManager
import Input

def main_menu():
    '''Handles all choices for start of game'''
    while(True):
        choice = input('1. New Game \n2. Load Game \n3. Exit\n')
        if choice == '1':
            CharacterManager.create_new_player()
        elif choice == '2':
            player = CharacterManager.load_character()
            return player
        elif choice == '3':
            return False
        else:
            print('Please choose a valid choice!')

def inventory_menu():
    '''Controls Inventory'''
    print('Inventory:')
    #call to InventoryManager.py to get list
    #loop through all items
    item_id = Input.input_int('Please enter valid id#')
    #if item_id in InventoryManager.player_items:
    #   check item type
    #   make relevant calls to InventoryManager
    #   if x then leave
    

def explore_menu(room):
    '''Handles exploration, can engage inventory/trigger battle'''
    print('What do you want to do?')
    while(True):
        choice = input('1) Continue to explore \n2) Check Inventory \n3) Quit \n')
        if choice == '1':
            return MapManager.select_direction(room)
        elif choice == '2':
            print('inventory here!!') #need a menu for inventory
        elif choice == '3':
            return False
        else:
            print('Please choose a valid choice!')




