#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# main_en.py - Simple bash emulator in Python with English interface
# Author: Maks-Pacman
# Version: 1.0

# Import necessary modules
import os
import sys
import readline
# Emulator settings
directoria = "/home/maks-pacman/CODING"
runing = True
name = "bash"
home = "/home/maks-pacman/CODING"
# Help commands
help_cmd = {
    "help":"""  help:           Command for this list and for each command. Example: help <command>.
  q/exit:         Exit the program. There are arguments for exiting with clearing: q/exit <-c/-clear>.
  clear:          Command clears the screen. Can be combined with the q/exit command as an argument.
  echo:           Command echo is roughly echo <what you want> output <what you entered after 'echo ' yes, a space.>"""
}

# Help commands with arguments
help_cmd_q = {
    "help":"  q/exit:         Commands q/exit are commands to exit the script. They support arguments such as: <-c/clear>"
}

# Help commands with arguments
help_cmd_clear = {
    "help":"  clear:          Commands clear clears the screen. It is also an argument for the q/exit command in the form -c/-clear"
}

# Help commands with arguments
help_cmd_echo = {
    "help":"  echo:           Comands for outputting what the user wrote after echo. Example: echo hello. Output: hello."
}

# Main loop of operation
while runing:

    # Prompt for command input
    inp = input(f"[{directoria} ] : [{name}] |>> $| ").strip()

    # Exit command without clearing
    if inp == "q" or inp == "exit":
        runing = False
    else:
        # Exit command with clearing
        if inp == "q -c" or inp == "q -clear" or inp == "exit -c" or inp == "exit -clear":
            os.system("cls" if os.name == 'nt' else 'clear')
            runing = False

    # Clear screen command
    if inp == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')

    # Echo command <text>
    if inp.startswith("echo "):
        text = inp[5:].strip()
        print(text)

    # Secret command (secret command)
    if inp == "command":
        print("#%$%#$^$&^$#@$^$^&$%^&^")

    # Help command (without arguments)
    if inp == "help":
        print(help_cmd["help"])
    else:
        # Help command <command> (with arguments)
        if inp == "help q" or inp == "help exit":
            print(help_cmd_q["help"])
        else:
            if inp == "help clear":
                print(help_cmd_clear["help"])
            else:
                if inp == "help echo":
                    print(help_cmd_echo["help"])
                else:
                    # Help command all (all commands)
                    if inp == "help all":
                        print(help_cmd_q["help"])
                        print(help_cmd_clear["help"])
                        print(help_cmd_echo["help"])

    # Handling non-existent commands and errors
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

    # Ignoring empty input and known commands
    if inp in cmd_error_inp:
        ()
    else:
        print(f"{name}: {inp}: command not found")

    # End of main loop