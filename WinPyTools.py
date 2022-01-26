""" WinPyTools
(c) Justin Thoreson
Created on 26 January 2022

Sources:
https://nitratine.net/blog/post/how-to-make-hotkeys-in-python/
"""

# Import modules
from HotkeyListener import HotkeyListener

def main():
    listener = HotkeyListener()
    listener.listen()

if __name__ == '__main__':
    main()