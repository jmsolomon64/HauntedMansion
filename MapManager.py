import json
import Input

#You reminded me global variables exist in your screenshot Ryan
room_path = './assets/rooms.json'
room_file = open(room_path)
room_data = json.load(room_file)
rooms = {}
for room in room_data:
    rooms[room['id']] = room

def change_discovery(room_id):
    print(f'You have discovered {new_room["roomName"]}')
    rooms[room_id]['discovered'] == True


def select_direction(room):
    print('Where do you want to go?')
    for direction in room['directions']:
        if rooms[direction['roomId']]['discovered'] == False:
            print(direction['roomId'], direction['direction'])
            
        else:
            print(direction['roomId'], [direction['roomId']]['roomName'])

    return rooms[Input.input_int('Please enter valid id')]



