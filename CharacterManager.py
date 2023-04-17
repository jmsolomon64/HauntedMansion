import json #allows for parsing of JSON files
import random #pseudo random number generator
import in_out

def read_players():
    '''Loads players from player.json'''
    player_file = open('./assets/player.json')
    return json.load(player_file) #returns data converted to python data structures

def write_players(new_data):
    '''writes new player to player.json'''
    with open('./assets/player.json', 'w') as outFile: #opens file in 'write' mode
        json.dump(new_data, outFile, indent=4) #writes new player data to outfile
        #indent = 4 makes the file formatted all nice and neat

def create_new_player():
    '''Creates data for new character'''
    current_players = read_players()
    new_player = {} #create new dic
    new_player['id'] = current_players[-1]['id'] + 1 #generate new ID
    in_out.print_menu('What is your name?')
    new_player['name'] = input()
    new_player['health'] = random.randint(10, 20)
    new_player['speed'] = random.randint(3, 12)
    new_player['strength'] = random.randint(5, 10)
    new_player['inventory'] = []
    new_player['weapon'] = None #python's version of null
    new_player['upperBody'] = None
    new_player['lowerBody'] = None

    current_players.append(new_player)
    write_players(current_players)

def load_character():
    '''Returns a character from array of all players'''
    player_data = read_players()
    # dic of players with id as key and name as value
    players = {}
    for player in player_data:
        players[player['id']] = player['name']

    while(True):
        in_out.print_menu('Please select a character:')
        for player in players:
            print(player, players[player])

        player_id = in_out.input_int()
        if player_id in players:
            return player_data[player_id]
        else:
            in_out.invalid_choice_msg()