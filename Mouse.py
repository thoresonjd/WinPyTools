from pynput import mouse

class Mouse:
    def __init__(self):
        print('Init mouse listener')

    def on_scroll(self, x, y, dx, dy):
        print('Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up', dy))

    def listen(self):
        with mouse.Listener(on_scroll=self.on_scroll) as listener:
            listener.join()