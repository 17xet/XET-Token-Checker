import os
import time
from requests import get, post
from random import randint
from pystyle import Colors, Colorate

current_fg1 = Colors.DynamicMIX((Colors.blue, Colors.pink))
current_fg2 = Colors.DynamicMIX((Colors.pink, Colors.blue))

os.system('title ghost')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def variant1(token):
    response = get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})
    return True if response.status_code == 200 else False

def variant2(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
        return False
    else:
        return True

def variant2_Status(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if response.status_code == 401:
        return 'Invalid'
    elif "You need to verify your account in order to perform this action." in str(response.content):
        return 'Phone Lock'
    else:
        return 'Valid'

def check_tokens():
    try:
        checked = []
        with open('tokens.txt', 'r') as tokens:
            for token in tokens.read().split('\n'):
                half_token = token[:len(token)//2] + "..."
                if len(token) > 15 and token not in checked and variant2(token):
                    print(Colorate.Horizontal(current_fg1, f'[+] Token: {half_token} is Valid'))
                    checked.append(token)
                else:
                    print(Colorate.Horizontal(current_fg2, f'[x] Token: {half_token} is Invalid'))
        if len(checked) > 0:
            save = input(Colorate.Horizontal(current_fg1, f'{len(checked)} valid tokens\nSave to File (y/n)')).lower()
            if save == 'y':
                name = randint(100000000, 9999999999)
                with open(f'{name}.txt', 'w') as saveFile:
                    saveFile.write('\n'.join(checked))
                print(Colorate.Horizontal(current_fg1, f'Tokens Saved to {name}.txt File!'))
        input(Colorate.Horizontal(current_fg1, 'Press Enter For Exit...'))
    except:
        input(Colorate.Horizontal(current_fg1, 'Can\'t Open "tokens.txt" File!'))

def change_color_theme():
    global current_fg1, current_fg2
    clear_screen()
    print(Colorate.Horizontal(Colors.DynamicMIX((Colors.red, Colors.blue, Colors.green)), "1. Color Cycle"))
    print(Colorate.Horizontal(Colors.DynamicMIX((Colors.cyan, Colors.blue)), "2. Ocean"))
    print(Colorate.Horizontal(Colors.DynamicMIX((Colors.red, Colors.orange, Colors.yellow)), "3. Fire"))
    print(Colorate.Horizontal(Colors.DynamicMIX((Colors.pink, Colors.purple, Colors.blue)), "4. Cotton Candy"))
    print(Colorate.Horizontal(Colors.DynamicMIX((Colors.green, Colors.black)), "5. Matrix"))

    theme_choice = input("Enter theme number: ").strip()

    if theme_choice == '1':
        current_fg1 = Colors.DynamicMIX((Colors.red, Colors.blue, Colors.green))
        current_fg2 = Colors.DynamicMIX((Colors.green, Colors.blue, Colors.red))
    elif theme_choice == '2':
        current_fg1 = Colors.DynamicMIX((Colors.cyan, Colors.blue))
        current_fg2 = Colors.DynamicMIX((Colors.blue, Colors.cyan))
    elif theme_choice == '3':
        current_fg1 = Colors.DynamicMIX((Colors.red, Colors.orange, Colors.yellow))
        current_fg2 = Colors.DynamicMIX((Colors.orange, Colors.red))
    elif theme_choice == '4':
        current_fg1 = Colors.DynamicMIX((Colors.pink, Colors.purple, Colors.blue))
        current_fg2 = Colors.DynamicMIX((Colors.blue, Colors.pink))
    elif theme_choice == '5':
        current_fg1 = Colors.DynamicMIX((Colors.green, Colors.black))
        current_fg2 = Colors.DynamicMIX((Colors.black, Colors.green))
    else:
        print(Colorate.Horizontal(Colors.red, "Invalid choice. Try again."))
        time.sleep(1)
        clear_screen()
        return

    clear_screen()
    print(Colorate.Horizontal(current_fg1, "Theme applied!"))
    input(Colorate.Horizontal(current_fg1, 'Press Enter to return to the main menu...'))
    clear_screen()

def show_credits():
    clear_screen()
    print(Colorate.Horizontal(current_fg1, "Made with love by 17xet."))
    print(Colorate.Horizontal(current_fg1, "https://discord.gg/mx9raXzU9S"))
    print(Colorate.Horizontal(current_fg1, "https://www.youtube.com/@17xet"))
    print(Colorate.Horizontal(current_fg1, "https://github.com/17xet"))
    input(Colorate.Horizontal(current_fg1, 'Press Enter to return to the main menu...'))
    clear_screen()

def main_menu():
    while True:
        clear_screen()

        ascii_art = """
		██╗  ██╗███████╗████████╗
		╚██╗██╔╝██╔════╝╚══██╔══╝
		 ╚███╔╝ █████╗     ██║   
		 ██╔██╗ ██╔══╝     ██║   
		██╔╝ ██╗███████╗   ██║   
		╚═╝  ╚═╝╚══════╝   ╚═╝   
        """

        split_line = ascii_art.split('\n')
        middle_index = len(split_line) // 2

        for i in range(middle_index):
            print(Colorate.Horizontal(current_fg1, split_line[i]))
        for i in range(middle_index, len(split_line)):
            print(Colorate.Horizontal(current_fg2, split_line[i]))

        print(Colorate.Horizontal(current_fg1, "[1] Token checker"))
        print(Colorate.Horizontal(current_fg1, "[2] Change Theme"))
        print(Colorate.Horizontal(current_fg1, "[3] Credits"))
        print(Colorate.Horizontal(current_fg1, "[4] Exit"))

        choice = input(Colorate.Horizontal(current_fg1, "Enter your choice: ")).strip()

        if choice == '1':
            check_tokens()
        elif choice == '2':
            change_color_theme()
        elif choice == '3':
            show_credits()
        elif choice == '4':
            print(Colorate.Horizontal(current_fg1, "Exiting..."))
            break
        else:
            print(Colorate.Horizontal(current_fg1, "Invalid choice. Try again."))
            input(Colorate.Horizontal(current_fg1, 'Press Enter to return to the menu...'))
            clear_screen()

if __name__ == "__main__":
    main_menu()
