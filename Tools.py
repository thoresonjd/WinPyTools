from pynput.keyboard import Key, Controller
# import screen_brightness_control as screen
import win32con
import win32gui
import ctypes
import os

class Tools:
    
    def __init__(self):
        """ Read all filenames from cursor directory
        Save original cursor
        """

        self.current_cursor = 0
        self.cursors = []
        path = 'C:\\Windows\\Cursors'
        files = os.listdir(path)
        for file in files:
            if os.path.isfile(filename := os.path.join(path, file)):
                self.cursors.append(filename)
        self.save_cursor()
        
    def save_cursor(self):
        """ Save system cursor """

        cursor = win32gui.LoadImage(0, 32512, win32con.IMAGE_CURSOR, 
                                    0, 0, win32con.LR_SHARED)
        self.save_system_cursor = ctypes.windll.user32.CopyImage(cursor, win32con.IMAGE_CURSOR, 
                                    0, 0, win32con.LR_COPYFROMRESOURCE)

    def restore_cursor(self):
        """ Restor system cursor"""

        ctypes.windll.user32.SetSystemCursor(self.save_system_cursor, 32512)
        ctypes.windll.user32.DestroyCursor(self.save_system_cursor)

    def change_cursor(self, scroll_direction : int):
        """ Change system cursor
        
        :param scroll_direction: Direction of the mouse scroll wheel
        """

        self.current_cursor = (self.current_cursor + scroll_direction) % len(self.cursors)

        try:
            cursor = win32gui.LoadImage(0, self.cursors[self.current_cursor], win32con.IMAGE_CURSOR, 
                                        0, 0, win32con.LR_LOADFROMFILE)
            ctypes.windll.user32.SetSystemCursor(cursor, 32512)
            ctypes.windll.user32.DestroyCursor(cursor)
        except:
            print('Could not change cursor')

    def change_volume(self, scroll_direction : int):
        """ Increase or decrease system volume
        
        :param scroll_direction: Direction of the mouse scroll wheel
        """

        def increase():
            """ Increase volume """

            keyboard.press(Key.media_volume_up) 
            keyboard.release(Key.media_volume_up)

        def decrease():
            """ Decrease volume """

            keyboard.press(Key.media_volume_down)
            keyboard.release(Key.media_volume_down)
        
        keyboard = Controller()
        if scroll_direction > 0:
            [increase() for _ in range(3)]
        elif scroll_direction < 0:
            [decrease() for _ in range(3)]

    # def change_brightness(self, scroll_direction : int):
    #     """ Increase or decrease screen brightness
        
    #     :param scroll_direction: Direction of the mouse scroll wheel
    #     """

    #     print(f'func1: {scroll_direction}')
    #     try:
    #         current_brightness = screen.get_brightness()
    #         new_brightness = [brightness + scroll_direction for brightness in current_brightness]
    #         for i in range(len(new_brightness)):
    #             screen.set_brightness(new_brightness[i])
    #     except:
    #         print('Could not change brightness')