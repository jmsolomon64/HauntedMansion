def input_int(error_message):
    '''Collects user info and loops until a valid number is entered'''
    while(True):
        choice = input()
        try:
                return int(choice)
        except TypeError:
            print(error_message)
        print(error_message)