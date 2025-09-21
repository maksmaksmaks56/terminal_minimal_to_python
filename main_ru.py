import os
import readline
import sys
# Настройки

directoria = "/home/maks-pacman/GitHab Realse/Bash"
home_dir = "/home/maks-pacman/GitHab Realse/Bash"

name = "bash"

try:
    os.listdir(directoria)
except FileNotFoundError:
    print(f"{name}:    Рабочей директории не существует.")
    print(f"{name}:    Экстренное завершение програмы.")
    sys.exit(1)
except PermissionError:
    print(f"{name}:    Ошибка получения прав доступа к рабочей директории.")
    print(f"{name}:    Экстренное завершение програмы.")
    sys.exit(1)
except NotADirectoryError:
    print(f"{name}:    Ошибка чтения {directoria} это файл а не директория")
    print(f"{name}:    Экстренное завершения программы")
    sys.exit(1)

try:
    os.listdir(home_dir)
except FileNotFoundError:
    print(f"{name}:    Домашней директории не существует.")
    print(f"{name}:    Экстренное завершение програмы.")
    sys.exit(1)
except PermissionError:
    print(f"{name}:    Ошибка получения прав доступа к домашней директории.")
    print(f"{name}:    Экстренное завершение програмы.")
    sys.exit(1)
except NotADirectoryError:
    print(f"{name}:    Ошибка чтения {home_dir} это файл а не директория")
    print(f"{name}:    Экстренное завершение програмы.")
    sys.exit(1)

help_cmd = {
    "help":"""q/exit: Выход из скрипта.
q/exit -c/--clear: Выход из скрипта с очисткрй экрана.
echo: Выводит текст после, себя пример: echo 1 вывод → 1. 
cd: Переводит вас в назначеную директорию. 
cd ~ : переводит вас в домашнюю директорию. 
ls: показывает все файйлы/папки в донной директории. 
ls -w: показывает все файлы в дериктории которую вы скажете. 
ls -m --file/--folder: Создает в данной директории файл/папку. 
ls -rm --file/--folder: Удаляет файл/папку в данной директории.
help: Этот командный список."""
}

while True:

    inp = input(f"{directoria}|{name}| >>> $ ").strip()

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
            print(f"{name}: cd: Такого каталога не существует {home_dir}")
        except PermissionError:
            print(f"{name}: cd: Отказано в доступе {home_dir}")
        except NotADirectoryError:
            print(f"{name}: cd: {home_dir}: Это путь к файлу а не директории")

    elif inp.startswith("cd "):
        dir_cd = inp[3:].strip()
        try:
            os.listdir(dir_cd)
            directoria = dir_cd
        except FileNotFoundError:
            print(f"{name}: cd: Такой директории не существует {dir_cd}")
        except PermissionError:
            print(f"{name}: cd: Отказано в доступе {dir_cd}")
        except NotADirectoryError:
            print(f"{name}: cd: {dir_cd}: Это путь к файлу а не директории")
    
    if inp.startswith("ls -m --folder "):
        name_folder = inp[15:].strip()
        new_folder_path = os.path.join(directoria, name_folder)
        try:
            os.listdir(directoria)
            os.mkdir(new_folder_path)
            print("Успешно!")
        except FileExistsError:
            print(f"{name}: ls: Такая папка уже существует")
        except PermissionError:
            print(f"{name}: ls: отказано в доступе {directoria}")

    elif inp.startswith("ls -m --file "):
        name_file = inp[13:].strip()
        new_file_path = os.path.join(directoria, name_file)
        try:
            os.listdir(directoria)
            if os.path.exists(new_file_path):
                print(f"{name}: ls: Такой файл уже существует")
            else:
                with open(new_file_path, "w") as f:
                    pass
                print("Успешно!")
        except PermissionError:
            print(f"{name}: ls: Отказано в доступе {new_file_path}")

    elif inp.startswith("ls -rm --folder "):
        name_folder = inp[16:].strip()
        delete_folder_path = os.path.join(directoria, name_folder)
        try:
            os.listdir(directoria)
            os.removedirs(delete_folder_path)
            print("Успешно!")
        except PermissionError:
            print(f"{name}: ls: Отказано в доступе {delete_folder_path}")
        except FileNotFoundError:
            print(f"{name}: ls: Такого файла/папки не существует {name_folder}")

    elif inp.startswith("ls -rm --file "):
        name_file = inp[14:].strip()
        delete_file_path = os.path.join(directoria, name_file)
        try:
            os.listdir(directoria)
            os.remove(delete_file_path)
            print("Успешно!")
        except PermissionError:
            print(f"{name}: ls: Отказано в доступе {delete_file_path}")
        except FileNotFoundError:
            print(f"{name}: ls: Нет такого файла или каталога {name_file}")

    elif inp == "ls":
        print(os.listdir(directoria))

    elif inp.startswith("ls -w "):
        dire = inp[6:].strip()
        try:
            print(os.listdir(dire))
        except PermissionError:
            print(f"{name}: ls: {dire}: доступ запрещен")
        except FileNotFoundError:
            print(f"{name}: ls: {dire}: Такой директории не существует")
        except NotADirectoryError:
            print(f"{name}: ls: Это путь к файлу а не директории")


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
        f"cd":"",
        f"help{inp[4:]}":""
    }

    if inp not in проверка:
        print(f"{name}: {inp}: Неизвестная команда")


sys.exit(1)