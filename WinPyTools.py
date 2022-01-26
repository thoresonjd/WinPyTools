""" WinPyTools
(c) Justin Thoreson
Created on 26 January 2022

Sources:
https://nitratine.net/blog/post/how-to-make-hotkeys-in-python/
"""

# Import modules
from pynput.keyboard import Key, KeyCode, Listener

# Functions to execute
def func1():
    print('func1')

def func2():
    print('func2')

# Map functions to hotkey combinations
COMBINATIONS = {
    frozenset([Key.shift, KeyCode(vk=ord('D'))]): func1,
    frozenset([Key.shift, KeyCode(vk=ord('L'))]): func2
}

def main():
    print('Hello, world!')

if __name__ == '__main__':
    main()