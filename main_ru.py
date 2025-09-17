# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# main_ru.py - Простой эмулятор bash на Python с русским интерфейсом
# Автор: Maks-Pacman
# Версия: 1.0

# Импорт необходимых модулей
import os
import sys
import readline

# Настройки эмулятора
directoria = "/home/maks-pacman/CODING"
runing = True
name = "bash"
home = "/home/maks-pacman/CODING"
# Команды помощи
help_cmd = {
    "help":"""  help:           Команда для этого списка и для каждой команды. пример: help <команда>.
  q/exit:         Выход из программы. есть аргументы для выхода с очисткой: q/exit <-c/-clear>.
  clear:          Команда очищяет екран. обьединима с командой q/exit в каччестве аргумента.
  echo:           Команда echo это примерно это echo <что хотите> вывод <то что вы ввели после 'echo ' да имменно пробел.>"""
}

# Команды помощи с аргументами
help_cmd_q = {
    "help":"  q/exit:         Команда q/exit это команды выхода из скрипта. подержывают такие аргументы как: <-c/clear>"
}

# Команды помощи с аргументами
help_cmd_clear = {
    "help":"  clear:          Команда clear очищяет екран. а также является аргументом для команды q/exit в виде -c/-clear"
}

# Команды помощи с аргументами
help_cmd_echo = {
    "help":"  echo:           Команда для вывода того что написал user после echo. пример: echo привет. вывод: привет."
}
# Основной цикл работы
while runing:
# Приглашение к вводу команды
    inp = input(f"[{directoria} ] : [{name}] |>> $| ").strip()
    # Команда выхода без очистки
    if inp == "q" or inp == "exit":
        runing = False
    else:
    # Команда выхода с очисткой
        if inp == "q -c" or inp == "q -clear" or inp == "exit -c" or inp == "exit -clear":
            os.system("cls" if os.name == 'nt' else 'clear')
            runing = False
    # Команда очистки экрана
    if inp == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    # Команда echo <текст>
    if inp.startswith("echo "):
        text = inp[5:].strip()
        print(text)
    # Команда secret (секретная команда)
    if inp == "command":
        print("#%$%#$^$&^$#@$^$^&$%^&^")
    # Команда help (без аргументов)
    if inp == "help":
        print(help_cmd["help"])
    else:
        # Команда help <команда> (с аргументами)
        if inp == "help q" or inp == "help exit":
            print(help_cmd_q["help"])
        else:
            if inp == "help clear":
                print(help_cmd_clear["help"])
            else:
                if inp == "help echo":
                    print(help_cmd_echo["help"])
                else:
                    # Команда help all (все команды)
                    if inp == "help all":
                        print(help_cmd_q["help"])
                        print(help_cmd_clear["help"])
                        print(help_cmd_echo["help"])
    # Обработка несуществующих команд и ошибок
    cmd_error_inp = {
        f"":"",
        f"q":"",
        f"exit":"",
        f"q -c":"",
        f"q -clear":"",
        f"exit -c":"",
        f"exit -clear":"",
        f"clear":"",
        f"help":"",
        f"help q":"",
        f"help exit":"",
        f"help clear":"",
        f"help echo":"",
        f"help all":"",
        f"echo{inp[4:]}":"",
        f"command":""
    }

    # Игнорирование пустого ввода и известных команд

    if inp in cmd_error_inp:
        ()
    else:
        print(f"{name}: {inp}: Такой команды не существует.")

    # Конец основного цикла