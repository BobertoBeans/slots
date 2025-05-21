from pynput import keyboard

def on_press(key):
    try:
        if key == keyboard.Key.space:
            print("Spacebar pressed! Triggering action...")
            # Place your desired action here
            # For example, you could call a function or change a variable
    except AttributeError:
        # Ignore special keys that don't have a character representation
        pass