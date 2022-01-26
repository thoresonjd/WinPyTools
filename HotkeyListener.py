from typing import Any
from xmlrpc.client import boolean
from pynput.keyboard import Key, KeyCode, Listener
import func1, func2

class HotkeyListener:
    def __init__(self):
        """ Map hotkey combinations to functions
        Initialiaze the set of currently pressed keys
        """
        self.COMBINATIONS = {
            frozenset([Key.shift, KeyCode(vk=ord('1'))]): func1.func1,
            frozenset([Key.shift, KeyCode(vk=ord('2'))]): func2.func2
        }
        self.pressed = set()

    def get_virtual_key(self, key : Key) -> int:
        """ Get the virtual key code of a key
        
        :param key: A key from the keyboard
        :return: The virtual key code of a key
        """
        return key.vk if hasattr(key, 'vk') else key.value.vk

    def is_hotkey_activated(self, combination : frozenset) -> bool:
        """ Determine if the hotkey combination is activated 
        
        :param combination:
        :return: True if combination activated, false if not
        """
        return all([self.get_virtual_key(key) in self.pressed for key in combination])

    def on_press(self, key : Key):
        """ Add key to set. Check is hotkey combination is activated.
        Execute respective hotkey combination function

        :param key: The key that is pressed
        """
        virtual_key = self.get_virtual_key(key)
        self.pressed.add(virtual_key)

        for COMBO in self.COMBINATIONS:
            if self.is_hotkey_activated(COMBO):
                self.COMBINATIONS[COMBO]()

    def on_release(self, key : Key):
        """ Remove key from set when released

        :param key: The key that is released
        """
        virtual_key = self.get_virtual_key(key)
        self.pressed.remove(virtual_key)

    def listen(self):
        """ Listen for keyboard input """
        with Listener(on_press = self.on_press, on_release = self.on_release, IS_TRUSTED = True) as listener:
            listener.join()