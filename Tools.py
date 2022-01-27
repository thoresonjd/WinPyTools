from pynput.keyboard import Key, Controller
# import screen_brightness_control as screen

# def change_brightness(scroll_direction : int):
#     # print(f'func1: {scroll_direction}')
#     try:
#         current_brightness = screen.get_brightness()
#         new_brightness = [brightness + scroll_direction for brightness in current_brightness]
#         for i in range(len(new_brightness)):
#             screen.set_brightness(new_brightness[i])
#     except:
#         print('Could not change brightness')

def change_volumn(scroll_direction : int):
    keyboard = Controller()
    if scroll_direction > 0:
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
    elif scroll_direction < 0:
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)