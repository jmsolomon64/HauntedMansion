import colorama #for cool colors!!
import time
from colorama import Fore, Back, Style

colorama.init() #initializes colorama

def invalid_choice_msg():
     '''Error message'''
     error_string = '\n!-!-!- Please enter valid # -!-!-!\n'
     print(Fore.RED + error_string + Style.RESET_ALL)

def death_msg():
     '''Game over'''
     print(Fore.RED + '\nYou Died\n' + Style.RESET_ALL)
     time.sleep(2.5)

def hit_msg(msg):
    '''Handles damage message'''
    print(Fore.YELLOW + '\n!!!!! OUCH !!!!!' + Style.RESET_ALL)
    print(Fore.RED + msg + Style.RESET_ALL)
    print('--------------------\n')
    time.sleep(.5)

def run_msg(msg, got_away):
    print(Fore.YELLOW + '\n>>>>> Attempting to run >>>>>\n' + Style.RESET_ALL)
    time.sleep(1)
    if got_away:
        print(Fore.GREEN + msg + Style.RESET_ALL)
    else:
        print(Fore.RED + msg + Style.RESET_ALL)


def enemy_message(msg):
    print(Fore.LIGHTRED_EX + msg)
    print('--------------------\n' + Style.RESET_ALL)
    time.sleep(.5)

def print_menu(msg):
    print(Fore.GREEN + '\n--------------------' + Style.RESET_ALL)
    print(msg)
    print(Fore.YELLOW + '--------------------\n' + Style.RESET_ALL)


def consumable_message(msg):
    print(Fore.BLUE + '\n..........')
    print(Fore.MAGENTA + msg + Style.RESET_ALL)
    print(Fore.BLUE + '.........\n' + Style.RESET_ALL)
    time.sleep(.5)


def armor_message(msg):
    print(Fore.GREEN + '\n][ ][ ][ ][ ][ ][ ][' + Style.RESET_ALL)
    print(msg)
    print(Fore.GREEN + '\n][ ][ ][ ][ ][ ][ ][' + Style.RESET_ALL)
    time.sleep(.5)


def weapon_message(msg):
    print(Fore.YELLOW + '\n||||||||||||||||||||' + Style.RESET_ALL)
    print(msg)
    print(Fore.YELLOW + '\n||||||||||||||||||||' + Style.RESET_ALL)
    time.sleep(.5)

def unknown_direction(msg):
    print(Fore.MAGENTA + '????? ' + msg + ' ?????' + Style.RESET_ALL)


def known_direction(msg):
    print(Fore.GREEN + '-> -> -> -> -> ' + msg + '<- <- <- <- <-' + Style.RESET_ALL)


def found_direction(msg):
    print(Fore.GREEN + '\n????? -> !!!!!!')
    print(msg)
    print('--------------------\n' + Style.RESET_ALL)


def input_int():
    '''Collects user info and loops until a valid number is entered'''
    while(True):
        choice = input()
        try:
                return int(choice)
        except TypeError:
            invalid_choice_msg()
        invalid_choice_msg()
        

def int_or_quit():
     '''Converts user input or press x to leave'''
     while(True):
        choice = input()
        if choice == 'x':
             return False
        else:
            try:
                return int(choice)
            except TypeError:
                invalid_choice_msg()
            invalid_choice_msg()


def inspect_enemy(enemy):
    details = f'''
    NAME: {enemy['name']}
    -----------------------
    HP: {enemy['health']}
    Stngth: {enemy['strength']}
    Speed: {enemy['speed']}
    -----------------------
        {enemy['description']}
    '''
    print(details)
    print()



