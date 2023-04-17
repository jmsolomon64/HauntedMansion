import Menu
import in_out
import MapManager

print('Haunted Mansion')
input('Press enter to start.\n')


player = Menu.main_menu()

current_room = MapManager.rooms[0]
    
#exploration loop
while(player):
    #key is in double quotes since whole string uses single quotes
    room_name = current_room['roomName']
    print(f'you are in the {room_name}')

    #Enemy encounter check
    enemy = MapManager.check_for_enemies(current_room['id'])

    if enemy != False:
        battle_status = Menu.battle_menu(player, enemy)
        if battle_status == False:
            in_out.death_msg()
            break
    

    current_room = Menu.explore_menu(current_room, player)
    if current_room == False: #check if user quit
        break

