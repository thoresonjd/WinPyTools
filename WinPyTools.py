""" WinPyTools
(c) Justin Thoreson
Created on 26 January 2022
"""

from HotkeyController import HotkeyController

def main():
    hotkey_program = HotkeyController()
    hotkey_program.listen()

if __name__ == '__main__':
    main()