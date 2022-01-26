""" WinPyTools
(c) Justin Thoreson
Created on 26 January 2022

Sources:
https://pypi.org/project/pynput/
https://nitratine.net/blog/post/how-to-make-hotkeys-in-python/
"""

# Import modules
from Hotkeys import Hotkeys

def main():
    hotkey_program = Hotkeys()
    hotkey_program.listen()

if __name__ == '__main__':
    main()