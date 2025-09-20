import os
import readline
import sys
# Настройки

directoria = "/home/maks-pacman/Test GPT"
home_dir = "/home/maks-pacman/Test GPT"

name = "bash"

try:
    os.listdir(directoria)
except FileNotFoundError:
    print(f"{name}:    There are no working folders.")
    print(f"{name}:    Emergency termination of the program.")
    sys.exit(1)
except PermissionError:
    print(f"{name}:    ")
    print(f"{name}:    Emergency termination of the program.")
    sys.exit(1)

try:
    os.listdir(home_dir)
except FileNotFoundError:
    print(f"{name}:    The home folder does not exist.")
    print(f"{name}:    Emergency termination of the program.")
    sys.exit(1)
except PermissionError:
    print(f"{name}:    Error obtaining access rights to home folder.")
    print(f"{name}:    Emergency termination of the program.")
    sys.exit(1)

while True:

    inp = input(f"{directoria}|{name}| >>> $ ").strip()

    if not inp:
        pass

    if inp == "q" or inp == "exit":
        break
    elif inp == "q -c" or inp == "q --clear" or inp == "exit -c" or inp == "exit --clear":
        os.system('cls' if os.name == 'nt' else 'clear')
        break

    if inp == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')

    if inp.startswith("echo "):
        text = inp[5:].strip()
        print(text)

    elif inp == "echo":
        pass
    
    if inp == "cd ~":
        try:
            os.listdir(home_dir)
            directoria = home_dir
        except FileNotFoundError:
            print(f"{name}: cd: Such a catalog does not exist. {home_dir}")
        except PermissionError:
            print(f"{name}: cd: Access denied {home_dir}")

    elif inp.startswith("cd "):
        dir_cd = inp[3:].strip()
        try:
            os.listdir(dir_cd)
            directoria = dir_cd
        except FileNotFoundError:
            print(f"{name}: cd: Such directory does not exist {dir_cd}")
        except PermissionError:
            print(f"{name}: cd: Access denied {dir_cd}")
    
    if inp.startswith("ls -m --folder "):
        name_folder = inp[15:].strip()
        new_folder_path = os.path.join(directoria, name_folder)
        try:
            os.listdir(directoria)
            os.mkdir(new_folder_path)
            print("Successfully!")
        except FileExistsError:
            print(f"{name}: ls: This folder already exists.")
        except PermissionError:
            print(f"{name}: ls: Access denied {directoria}")

    elif inp.startswith("ls -m --file "):
        name_file = inp[13:].strip()
        new_file_path = os.path.join(directoria, name_file)
        try:
            os.listdir(directoria)
            if os.path.exists(new_file_path):
                print(f"{name}: ls: This file already exists")
            else:
                with open(new_file_path, "w") as f:
                    pass
                print("Successfully!")
        except PermissionError:
            print(f"{name}: ls: Access denied {new_file_path}")

    elif inp.startswith("ls -rm --folder "):
        name_folder = inp[16:].strip()
        delete_folder_path = os.path.join(directoria, name_folder)
        try:
            os.listdir(directoria)
            os.removedirs(delete_folder_path)
            print("Successfully!")
        except PermissionError:
            print(f"{name}: ls: Access denied {delete_folder_path}")
        except FileNotFoundError:
            print(f"{name}: ls: This file/folder does not exist {name_folder}")

    elif inp.startswith("ls -rm --file "):
        name_file = inp[14:].strip()
        delete_file_path = os.path.join(directoria, name_file)
        try:
            os.listdir(directoria)
            os.remove(delete_file_path)
            print("Successfully!")
        except PermissionError:
            print(f"{name}: ls: Access denied {delete_file_path}")
        except FileNotFoundError:
            print(f"{name}: ls: No such file or directory {name_file}")

    elif inp == "ls":
        print(os.listdir(directoria))

    elif inp.startswith("ls -w "):
        dire = inp[6:].strip()
        try:
            print(os.listdir(dire))
        except PermissionError:
            print(f"{name}: ls: {dire}: Access denied")
        except FileNotFoundError:
            print(f"{name}: ls: {dire}: Such directory does not exist")

    проверка = {
        "":"",
        "q":"",
        "exit":"",
        "q -c":"",
        "q --clear":"",
        "exit -c":"",
        "exit --clear":"",
        "clear":"",
        "echo":"",
        f"echo {inp[5:]}":"",
        "ls":"",
        f"ls {inp[3:]}":"",
        f"cd {inp[3:]}":"",
        f"cd":""
    }

    if inp not in проверка:
        print(f"{name}: {inp}: Comand not found")

sys.exit(1)
