import Menu
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

    #enemy check goes here
    current_room = Menu.explore_menu(current_room)
    if current_room == False: #check if user quit
        break