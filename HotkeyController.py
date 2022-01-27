from pynput.keyboard import Key, KeyCode, Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
import Tools

class HotkeyController:

    def __init__(self):
        """ Map hotkey combinations to functions
        Initialiaze the set of currently pressed keys
        """
        self.COMBINATIONS = {
            frozenset([Key.shift, KeyCode(vk=ord('C'))]): Tools.change_cursor,
            frozenset([Key.shift, KeyCode(vk=ord('V'))]): Tools.change_volume,
            frozenset([Key.shift, KeyCode(vk=ord('B'))]): Tools.change_brightness
        }
        self.pressed = set()
        self.current_combo = None

        print('Init keyboard listener')

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

        # for COMBO in self.COMBINATIONS:
        #     if self.is_hotkey_activated(COMBO):
        #         self.COMBINATIONS[COMBO]()

        for COMBO in self.COMBINATIONS:
            if self.is_hotkey_activated(COMBO):
                self.current_combo = COMBO

    def on_release(self, key : Key):
        """ Remove key from set when released

        :param key: The key that is released
        """
        self.current_combo = None
        virtual_key = self.get_virtual_key(key)
        self.pressed.remove(virtual_key)

    def on_scroll(self, x, y, dx, dy):
        if self.current_combo:
            self.COMBINATIONS[self.current_combo](dy)

    def listen(self):
        """ Listen for device input """

        # Init threads
        keyboard_listener = KeyboardListener(on_press = self.on_press, on_release = self.on_release, IS_TRUSTED = True)
        mouse_listener = MouseListener(on_scroll=self.on_scroll, IS_TRUSTED = True)

        # Start threads
        keyboard_listener.start()
        mouse_listener.start()

        # Join threads
        keyboard_listener.join()
        mouse_listener.join()