import os
import readline
import sys
# Settings

directoria = "/home/maks-pacman/GitHab Realse/Bash"
home_dir = "/home/maks-pacman/GitHab Realse/Bash"

name = "bash"

# Check working directory
try:
    os.listdir(directoria)
except FileNotFoundError:
    print(f"{name}:    Working directory does not exist.")
    print(f"{name}:    Emergency program termination.")
    sys.exit(1)
except PermissionError:
    print(f"{name}:    Permission denied when accessing working directory.")
    print(f"{name}:    Emergency program termination.")
    sys.exit(1)
except NotADirectoryError:
    print(f"{name}:    Error reading {directoria}, it is a file not a directory")
    print(f"{name}:    Emergency program termination.")
    sys.exit(1)

# Check home directory
try:
    os.listdir(home_dir)
except FileNotFoundError:
    print(f"{name}:    Home directory does not exist.")
    print(f"{name}:    Emergency program termination.")
    sys.exit(1)
except PermissionError:
    print(f"{name}:    Permission denied when accessing home directory.")
    print(f"{name}:    Emergency program termination.")
    sys.exit(1)
except NotADirectoryError:
    print(f"{name}:    Error reading {home_dir}, it is a file not a directory")
    print(f"{name}:    Emergency program termination.")
    sys.exit(1)

# Help command list
help_cmd = {
    "help":"""q/exit: Exit the script.
q/exit -c/--clear: Exit the script and clear the screen.
echo: Prints the text after itself, example: echo 1 → output 1.
cd: Move to the specified directory.
cd ~ : Move to the home directory.
ls: Shows all files/folders in the current directory.
ls -w: Shows all files in the directory you specify.
ls -m --file/--folder: Creates a file/folder in the current directory.
ls -rm --file/--folder: Deletes a file/folder in the current directory.
help: This command list."""
}

while True:

    inp = input(f"{directoria}|{name}| >>> $ ").strip()

    if not inp:
        pass

    if inp == "help":
        print(help_cmd["help"])

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
            print(f"{name}: cd: No such directory {home_dir}")
        except PermissionError:
            print(f"{name}: cd: Permission denied {home_dir}")
        except NotADirectoryError:
            print(f"{name}: cd: {home_dir}: Is a file, not a directory")

    elif inp.startswith("cd "):
        dir_cd = inp[3:].strip()
        try:
            os.listdir(dir_cd)
            directoria = dir_cd
        except FileNotFoundError:
            print(f"{name}: cd: No such directory {dir_cd}")
        except PermissionError:
            print(f"{name}: cd: Permission denied {dir_cd}")
        except NotADirectoryError:
            print(f"{name}: cd: {dir_cd}: Is a file, not a directory")
    
    if inp.startswith("ls -m --folder "):
        name_folder = inp[15:].strip()
        new_folder_path = os.path.join(directoria, name_folder)
        try:
            os.listdir(directoria)
            os.mkdir(new_folder_path)
            print("Success!")
        except FileExistsError:
            print(f"{name}: ls: Folder already exists")
        except PermissionError:
            print(f"{name}: ls: Permission denied {directoria}")

    elif inp.startswith("ls -m --file "):
        name_file = inp[13:].strip()
        new_file_path = os.path.join(directoria, name_file)
        try:
            os.listdir(directoria)
            if os.path.exists(new_file_path):
                print(f"{name}: ls: File already exists")
            else:
                with open(new_file_path, "w") as f:
                    pass
                print("Success!")
        except PermissionError:
            print(f"{name}: ls: Permission denied {new_file_path}")

    elif inp.startswith("ls -rm --folder "):
        name_folder = inp[16:].strip()
        delete_folder_path = os.path.join(directoria, name_folder)
        try:
            os.listdir(directoria)
            os.removedirs(delete_folder_path)
            print("Success!")
        except PermissionError:
            print(f"{name}: ls: Permission denied {delete_folder_path}")
        except FileNotFoundError:
            print(f"{name}: ls: No such file or folder {name_folder}")

    elif inp.startswith("ls -rm --file "):
        name_file = inp[14:].strip()
        delete_file_path = os.path.join(directoria, name_file)
        try:
            os.listdir(directoria)
            os.remove(delete_file_path)
            print("Success!")
        except PermissionError:
            print(f"{name}: ls: Permission denied {delete_file_path}")
        except FileNotFoundError:
            print(f"{name}: ls: No such file or directory {name_file}")

    elif inp == "ls":
        print(os.listdir(directoria))

    elif inp.startswith("ls -w "):
        dire = inp[6:].strip()
        try:
            print(os.listdir(dire))
        except PermissionError:
            print(f"{name}: ls: {dire}: Permission denied")
        except FileNotFoundError:
            print(f"{name}: ls: {dire}: No such directory")
        except NotADirectoryError:
            print(f"{name}: ls: {dire}: Is a file, not a directory")

    # Command validation
    validation = {
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
        f"cd":"",
        f"help{inp[4:]}":""
    }

    if inp not in validation:
        print(f"{name}: {inp}: Unknown command")

sys.exit(1)