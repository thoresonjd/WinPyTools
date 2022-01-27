from pynput.keyboard import Key, Controller
# import screen_brightness_control as screen

def change_cursor(scroll_direction : int):
    """ Shuffle through cursors
    
    :param scroll_direction: Direction of the mouse scroll wheel
    """
    print(f'c: {scroll_direction}')

def change_volume(scroll_direction : int):
    """ Increase or decrease system volume
    
    :param scroll_direction: Direction of the mouse scroll wheel
    """

    def increase():
        keyboard.press(Key.media_volume_up) 
        keyboard.release(Key.media_volume_up)

    def decrease():
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
    
    keyboard = Controller()
    if scroll_direction > 0:
        [increase() for _ in range(3)]
    elif scroll_direction < 0:
        [decrease() for _ in range(3)]

def change_brightness(scroll_direction : int):
    """ Increase or decrease screen brightness
    
    :param scroll_direction: Direction of the mouse scroll wheel
    """
    print(f'func1: {scroll_direction}')
#     try:
#         current_brightness = screen.get_brightness()
#         new_brightness = [brightness + scroll_direction for brightness in current_brightness]
#         for i in range(len(new_brightness)):
#             screen.set_brightness(new_brightness[i])
#     except:
#         print('Could not change brightness')