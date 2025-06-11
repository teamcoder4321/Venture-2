from pynput.keyboard import Key,Controller

from time import sleep

keyboard = Controller()

def volumeup():
    """Press a key on the keyboard."""
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)  # Adding a small delay to ensure the key press is registered

def volumedown():
    """Press a key on the keyboard."""
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)  # Adding a small delay to ensure the key press is registered
