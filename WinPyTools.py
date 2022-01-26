""" WinPyTools
(c) Justin Thoreson
Created on 26 January 2022

Sources:
https://pypi.org/project/pynput/
https://nitratine.net/blog/post/how-to-make-hotkeys-in-python/
"""

# Import modules
from Keyboard import Keyboard as Listener

def main():
    keyboard = Listener()
    keyboard.listen()

if __name__ == '__main__':
    main()