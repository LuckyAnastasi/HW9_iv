from handler import *

# list of commands
COMMANDS = {'hello': greet, 'add': add, 'change': change, 'phone': phone, 'show all': show_all,
            'good bye': goodbye, 'exit': goodbye, 'close': goodbye}


def main():
    contacts_list = {}
    while True:
        user_command = input('Please enter a command >>> ')
        for k, v in COMMANDS.items():
            if k in user_command.lower():
                args = user_command[len(k):].split()  # find title of commands
                result = COMMANDS[k](contacts_list, *args)  # create list of title commands
                if result is None:
                    exit()
                print(result)
                break
        else:
            print('Unknown command! Enter again!\n')


if __name__ == '__main__':
    main()
