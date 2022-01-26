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

# Set of currently pressed keys
pressed = set()

def get_virtual_key(key):
    """ Get the virtual key code of a key
    
    :param key: A key from the keyboard
    :return: The virtual key code of a key
    """
    return key.vk if hasattr(key, 'vk') else key.value.vk

def is_hotkey_activated(combination):
    """ Determine if the hotkey combination is activated 
    
    :param combination:
    :return: True if combination activated, false if not
    """
    return all([get_virtual_key(key) in pressed for key in combination])

def on_press(key):
    """ Add key to set. Check is hotkey combination is activated.
    Execute respective hotkey combination function
    :param key: The key that is pressed
    """

    virtual_key = get_virtual_key(key)
    pressed.add(virtual_key)

    for COMBO in COMBINATIONS:
        if is_hotkey_activated(COMBO):
            COMBINATIONS[COMBO]()

def on_release(key):
    """ Remove key from set when released

    :param key: The key that is released
    """
    virtual_key = get_virtual_key(key)
    pressed.remove(virtual_key)

def listen():
    """ Listen for keyboard input """
    with Listener(on_press = on_press, on_release = on_release, IS_TRUSTED = True) as listener:
        listener.join()

def main():
    listen()

if __name__ == '__main__':
    main()